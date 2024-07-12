import os
os.environ["GITHUB_REPO"] = "https://github.com/riolaf05/langchain-fastapi-rag-platform.git"
os.environ["TOPIC"] = "Agents with Langchain and FastAPI"

from crewai_components.crews import crew
from dotenv import load_dotenv
load_dotenv(override=True)

# Starting the task execution process with enhanced feedback
result = crew.kickoff(inputs={'topic': os.getenv["TOPIC"]})
print(result)