Get your local Git repository on Bitbucket
Step 1: Switch to your repository's directory

cd /path/to/your/repo
Step 2: Connect your existing repository to Bitbucket

git remote add origin https://ndiayeom@bitbucket.org/ndiayeom/blent_python_project.git
git push -u origin main
zuXXCFwfjeRULGsWkd4u

===============================
…or create a new repository on the command line
echo "# blent_python_project" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/ndiayeom/blent_python_project.git
git push -u origin main


…or push an existing repository from the command line
git remote add origin https://github.com/ndiayeom/blent_python_project.git
git branch -M main
git push -u origin main