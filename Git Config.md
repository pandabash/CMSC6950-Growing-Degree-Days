### How to config your local git env

1. make a directory to store the remote repository. In my local ubuntu,it is named CMSC6950Poject
   mkdir CMSC6950Poject
   cd CMSC6950Poject
2. clone the whole repository from remote server to your local folder
   git clone https://github.com/cw7734/CMSC6950-Growing-Degree-Days.git
   cd CMSC6950-Growing-Degree-Days/
3. create your local workbranch,please name your local work branch as yourname
   git checkout -b xiaowang
4. after step 3, you create a new branch has same content with remote master branch,and also work on
   your local branch.
5. Use CMD git branch, verify that your local has two branch, master and XXX, also now work on XXX.
6. use CMD git branch -r , verify that remote only has mater branch, -r means remote
7. make changes to your local branch, as example, the Git config will add to my local branch 
8. git add XXX, for example, git add "Git Config", add this config file to local branch(xiaowang)
9. git commit -m "add git config" as an example
10. git push -u origin xiaowang , this step to push whole xiaowang branch to remote server
