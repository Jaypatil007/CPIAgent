# CPIAgent
# Git Basics: Essential Commands & Usage Guide

This README provides a concise guide to basic Git commands, their purposes, and examples for each. It also covers common scenarios such as adding/removing remotes, handling push/pull errors, and best practices for working with a remote repository.

---

## Table of Contents

- [Initializing a Repository](#initializing-a-repository)
- [Cloning a Repository](#cloning-a-repository)
- [Checking Status](#checking-status)
- [Staging Changes](#staging-changes)
- [Committing Changes](#committing-changes)
- [Adding a Remote Repository](#adding-a-remote-repository)
- [Pushing Changes](#pushing-changes)
- [Pulling Changes](#pulling-changes)
- [Merging Branches](#merging-branches)
- [Creating Pull Requests](#creating-pull-requests)
- [Fetching Changes](#fetching-changes)
- [Removing a Remote Repository](#removing-a-remote-repository)
- [Sparse Checkout (Clone Only a Folder)](#sparse-checkout-clone-only-a-folder)
- [Handling Push Errors](#handling-push-errors)
- [Best Practices](#best-practices)

---

## Initializing a Repository

Initialize a new Git repository in your current directory:

```bash
git init
```

---

## Cloning a Repository

Clone a remote repository to your local machine:

```bash
git clone <remote-url>
# Example
git clone https://github.com/Jaypatil007/myproject.git
```

---

## Checking Status

See the current state of your working directory and staging area:

```bash
git status
```

---

## Staging Changes

Stage files for commit:

```bash
git add filename.txt      # Add a specific file
git add .                 # Add all files in the directory
```

---

## Committing Changes

Commit staged changes to your local repository:

```bash
git commit -m "Your commit message"
```

---

## Adding a Remote Repository

Link your local repository to a remote (e.g., GitHub):

```bash
git remote add origin <remote-url>
# Example
git remote add origin https://github.com/Jaypatil007/new-repo.git
```

Verify remotes:

```bash
git remote -v
```

---

## Pushing Changes

Push your committed changes to the remote repository:

```bash
git push -u origin main
```

---

## Pulling Changes

Fetch and merge changes from the remote repository:

```bash
git pull origin main
```

> **Note:** If your branches have diverged, Git will prompt you to specify how to reconcile:
>
> - Merge (default):  
>   `git pull --no-rebase origin main`
> - Rebase:  
>   `git pull --rebase origin main`
> - Fast-forward only:  
>   `git pull --ff-only origin main`
>
> Set your default preference globally:
> ```bash
> git config --global pull.rebase false  # for merge
> git config --global pull.rebase true   # for rebase
> git config --global pull.ff only       # for fast-forward only
> ```

---

## Merging Branches

Integrate changes from one branch into another.

First, ensure you are on the branch you want to merge into (e.g., `main`):
```bash
git checkout main
```

Then, merge the desired branch (e.g., `feature-branch`) into your current branch:
```bash
git merge feature-branch
```

If conflicts occur, you'll need to resolve them manually, then `git add` the resolved files and `git commit` to finalize the merge.

---

## Creating Pull Requests

A Pull Request (PR) is a way to propose changes and have them reviewed before merging into a main branch on platforms like GitHub.

1. **Push your feature branch to the remote:**
   ```bash
   git push origin feature-branch
   ```

2. **Go to your GitHub repository:**
   * GitHub will usually detect the newly pushed branch and prompt you to create a Pull Request.
   * If not, navigate to the "Pull requests" tab and click "New pull request".

3. **Select the branches:** Choose your `feature-branch` as the `compare` branch and the target branch (e.g., `main`) as the `base` branch.

4. **Add a title and description:** Clearly explain the changes you've made and why.

5. **Create the Pull Request:** Click "Create pull request".

6. **Review and Merge:** Others can review your code, suggest changes, and once approved, the PR can be merged into the base branch.

---

## Fetching Changes

Download changes from the remote repository without merging:

```bash
git fetch origin
```

---

## Removing a Remote Repository

Remove a remote from your local repository:

```bash
git remote remove origin
# Or
git remote rm origin
```

---

## Sparse Checkout (Clone Only a Folder)

Git does not support cloning a specific folder directly, but you can use sparse checkout:

```bash
git clone --no-checkout <repo-url>
cd <repo-name>
git sparse-checkout init
git sparse-checkout set <folder-path>
git checkout
```
Example for folder `docs`:
```bash
git clone --no-checkout https://github.com/Jaypatil007/repo.git
cd repo
git sparse-checkout init
git sparse-checkout set docs
git checkout
```

---

## Handling Push Errors

If you get an error like:
```
! [rejected] main -> main (fetch first)
error: failed to push some refs to ...
```
This means the remote repo has changes your local branch doesn't have.

**Solution:**
1. Pull and merge remote changes:
    ```bash
    git pull origin main
    ```
2. Resolve any merge conflicts, commit, then push again:
    ```bash
    git push origin main
    ```
3. **If you want to overwrite the remote branch** (dangerous; will delete remote changes):
    ```bash
    git push --force origin main
    ```

---

## Best Practices

- **.gitignore:** Exclude files/folders you don’t want in the repo.
- **Commit messages:** Use clear, descriptive messages.
- **Check remotes:** Run `git remote -v` before pushing/pulling.
- **Branch naming:** Use meaningful names (`main`, `feature/login`, etc.).
- **Push regularly:** Keep your remote repo updated.
- **Secure your repo:** Never push sensitive data.
- **Review before push:** Use `git status` and `git log` to review changes.

---

## Quick Reference Table

| Command                        | Purpose/Usage                                      |
|---------------------------------|----------------------------------------------------|
| `git init`                      | Initialize a new repo                              |
| `git clone <url>`               | Clone repo from remote                             |
| `git status`                    | Show working directory status                      |
| `git add .`                     | Stage all changes                                 |
| `git commit -m "msg"`           | Commit staged changes                              |
| `git remote add origin <url>`   | Add remote repo                                    |
| `git push -u origin main`       | Push local branch to remote                        |
| `git pull origin main`          | Fetch & merge remote changes                       |
| `git merge <branch>`            | Merge changes from one branch into another         |
| `git fetch origin`              | Fetch remote changes without merging               |
| `git remote remove origin`      | Remove remote repo                                 |
| Sparse checkout                 | Clone only part of the repo (see section above)    |

---

## Need Help?

For more details on any command, use `git help <command>` or visit the [Git documentation](https://git-scm.com/doc).
