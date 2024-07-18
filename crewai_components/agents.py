from crewai import Agent, Task, Crew, Process
from dotenv import load_dotenv
# from crewai_components.tools import github_tools, search_tool
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
load_dotenv(override=True)

llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2
)

#define agents

# researcher = Agent(
#   role='Senior Researcher',
#   goal='Uncover groundbreaking technologies in {topic}',
#   verbose=True,
#   memory=True,
#   backstory=(
#     "Driven by curiosity, you're at the forefront of"
#     "innovation, eager to explore and share knowledge that could change"
#     "the world."
#   ),
#   tools=[search_tool],
#   allow_delegation=True
# )

planner = Agent(
    role="Content Planner",
    goal="Plan engaging and factually accurate content on {topic}",
    backstory="You're working on planning a blog article "
              "about the topic: {topic} in 'https://medium.com/'."
              "You collect information that helps the "
              "audience learn something "
              "and make informed decisions. "
              "You have to prepare a detailed "
              "outline and the relevant topics and sub-topics that has to be a part of the"
              "blogpost."
              "Your work is the basis for "
              "the Content Writer to write an article on this topic.",
    llm=llm,
    allow_delegation=False,
    verbose=True
)

writer = Agent(
    role="Content Writer",
    goal="Write insightful and factually accurate "
         "opinion piece about the topic: {topic}",
    backstory="You're working on a writing "
              "a new opinion piece about the topic: {topic} in 'https://medium.com/'. "
              "You base your writing on the work of "
              "the Content Planner, who provides an outline "
              "and relevant context about the topic. "
              "You follow the main objectives and "
              "direction of the outline, "
              "as provide by the Content Planner. "
              "You also provide objective and impartial insights "
              "and back them up with information "
              "provide by the Content Planner. "
              "You acknowledge in your opinion piece "
              "when your statements are opinions "
              "as opposed to objective statements.",
    allow_delegation=False,
    llm=llm,
    verbose=True
)

# github_developer = Agent(
#     role="Code Snippet Seeker",
#     goal="Understand the code inside a GitHub repo and extract useful snippet of code.",
#     backstory="You are Code Snippet Seeker, an AI agent created to bridge conceptual"
#               "knowledge and practical implementation. Born from a sophisticated neural"
#               "network, your mission is to find precise code snippets corresponding to"
#               "section titles provided by Content Planner."

#               "Content Planner structures articles on technical topics, and when a"
#               "section is ready, you take over. You dive into the given GitHub repository,"
#               "locating the exact lines of code that match the given section titles."

#               "With your understanding of context, programming languages, and coding"
#               "conventions, you ensure articles are both theoretically sound and"
#               "practically grounded. You are an invaluable asset, maintaining the bridge"
#               "between high-level concepts and real-world coding practices, and your"
#               "skills evolve through continuous learning.",
#     tools=[github_tools],
#     allow_delegation=False,
#     verbose=True
# )

editor = Agent(
    role="Editor",
    goal="Edit a given blog post to align with "
         "the writing style of the organization 'https://medium.com/'. ",
    backstory="You are an editor who receives a blog post "
              "from the Content Writer. "
              "Your goal is to review the blog post "
              "to ensure that it follows journalistic best practices,"
              "provides balanced viewpoints "
              "when providing opinions or assertions, "
              "and also avoids major controversial topics "
              "or opinions when possible.",
    llm=llm,
    allow_delegation=False,
    verbose=True
)
