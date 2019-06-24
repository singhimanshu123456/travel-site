#Import dependencies
from subprocess import call

#Commit Message
with open("hello.txt" ,"w") as f:
    f.write("hello")
commit_message = "Adding sample files"

#Stage the file 
call('git add .', shell = True)

# Add your commit
call('git commit -m "'+ commit_message +'"', shell = True)

#Push the new or update files
call('git push origin master', shell = True)