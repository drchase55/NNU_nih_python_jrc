# Tutorial 6: Managing your GitHub data repositories
---------------------------------------------------------------

## Overview


## Learning Objectives



--------------------------------------------------------------
## Why use Git for your research lab team *DATA?*
In a research lab environment, managing data properly is just as important as collecting it. Labs often deal with long-term datasets, changing protocols, and *multiple* contributors, which can lead to data integrity issues if not properly managed.

🧪 GitHub Repo Management Guide for Science Lab PIs

🎯 Goal:
As the lab PI or project manager, you want to:

- Ensure collaborators don’t accidentally overwrite important files.
- Control when changes are added to the main dataset/code.
- Require collaborators to submit changes for review before those changes are finalized.
- Protect your team’s research integrity and maintain FAIR data practices.

GitHub makes this possible with a system of branch protection and pull requests—and you can manage it all through a point-and-click interface (no coding required).

## Key Concepts (Plain Language)
🔹 What is a “commit”?
A commit is like saving a version of your file with a note attached—"I added this graph," "I fixed a typo," etc. Every team member commits their own changes as they work.

🔹 What is “push” vs. “pull”?
Push: Upload your saved changes to GitHub (shared with the team).

Pull: Download the latest team updates from GitHub to your computer.

🔹 What is the “main” branch?
Think of the main branch as the “official” version of the project or dataset. You want to keep it clean and stable—like a published paper.

## Why You Should Protect the “Main” Branch
Without protection 🔒:
- A student or collaborator might accidentally delete or overwrite key data.
- Anyone could push changes at any time—even if they weren’t reviewed.
- There’s no record of who approved changes or when.

With protection:
- Collaborators must submit proposed changes (like peer review).
- You (or a designated reviewer) can approve or deny changes before they go public.
- The main branch stays clean, traceable, and trustworthy.

## Step-by-Step: Set Up GitHub to Control When Collaborators Can Commit
✅ 1. Log into GitHub and Open Your Repository
Go to github.com and click on the repository you want to manage.

✅ 2. Go to Settings
Click the “Settings” tab at the top of the repo.

In the left sidebar, scroll down and click “Branches”.

✅ 3. Add a Branch Protection Rule
This sets the rules for your "main" branch.

On the "Branches" page:
Click “Add rule”.

In Branch name pattern, type:

main      (or master, depending on your repo)

**Check the following boxes:**

✅ Require pull request reviews before merging
(This forces team members to submit changes for your approval)

✅ Require status checks to pass
(Optional: useful if you’re using automated testing or data validation scripts)

✅ Require branches to be up to date
(Ensures everyone works from the latest version)

✅ Restrict who can push to matching branches
(You can list yourself or other senior members who are allowed to approve changes)

Click Create or Save changes.

👥 What This Looks Like for Your Collaborators
Now, your students and research assistants won’t be able to push changes directly to the official version. Instead, they will:

- Create a new branch (a personal workspace).
- Add or update files.
- Use GitHub Desktop or GitHub.com to create a pull request (PR).

You (or a trusted reviewer) will get a notification.

You can review the changes, leave comments, and then click “Merge” to accept them.

🧠 Think of a Pull Request like a manuscript submission—it gets reviewed before being added to the “published” record.

## Summary: What You’re Gaining

As the lab PI, you now have:

|🔒 Protection From	|✅ Tools You Now Have|
|:--------------------:|:----------------------:|
|Accidental data loss|	Branch protection rules|
|Unreviewed changes|	Pull requests (PRs)|
|Unclear authorship	|Contributor tracking|
|Unapproved protocol changes|	Review workflows|

## Conclusion

You should now be able to use Github and the underlying tool of Git to keep track of and protect your data. However, it is not yet FAIR data because you need a fixed identifier for a set of data (even if you later update it) to inlcude with your journal articles. 

For that information, view the [last tutorial on Git](Submodule_0_Tutorial_6_DOI.md) in this submodule.

