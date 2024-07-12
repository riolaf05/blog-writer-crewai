from crewai_tools import SerperDevTool, GithubSearchTool 
import os

search_tool = SerperDevTool()

# Initialize the tool for semantic searches within a specific GitHub repository
github_tool = GithubSearchTool(
    github_repo=os.getenv('GITHUB_REPO'),
    content_types=['code', 'repo'], # Options: code, repo, pr, issue
)
