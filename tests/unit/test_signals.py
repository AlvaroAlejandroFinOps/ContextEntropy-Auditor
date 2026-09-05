import pytest
from src.context_auditor.models import AuditInput, Message, Document, ToolEvent
from src.context_auditor.signals import extract_deterministic_signals, estimate_tokens

def get_base_input():
    return AuditInput(
        schema_version="1.0.0",
        messages=[
            Message(id="m1", role="system", content="A"*40),
            Message(id="m2", role="user", content="B"*40),
            Message(id="m3", role="assistant", content="C"*40),
            Message(id="m4", role="user", content="D"*40)
        ],
        documents=[],
        tool_events=[]
    )

def test_estimate_tokens():
    assert estimate_tokens("abcd") == 1
    assert estimate_tokens("a" * 400) == 100
    assert estimate_tokens("") == 0

def test_signal_message_counts():
    data = get_base_input()
    signals = extract_deterministic_signals(data)
    assert signals["message_count"] == 4
    assert signals["user_turns"] == 2
    assert signals["assistant_turns"] == 1
    assert signals["messages_since_last_user_turn"] == 0 # The very last message is user

def test_signal_token_estimation():
    data = get_base_input()
    signals = extract_deterministic_signals(data)
    # 4 messages * 40 chars = 160 chars. ~40 tokens.
    assert signals["estimated_tokens"] == 40
    # context_utilization_ratio should be 40 / 128000
    assert signals["context_utilization_ratio"] == round(40 / 128000, 4)

def test_signal_document_duplication():
    data = get_base_input()
    data.documents = [
        Document(id="d1", content="same info", source="docA"),
        Document(id="d2", content="same info", source="docB"),
        Document(id="d3", content="different info", source="docA")
    ]
    signals = extract_deterministic_signals(data)
    assert signals["document_count"] == 3
    assert signals["unique_sources"] == 2
    assert signals["exact_document_duplicates"] == 1

def test_signal_id_integrity():
    data = get_base_input()
    # Introduce duplicate IDs
    data.messages.append(Message(id="m1", role="user", content="test"))
    signals = extract_deterministic_signals(data)
    assert signals["duplicate_ids_found"] == 1

def test_signal_tool_replacement():
    data = get_base_input()
    data.tool_events = [
        ToolEvent(id="t1", tool_name="get_weather", parameters={"loc": "NY"}, result="Rain"),
        ToolEvent(id="t2", tool_name="get_weather", parameters={"loc": "NY"}, result="Sun")
    ]
    signals = extract_deterministic_signals(data)
    assert signals["superseded_tool_results"] == 1

def test_signal_last_objective_recency():
    data = get_base_input()
    # Add assistant messages at the end
    data.messages.append(Message(id="m5", role="assistant", content="Wait"))
    data.messages.append(Message(id="m6", role="assistant", content="Here"))
    signals = extract_deterministic_signals(data)
    # The last user message is m4. Reversed order: m6(0), m5(1), m4(2)
    assert signals["messages_since_last_user_turn"] == 2
