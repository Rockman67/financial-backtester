import subprocess, sys, pathlib
sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))

def test_cli_help():
    completed = subprocess.run(
        [sys.executable, "load_data.py", "--help"],
        capture_output=True, text=True
    )
    assert completed.returncode == 0
    assert "parse" in completed.stdout and "all" in completed.stdout
