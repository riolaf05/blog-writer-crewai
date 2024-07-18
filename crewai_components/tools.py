from crewai_tools import SerperDevTool, GithubSearchTool 
import os
from dotenv import load_dotenv
load_dotenv(override=True)

search_tool = SerperDevTool()

# Initialize the tool for semantic searches within a specific GitHub repository
# https://docs.crewai.com/tools/GitHubSearchTool/?h=github#custom-model-and-embeddings
github_tools = GithubSearchTool(
    github_repo=os.getenv('GITHUB_REPO'),
    gh_token=os.getenv('GITHUB_TOKEN'),
    content_types=['code'], # Options: code, repo, pr, issue
)
