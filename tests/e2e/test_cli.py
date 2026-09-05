import json
import subprocess
import os

def get_base_dir():
    return os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def test_cli_healthy_conversation():
    base_dir = get_base_dir()
    example_path = os.path.join(base_dir, "examples", "healthy-conversation.json")
    
    # Run CLI as a module
    env = os.environ.copy()
    env["PYTHONPATH"] = base_dir
    
    result = subprocess.run(
        ["python", "-m", "src.context_auditor.cli", example_path],
        capture_output=True,
        text=True,
        env=env
    )
    
    # It should succeed
    assert result.returncode == 0
    
    # Output should be valid JSON
    output_json = json.loads(result.stdout)
    
    # Verify schema version and fields
    assert output_json["schema_version"] == "1.0.0"
    assert "audit_id" in output_json
    assert "risk_score" in output_json
    assert output_json["overall_status"] in ["stable", "moderate", "high", "critical"]

def test_cli_invalid_file():
    base_dir = get_base_dir()
    example_path = os.path.join(base_dir, "examples", "non_existent.json")
    
    env = os.environ.copy()
    env["PYTHONPATH"] = base_dir
    
    result = subprocess.run(
        ["python", "-m", "src.context_auditor.cli", example_path],
        capture_output=True,
        text=True,
        env=env
    )
    
    # It should fail
    assert result.returncode == 1
    assert "Error during audit" in result.stderr
