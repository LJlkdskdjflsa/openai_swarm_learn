# OpenAI Agent Swarm

A Python implementation that orchestrates multiple OpenAI Assistants in a swarm configuration, enabling collaborative problem-solving and distributed task execution.

## Description

This project leverages OpenAI's Assistant API to create a swarm of AI agents that can work together, communicate, and solve complex tasks collaboratively. Each agent in the swarm can have specialized roles while maintaining the ability to coordinate and share information with other agents in the network.

## Features

- Multi-agent system using OpenAI's Assistant API
- Agent-to-agent communication and coordination
- Dynamic task distribution and delegation
- Specialized agent roles and capabilities
- Concurrent task execution
- Emergent problem-solving through agent collaboration

## Prerequisites

- Python 3.8x
- [Poetry](https://python-poetry.org/docs/#installation) for dependency management
- OpenAI API key (with access to Assistants API)

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/openai_swarm_learn.git
cd openai_swarm_learn

# Install dependencies using Poetry
poetry install

# Activate the Poetry virtual environment
poetry shell
```

## Configuration

1. Create a `.env` file in the project root
2. Add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## Usage

[Detailed usage instructions and examples will be added as the project develops]

## Architecture

The swarm consists of multiple AI agents, each powered by OpenAI's Assistant API. The agents can:
- Communicate with each other
- Share tasks and information
- Work on problems collaboratively
- Specialize in different aspects of problem-solving

## Development

```bash
# Install development dependencies
poetry install --with dev

# Run tests
poetry run pytest

# Format code
poetry run black .
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License

## Contact

