# Digit Classification
This is a 1st semester project at UTEC, it classifies a written digit. It uses the Digit DataSet from Scikit-Learn.</p>
## Installation
1. Clone the project
2. Create a virtual environment in the root directory with:
    >python -m venv env
3. Activate the virtual environment:
    >env\Scripts\activate</p>
    In case it doesn't work:</p>
    - Open PowerShell as administrator</p>
    - And copy the following line (give ‘Y’ to everything):</p>
        >Set-ExecutionPolicy RemoteSigned -Scope CurrentUser</p>
    - Try again to activate the virtual environment.
4. Install the dependencies with:
    >pip install -r requirements.txt
## Main commands to navigate Git Bash:
- Start the local repository.
    > git init
- Change the address of the folder/directory you are in.
    > cd <‘name of the directory/folder to move’>
- Changes to the previous folder/directory address.
    >cd ...
- Check the status of the local repository.
    >git status
- Start tracking files.
    >git add <‘filename’>
- Make a screenshot or a save of what has been done so far.
    >git commit -m ‘descriptive message about what's been done’   
- Push the changes to GitHub(care)‼️‼️.
    >git push origin <‘name of your branch’>
- Get changes from GitHub.
    >git pull origin <‘name of branch’>
- Create new branch.
    >git branch <‘name of the branch’>
- Move between branches.
    >git checkout <‘name of branch’>
- List of existing branches.
    >git branch
- Merge branches with the current branch.
    >git merge <‘name of branch to be merged’>
- Fetch all branches from the remote repository.
    >git fetch
- Remove local branch.
    >git branch -d <‘name of branch to remove’>
- Remove a branch from GitHub(care)‼️‼️.
    >git push origin --delete <‘name of the branch’>
- Show commit history:
    >git log
- Show the differences between commits:
    >git diff
- When you want to deactivate the virtual environment:
    >deactivate
- When you want to add more dependencies to the (requirements.txt)
    >pip freeze > requirements.txt
## Workflow 
- Once the installation of the project and its dependencies are ready, you will start modifying/creating the files you consider necessary to carry out the part you have been assigned.
    - When you have what you need, upload it to GitHub so that others can view it, make suggestions, or continue with the project. But you will upload only the branch with your name (>git push origin <‘branch name’>) so that it doesn't interfere with the final product.
    - When you want to get the changes from the other branches either because you need them to continue the project or to look at the progress use (git pull origin <‘branch name’>).
    - Maintain frequent communication as this is a collective project, so we will need to help each other. Don't forget to ask for help or let us know before you do a pull or push.
    - When you have to add libraries for some reason, let the others know to edit (requirements.txt).
    - Good luck! 😁