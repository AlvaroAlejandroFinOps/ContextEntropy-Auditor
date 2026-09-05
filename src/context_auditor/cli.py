import argparse
import json
import sys
from src.context_auditor.auditor import ContextAuditor
from src.context_auditor.adapters.gemini import GeminiAdapter
from src.context_auditor.policies import PolicyMode

def main():
    parser = argparse.ArgumentParser(description="Context Entropy Auditor (CEA) CLI")
    parser.add_argument("input_file", help="Path to the JSON input file matching audit-input.schema.json")
    parser.add_argument("--policy", choices=[m.value for m in PolicyMode], default=PolicyMode.RECOMMEND.value, help="Policy mode for recommendations")
    parser.add_argument("--factual", action="store_true", help="Set to true if the task requires factual claims (stricter evidence checks)")
    
    args = parser.parse_args()

    try:
        with open(args.input_file, "r", encoding="utf-8") as f:
            raw_input = json.load(f)
            
        adapter = GeminiAdapter()
        auditor = ContextAuditor(llm_adapter=adapter, policy_mode=PolicyMode(args.policy))
        
        result = auditor.audit(raw_input, task_requires_factual=args.factual)
        
        # Print valid JSON to stdout
        print(json.dumps(result.model_dump(), indent=2))
        
    except Exception as e:
        print(f"Error during audit: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
