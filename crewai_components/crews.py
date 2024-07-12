from crewai import Crew, Process
from crewai_components.agents import planner, writer, editor, github_developer
from crewai_components.tasks import code_tutorial, code_snippets, research_task, plan, write, edit

# Forming the tech-focused crew with some enhanced configurations
crew = Crew(
  agents=[planner, writer, editor, github_developer],
  tasks=[code_tutorial, code_snippets, research_task, plan, write, edit],
  process=Process.sequential,  # Optional: Sequential task execution is default
  memory=True,
  cache=True,
  max_rpm=100,
  share_crew=True
)