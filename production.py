from github import Github, Auth
import os
import json

if __name__ == "__main__":
  token = os.environ['GITHUB_TOKEN']
  if token is None:
    raise ValueError("GITHUB_TOKEN environment variable not set")
  auth = Auth.Token(token)
  github = Github(token)
  repo = github.get_repo("tepzilon/test-release-please")

  main_manifest = None
  with open(".release-please-manifest.json", "r") as f:
    main_manifest = json.load(f)
  
  prod_manifest = None
  c = repo.get_contents(".release-please-manifest.json", ref="production")

  c.content

  body = '''
pull request description
'''
  pr = repo.create_pull(base='production', head='main', title='Production', body=body)
  github.close()