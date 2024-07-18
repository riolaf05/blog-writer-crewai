import os
os.environ["GITHUB_REPO"] = "https://github.com/riolaf05/langchain-crewai-agent"
os.environ["TOPIC"] = "Agents with CrewAI and Langchain"
from crewai_components.crews import crew
from dotenv import load_dotenv
load_dotenv(override=True)

# Starting the task execution process with enhanced feedback
inputs = {"topic":"Comparative study of LangGraph, Autogen and Crewai for building multi-agent system."}
result = crew.kickoff(inputs=inputs)
print(result)