from subprocess import call
import os

for root, dirs, files in os.walk(".", topdown=False):
    for name in files:
        File = os.path.join(root,name)
        if File.endswith(".py"):
            call(["2to3","-w",File])
            
# with open("files_to_change.txt","r") as f:
#     for line in f.read().split("\n"):
#         if line.endswith(".py"):
#             call(['2to3',"-w",line])
