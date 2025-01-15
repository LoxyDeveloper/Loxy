from github import Github

def get_repository_data(repo_url):
    token = "YOUR_GITHUB_TOKEN"  # Replace with your GitHub token
    github = Github(token)
    repo_name = repo_url.split("github.com/")[-1]
    repo = github.get_repo(repo_name)

    files = []
    for content in repo.get_contents(""):
        files.append({
            "path": content.path,
            "content": content.decoded_content.decode("utf-8") if content.type == "file" else None,
        })

    return files
