from crewai import Task
from crewai_components.agents import researcher, writer, planner, github_developer, editor
from crewai_components.tools import TurnOnEC2
from crewai_components import SerperDevTool
from dotenv import load_dotenv
load_dotenv(override=True)

search_tool = SerperDevTool()
turn_on_ec2_tool = TurnOnEC2()


#Tasks 

code_tutorial = Task(
    description=(
        "1. Take a look at the README file on the code \n"
        "2. Identify the list of step for the setup of the project \n"
        "3. Analyze the code's and find the snippets or cli command of code related to each of the above mentioned code \n"
    ),
    expected_output="A comprehensive code snippet or cli command for each the points of the tutorial.",
    agent=github_developer
)

code_snippets = Task(
    description=(
        "1. Take a look at the entire code \n"
        "2. Identify the list of main step for the implementation \n"
        "3. Analyze the code's and find the snippets that represents each step of implementation of the previous point. \n"
    ),
    expected_output="A comprehensive code snippets list for each step of implementation.",
    agent=github_developer
)

research_task = Task(
  description=(
    "Identify all the useful information about the use case {topic}."
    "Focus on identifying the current state of art."
    "Your final report should clearly articulate the key points,"
    "the techniques and technologies used for the implementation,"
    "the tools that are involved (language of programming, cloud vendors, etc.),"
    "the market opportunities, and potential risks."
  ),
  expected_output='A comprehensive long paragraph that report state of art for the given use case.',
  tools=[search_tool],
  agent=researcher,
)

plan = Task(
    description=(
        "1. Examine all the, technologies, techniques, "
            "tools, code snippets used for the implementation "
            "and noteworthy news on the use case {topic}.\n"
        "2. Develop a detailed content outline including "
            "an introduction, setup, code explanation, possible applications, conclusion.\n"
        "3. Include SEO keywords and relevant data or sources."
    ),
    expected_output="A comprehensive content plan document "
        "with an outline, audience analysis, "
        "SEO keywords, and resources.",
    agent=planner,
)

write = Task(
    description=(
        "1. Use the content plan to craft a compelling "
            "blog post on {topic}.\n"
        "2. Incorporate code snippets and cli commands in the setup and code explanation paragraphs. \n"
        "3. Incorporate SEO keywords naturally.\n"
        "4. Sections/Subtitles are properly named "
            "in an engaging manner.\n"
        "5. Ensure the post is structured with an "
            "engaging introduction, insightful body, "
            "and a summarizing conclusion.\n"
        "6. Proofread for grammatical errors and "
            "alignment with the brand's voice.\n"
    ),
    expected_output="A well-written blog post "
        "in markdown format, ready for publication, "
        "each section should have as many paragraphs are needed according to the list of extracted snippets and the information retrieved.",
    agent=writer,
)

edit = Task(
    description=("Proofread the given blog post for "
                 "grammatical errors and "
                 "alignment with the brand's voice."),
    expected_output="A well-written blog post in markdown format, "
                    "ready for publication, "
                    "each section should have as many paragraphs are needed according to the list of extracted snippets and the information retrieved.",
    agent=editor
)
