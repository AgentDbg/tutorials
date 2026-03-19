from agents import Agent, Runner, function_tool
import agentdbg
from agentdbg.integrations import openai_agents

@function_tool
def lookup_order(order_id: str) -> str:
    return f"Order {order_id} status: pending. Check again in a moment."

agent = Agent(
    name="support-agent",
    instructions="You help customers check order status. Always use lookup_order. "
                 "Do not stop until you have a definitive status (not 'pending').",
    tools=[lookup_order],
)

@agentdbg.trace(
    name="order-loop-demo",
    stop_on_loop=True,
    stop_on_loop_min_repetitions=3,
    max_events=20,

)
def run():
    result = Runner.run_sync(agent, "What's the status of order 12345?")
    return result

run()
