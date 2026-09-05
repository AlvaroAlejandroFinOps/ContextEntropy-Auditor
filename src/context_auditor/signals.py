from typing import Dict, Any, List
from src.context_auditor.models import AuditInput

def estimate_tokens(text: str) -> int:
    """
    Fallback deterministic token estimator. 
    Assumes roughly 4 characters per token as a standard heuristic.
    """
    if not text:
        return 0
    return max(1, len(text) // 4)

def extract_deterministic_signals(audit_input: AuditInput) -> Dict[str, Any]:
    """
    Computes verifiable, deterministic metrics from the audited context.
    Does not use an LLM.
    """
    signals = {}
    
    # 1. Message & Turn Counts
    signals["message_count"] = len(audit_input.messages)
    signals["user_turns"] = sum(1 for m in audit_input.messages if m.role == "user")
    signals["assistant_turns"] = sum(1 for m in audit_input.messages if m.role == "assistant")
    
    # 2. Token Estimations
    total_chars = sum(len(m.content) for m in audit_input.messages)
    total_chars += sum(len(d.content) for d in audit_input.documents)
    total_chars += sum(len(t.result) for t in audit_input.tool_events)
    signals["estimated_tokens"] = estimate_tokens("a" * total_chars)
    
    context_limit = audit_input.audit_configuration.get("context_limit_tokens", 128000)
    signals["context_utilization_ratio"] = round(signals["estimated_tokens"] / context_limit, 4)

    # 3. Documents & Sources
    signals["document_count"] = len(audit_input.documents)
    unique_sources = set(d.source for d in audit_input.documents if d.source)
    signals["unique_sources"] = len(unique_sources)

    # 4. Exact Duplication Check (Content level)
    content_hashes = set()
    exact_duplicates = 0
    for doc in audit_input.documents:
        if doc.content in content_hashes:
            exact_duplicates += 1
        else:
            content_hashes.add(doc.content)
    signals["exact_document_duplicates"] = exact_duplicates

    # 5. ID Integrity
    all_ids = [m.id for m in audit_input.messages] + [d.id for d in audit_input.documents] + [t.id for t in audit_input.tool_events]
    unique_ids = set(all_ids)
    signals["duplicate_ids_found"] = len(all_ids) - len(unique_ids)

    # 6. Tool Result Replacements (Multiple tool events with same tool_name but different results)
    tool_calls_by_name = {}
    replaced_tools = 0
    for t in audit_input.tool_events:
        if t.tool_name in tool_calls_by_name:
            replaced_tools += 1
        tool_calls_by_name[t.tool_name] = t.result
    signals["superseded_tool_results"] = replaced_tools

    # 7. Last Explicit Objective Recency
    # Distance from the end of the conversation to the last user message
    if signals["user_turns"] > 0:
        last_user_index = -1
        for i, m in enumerate(reversed(audit_input.messages)):
            if m.role == "user":
                last_user_index = i
                break
        signals["messages_since_last_user_turn"] = last_user_index
    else:
        signals["messages_since_last_user_turn"] = -1

    return signals
