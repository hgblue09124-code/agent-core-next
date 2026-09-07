from Execution.Planner import Planner
from Execution.Executor import ActionExecutor
from Execution.Verification import OutcomeVerifier
from Tests.architecture import files_under


def test_three_modules_are_separate():
    planner_files = files_under("Execution", "Planner")
    executor_files = files_under("Execution", "Executor")
    verifier_files = files_under("Execution", "Verification")
    assert planner_files
    assert executor_files
    assert verifier_files
    assert Planner is not None
    assert ActionExecutor is not None
    assert OutcomeVerifier is not None


def test_planner_module_does_not_define_executor():
    text = "\n".join(p.read_text(encoding="utf-8") for p in files_under("Execution", "Planner"))
    assert "class ActionExecutor" not in text
    assert "class OutcomeVerifier" not in text
