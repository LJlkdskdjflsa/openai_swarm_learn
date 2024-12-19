import os

from dotenv import load_dotenv
from swarm import Agent, Swarm

# Load environment variables from .env file
load_dotenv()

# Now you can access environment variables like this:
api_key = os.getenv("OPENAI_API_KEY")

print(api_key)


# creating handoffs functions
def handoff_to_weather_agent():
    """Transfer to the weather agent for weather queries."""
    print("Handing off to Weather Agent")
    return weather_agent


def handoff_to_math_agent():
    """Transfer to the math agent for mathematical queries."""
    print("Handing off to Math Agent")
    return math_agent


# Initialize the agents with specific roles
math_agent = Agent(
    name="Math Agent",
    instructions="You handle only mathematical queries.",
    functions=[handoff_to_weather_agent],
)

weather_agent = Agent(
    name="Weather Agent",
    instructions="You handle only weather-related queries.",
    functions=[handoff_to_math_agent],
)
