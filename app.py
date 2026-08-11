print ("hello world")

#git status
# git init()

# wap to check a number is prime or not

def prime (num):

    for i in range (2,num):

        if num % i == 0:

            print ("not prime")

        else:

            print ("its prime")

            break

prime(7)

# check amstrong or not 

n = int(input("Enter a number: "))
s = 0
temp = n

while temp > 0:
    r = temp % 10
    s += r ** 3
    temp //= 10

if s == n:
    print("Armstrong")
else:
    print("Not Armstrong")


"""
git --version >>>> to check the current version of the git installed 

git config --list >>> to get the configaration list in git

git status >>> to check the status of directory (folder) using git 

git init >>> initialise the git into the current working directory into staging area 


staging area >>> refers to the point where the files are ready to push into git(for each change)

git app.py >>> add only the app.py into the staging area 
git commit -m "message " >> commit the current change (version) into the git respiratory

commit >>> a snapshot of ur project at a particullar point 

git log >> the entire history and list of all commits from the directory
"""