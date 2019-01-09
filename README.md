# EasyClaims



   0. Clone the project from GitHub - run the command “git clone https://github.com/kalyanshashi/EasyClaims”
1. Run the command “git branch” to validate the branches as mentioned in the below sample output
          (venv) 19:08 ~/EasyClaims (staging)$ git branch
              develop
              master
             * staging

2. Checkout to development branch - run command “git checkout develop”
3. Create python3 environment - run command “python3 -m venv venv”
4. Activate created virtual environment - run command “source venv/bin/activate”
5. Install required packages to the project - run command “pip -r requirements.txt”
  6. “cd easyclaims”
  7. run “./manage.py makemigrations”
  8. run command “./manage.py migrate”
  

Git commands:
———————

Git life cycle

Staging —> Committing —> Pushing


Configure git your userid and email (GitHub registered email id):

git config —global user.name “kalyanshashi”
git config —global user.email “shashikalyan421@gmail.com”

Verify where your local branch pointing to right now:

	git branch

	Note: Observe * over there — where it is pointing to that branch

Switch to another branch:

	git checkout <branch_name>

Pull the latest changes from the remote repository:

	git pull


Check the status of git (Run below command every time during git related information to know the status of your current repository):

	git status

Staging/adding modified files:

	To add all modified files:

		git add -A

	To add specific file:

		git add <file_name>

To remove the modified changes (in case required):

	git stash

	Note: Above command is dangerous as it will remove all your changes. Be careful before executing it.

Commit the files to your local branch:

	git commit -a -m “<Appropriate message>”

Push the changes to your remote branch:

	git push -u origin <branch_name>






 



