from github import Github, Auth
import os

if __name__ == "__main__":
  token = os.environ['GITHUB_TOKEN']
  if token is None:
    raise ValueError("GITHUB_TOKEN environment variable not set")
  auth = Auth.Token(token)
  github = Github(token)
  repo = github.get_repo("AlphaFinanceLab/infinit-agents-monorepo")
  body = '''
pull request description
'''
  pr = repo.create_pull(base='production', head='main', title='Production', body=body)
  github.close()