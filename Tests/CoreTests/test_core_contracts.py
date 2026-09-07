from Core.Contracts import Action, Capability, ExecutionResult, ExecutionStatus
from Core.Agent import Agent
from Core.Runtime import AgentRuntime


def test_contracts_exist():
    action = Action(name="echo", capability_id="mock.echo")
    cap = Capability(id="mock.echo", name="Echo")
    result = ExecutionResult(status=ExecutionStatus.NOT_EXECUTED)
    assert action.name == "echo"
    assert cap.id == "mock.echo"
    assert result.status is ExecutionStatus.NOT_EXECUTED


def test_agent_and_runtime_are_protocols():
    assert getattr(Agent, "_is_protocol", True)
    assert getattr(AgentRuntime, "_is_protocol", True)
