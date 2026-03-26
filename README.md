# AgentDbg Tutorials

Interactive Jupyter notebooks for learning how to trace and debug AI agents with AgentDbg. All notebooks run without API keys or network calls — they use deterministic stubs and fake models.

## Notebooks

### 1. Stop a Runaway Agent (`Guardrails/`)

**File:** `Guardrails/Stop a Runaway Agent.ipynb`
**Install:** `pip install agentdbg`

A minimal introduction using only the core AgentDbg SDK — no framework dependencies. Builds a tiny local agent that loops on the same tool call and model call, then shows how to:

- Observe a `LOOP_WARNING` in the timeline without stopping the run
- Enable `stop_on_loop` to abort execution as soon as the pattern repeats
- Compare the two runs side by side in `agentdbg view`

Good starting point if you want to understand guardrails before looking at framework integrations.

---

### 2. Debug a LangGraph Agent (`LangChain/`)

**File:** `LangChain/Mock LangGraph Agent.ipynb`
**Install:** `pip install "agentdbg[langchain]"`

Builds a multi-node LangGraph graph (search → calculate → save) using `FakeListLLM` and deterministic `@tool` functions. Covers:

- Adding `AgentDbgLangChainCallbackHandler` to a LangGraph run
- The happy-path trace (RUN_START → LLM_CALL → TOOL_CALL × 3 → RUN_END)
- A looping agent that triggers `LOOP_WARNING`
- Using `stop_on_loop` to abort the graph mid-execution

---

### 3. Debug an OpenAI Agents Workflow (`OpenAI/`)

**File:** `OpenAI/Mock OpenAI Agent.ipynb`
**Install:** `pip install "agentdbg[openai]" openai-agents`

Uses the OpenAI Agents SDK tracing API (`generation_span`, `function_span`) with deterministic inputs to drive the same quarterly-sales workflow without hitting any real model endpoint. Covers:

- Registering `AgentDbgOpenAIAgentsTracingProcessor` via `set_trace_processors`
- How `generation_span` → `LLM_CALL` and `function_span` → `TOOL_CALL` translation works
- The looping pattern and `LOOP_WARNING`
- The key difference from LangChain: the SDK swallows exceptions from tracing processors, so you must poll `PROCESSOR.abort_exception` inside your loop and call `PROCESSOR.raise_if_aborted()` after

---

## Running the notebooks

```bash
# From the repo root — install AgentDbg and Jupyter
uv pip install agentdbg jupyter

# For LangChain notebook
uv pip install "agentdbg[langchain]"

# For OpenAI Agents notebook
uv pip install "agentdbg[openai]" openai-agents

# Start Jupyter
jupyter notebook
```

Open the notebook of your choice and run all cells in order. After each run, start the viewer in a terminal:

```bash
agentdbg view
```
