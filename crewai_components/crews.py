from crewai import Crew, Process
from crewai_components.agents import planner, writer, editor
from crewai_components.tasks import plan, write, edit

# Forming the tech-focused crew with some enhanced configurations
crew = Crew(
    agents=[planner, writer, editor],
    tasks=[plan, write, edit],
    verbose=2
)