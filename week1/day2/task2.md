1. Delete your local repo.
rm -r git

2. clone your repo locally.
git clone SHA256:VzCIInrGA7bN3L0LmyQSlJZTxUhRZjvdjLCthNKfsbg

3. create new branch called `feature-add-new-week` from `main` branch.
git checkout -b feature-add-new-week 

4. create new folder called `week2` using command kine `mkdir`.
mkdir week2

5. Create new file inside `week2` called `README.md` using `touch`.
cd week2
 touch read.me

6. Add this line `# Hello From Week 2` to the file `README.md` using `echo "" > README.md`
echo "# Hello From Week 2">read.me


7. add the folder `week1` to the staging area.
git add .

8. Commit the staged files.
git commit -m "version2"


9. See your tracking status using `git status` to make sure all files are committed.
git status

10. merge your branch to `main` branch.
git merge feature-add-new-week

11. Delete your branch.
git branch -d feature-add-new-week

12. See all your commits.
git log
