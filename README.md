# Starter Environment

This repository contains a minimal example demonstrating how to orchestrate multiple AI agents that work together to build and verify software. The main entry point is `agents.py`.

## Files

- `agents.py` – Implements simple agent classes (`DeveloperAgent`, `ReviewerAgent`, `QAAgent`, and `IntegratorAgent`) and a `multi_agent_workflow` function that shows how they interact.

## Running the demo

Run the script directly to see a simulated workflow:

```bash
python agents.py
```

Each agent produces a placeholder response. You can replace the implementation of `BaseAgent.run()` with calls to your preferred LLM API (for example, `openai.ChatCompletion.create`).
