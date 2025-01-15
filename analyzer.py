import os
import openai
from github_api import get_repository_data
from utils import find_reused_code, analyze_code_quality

openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_repository(repo_url):
    print(f"Analyzing repository: {repo_url}")
    repo_data = get_repository_data(repo_url)
    reused_code = find_reused_code(repo_data)
    code_quality = analyze_code_quality(repo_data)

    print("Reused Code:")
    print(reused_code)
    print("\nCode Quality Issues:")
    print(code_quality)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Analyze a GitHub repository")
    parser.add_argument("--repo-url", required=True, help="URL of the GitHub repository to analyze")
    args = parser.parse_args()

    analyze_repository(args.repo_url)
