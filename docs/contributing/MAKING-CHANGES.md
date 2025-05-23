[How to Write a Git Commit Message]: https://cbea.ms/git-commit/
[interactive rebase]: https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History
[pre-commit]: https://pre-commit.com

[GIT-WORKFLOW.md]: GIT-WORKFLOW.md
[Makefile]: Makefile

<div align="justify">

### Making changes

Create a branch and a Pull Request (PR) following the workflow defined in [GIT-WORKFLOW.md].

**When working on a branch, try to follow this guidelines:**
- Write clear commit messages. See [How to Write a Git Commit Message].
- Use [interactive rebase] to maintain the commit history of your branch clean.
- If you are not using [pre-commit] hooks,
  use the provided [Makefile] commands (`format`, `lint`, `codespell`, `typecheck`)
  as much as possible to maintain code quality. 
- Add unit tests for each piece of code:
  * Avoid connecting to external services during unit tests. Use mocks as needed.
  * Ensure unit tests run as fast as possible.

**When submitting a PR, ensure it meets the following criteria:**
- The PR targets the correct base branch (this depends on the chosen Git workflow).
- The title and body clearly explain **what** the PR does and **why** it’s necessary.
- The body includes a link to the related JIRA ticket,
  facilitating integration between the ticket and the PR.