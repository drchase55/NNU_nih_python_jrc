# Tutorial 4: GitHub For YOUR purposes
----------------------------------------------------------

## Overview

## Learning Objectives
By the end of this lesson, you will be able to:

- Define FAIR data practices
- Understand the purpose of git tools
- Create a GitHub account
- Set up Git on your local computer
- Create your first repository
- Push code to GitHub

# FAIR Data principles

You may already have seen that the NIH requires researchers to share their data in ways that make it FAIR to maximize its value. Ensuring data is well-documented, openly available, and in standardized formats not only enhances transparency and collaboration but also aligns with NIH’s commitment to advancing scientific discovery.

The FAIR data principles are:

- Findable: Data should be assigned unique identifiers (e.g., DOIs) and be discoverable through metadata and search engines.
- Accessible: Data should be retrievable through standardized protocols, with clear terms on access (open or restricted).
- Interoperable: Data should use standardized formats and vocabularies to enable integration with other datasets.
- Reusable: Data should be well-documented with clear licensing to support reuse and replication in different contexts.




### Step 1: Creating a GitHub Account

Before you can start using GitHub for your materials, you need to create an account. GitHub is a platform that allows you to store, share, and collaborate on code. It is widely used by developers, students, and organizations for managing software projects using Git, a version control system that tracks changes in your code.

To get started, you need to sign up for a free GitHub account. This will give you access to your own profile, repositories, and collaboration tools. Follow the steps below to create your GitHub account.

- Go to GitHub's website
- Click on Sign up in the top-right corner.
- Enter your email address, username, and password.
- Click Create an account and follow the instructions.
- GitHub will send a verification email. Click the link in the email to verify your account.

## Step 2: Setting Up Git on Your Local Computer
While GitHub is an online platform for hosting code, Git is the tool that allows you to track and manage changes in your projects. Git is a version control system that records changes to files, allowing multiple people to work on the same project without conflicts.

Before you can push code or other files to GitHub, you need to install **Git** on your computer. This will allow you to work with your projects locally and sync them with GitHub. The installation process depends on your operating system.

### Instructions for Windows
- Download Git for Windows from git-scm.com.
- Run the installer and follow the default settings.

### Instructions for Mac
- Open the Terminal and type:

    git --version

- If Git is not installed, install it using:

   brew install git

(You may need to install Homebrew first.)

### For Linux (Ubuntu/Debian-based):
Open the Terminal and run:

    sudo apt update
    sudo apt install git

Once installed, verify the installation by running:

     git --version


## Step 3: Configuring Git with Your GitHub Account
Once Git is installed, you need to configure it with your name and email. This helps Git track your changes and associate them with your GitHub account. Every time you make changes to a file, Git will store your name and email in the history log, allowing you and others to see who made each update.

Setting up Git properly ensures a smooth workflow when pushing your code to GitHub. Let’s configure Git with your identity.

## Step 4: Creating Your First GitHub Repository
A repository (repo) is where your project files are stored on GitHub. It acts like a folder where you can save, track, and collaborate on code. You can create repositories for personal projects, class assignments, or team-based development.

Repositories can be public (anyone can see them) or private (only you and selected people can view them). To get started, you will create your first repository directly on GitHub.

### Instructions:
- Go to your GitHub homepage.
- Click on the + icon (top right) and select New repository.
- Enter a repository name (e.g., my-first-repo).
- Choose Public or Private.
- Check the box for Initialize this repository with a README (optional).
- Click Create repository.

## Step 5: Connecting Your Local Project to GitHub
Now that you have a repository on GitHub, it’s time to connect it with a local project on your computer. This allows you to write code on your machine and sync it with GitHub. You will use Git commands to initialize, commit, and push your project to GitHub.

This step is essential if you want to store your code in GitHub or collaborate with others. Let’s walk through the process.

### Instructions:
- Open the Terminal (or Git Bash).
- Navigate to the folder where you want to create your project:

## Conclusion
Now that you have GitHub set up, you can explore more advanced features:
✅ Learn basic Git commands (git status, git pull, git branch).
✅ Use GitHub Desktop if you prefer a graphical interface.
✅ Try GitHub Actions for automation.

Go to the [next tutorial](Submodule_0_Tutorial_6_UsingGit.md)