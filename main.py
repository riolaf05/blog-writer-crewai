import os
os.environ["GITHUB_REPO"] = "https://github.com/riolaf05/langchain-crewai-agent"
os.environ["TOPIC"] = "Agents with CrewAI and Langchain"

from crewai_tools.crews import crew
from dotenv import load_dotenv
load_dotenv(override=True)

# Starting the task execution process with enhanced feedback
result = crew.kickoff(inputs={'topic': os.getenv["TOPIC"]})
print(result)