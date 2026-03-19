from langmem import create_memory_manager
from langmem.knowledge.extraction import ExtractedMemory, Memory
import asyncio

from agentdbg import trace  # To wrap the async function
from agentdbg.integrations import AgentDbgLangChainCallbackHandler  # To handle errors

manager = create_memory_manager(
    "openai:gpt-5-chat",
    enable_deletes=True
)

conversation = [
    {"role": "user", "content": "Hi"},
    {"role": "assistant", "content": "Hello! How can I assist you today?"},
]

@trace(
    name="LangMem Run",
    stop_on_loop=True,
    stop_on_loop_min_repetitions=3,
    max_duration_s=10,
    max_events=20,
)
async def test():
    handler = AgentDbgLangChainCallbackHandler()
    config = {"callbacks": [handler]}
    # Extract memories from conversation

    memories = await manager.ainvoke({
        "messages": conversation,
        "existing": [
            ExtractedMemory(id='e8ef6ca4-0159-4844-8c22-32cdbf87f260', content=Memory(content='User likes to receive notifications in the morning.')),
            ExtractedMemory(id='2e469b7d-58bd-4575-9049-a395633cf20d', content=Memory(content='User has a preference for dark mode in all their apps.'))
        ],
        "max_steps": 1
    }, config=config)

    for memory in memories:
        print(memory)

if __name__ == "__main__":
    asyncio.run(test())
