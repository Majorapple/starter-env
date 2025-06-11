class BaseAgent:
    """Base agent with simple run interface."""

    def __init__(self, name):
        self.name = name

    def run(self, task_description, context=None):
        """Placeholder run method. Replace with actual LLM API calls."""
        prompt = f"Agent {self.name} received task: {task_description}\nContext: {context}"
        # TODO: integrate with actual LLM API
        response = f"[Simulated response from {self.name}]"
        return response


class DeveloperAgent(BaseAgent):
    """Generates code or implementation details for a given task."""


class ReviewerAgent(BaseAgent):
    """Reviews code produced by the developer agent."""


class QAAgent(BaseAgent):
    """Runs tests and validates the code."""


class IntegratorAgent(BaseAgent):
    """Integrates approved code into the project."""


def multi_agent_workflow(task):
    """Demonstrates a simple pipeline where agents verify each other's work."""
    developer = DeveloperAgent("Developer")
    reviewer = ReviewerAgent("Reviewer")
    qa_agent = QAAgent("QA")
    integrator = IntegratorAgent("Integrator")

    dev_output = developer.run(task)
    review_output = reviewer.run("Review the developer's work", context=dev_output)
    qa_output = qa_agent.run("Test the reviewed code", context=review_output)
    integration_output = integrator.run("Integrate code if QA passes", context=qa_output)

    return {
        "developer": dev_output,
        "review": review_output,
        "qa": qa_output,
        "integrator": integration_output,
    }


if __name__ == "__main__":
    result = multi_agent_workflow("Build a landing page")
    for role, output in result.items():
        print(f"{role.capitalize()} output: {output}")
