# GHA-test

This repo is to test some GHA workflows.

## 1. Create files upon "push" and writes to the same repo

Steps:
- Create a workflow file
- Create a token that has push permission to the repo (currently using account-scoped token)
- Save the token in the repo secrets (Settings > Secrets and Variables > Actions > New repository secret)
- Use the secret in the workflow yaml to realize "git push"