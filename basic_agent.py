import os

from dotenv import load_dotenv
from swarm import Agent, Swarm

# Load environment variables from .env file
load_dotenv()

# Now you can access environment variables like this:
api_key = os.getenv("OPENAI_API_KEY")


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

# Initialize the Swarm client
client = Swarm()

# Test handoff by asking a math question to the weather agent
messages = [{"role": "user", "content": "What is 2+2?"}]
handoff_response = client.run(agent=weather_agent, messages=messages)
print(handoff_response.messages[-1]["content"])

# Response:
# Handing off to Math Agent
# The answer to 2 + 2 is 4.


messages = [
    {"role": "user", "content": "How is the weather in Canada in December?"},
    {
        "role": "assistant",
        "content": "Canada generally experiences cold weather during December, with varying conditions depending on the region. Coastal areas like Vancouver may have milder temperatures, while areas like Toronto, Ottawa, and Montreal see cooler, snowy conditions. Northern regions experience extreme cold. Checking a reliable weather service will provide the most accurate information.",
    },
]
response = client.run(agent=math_agent, messages=messages)
print(response.messages[-1]["content"])

# Response:
# Handing off to Weather Agent
# Canada generally experiences cold weather during December, with varying conditions depending on the region. Coastal areas like Vancouver may have milder temperatures, while areas like Toronto, Ottawa, and Montreal see cooler, snowy conditions. Northern regions experience extreme cold. Checking a reliable weather service will provide the most accurate information.
