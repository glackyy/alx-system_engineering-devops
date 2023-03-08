DON'T FORGET : #!/bin/bash in vi or emacs.
0-Path name of the current directory : pwd //
1-list content of the current directory : ls //
2-change from directory to user's home directory : cd ~ //
3-Display current directory contents in a long format : ls -l //
4-Display current directory contents in a long format,including files starting with(.) : ls -al or ls -a -l //
5-Display current directory contents : LongFormat/user,groupids(n)/hiddenFiles(.) : ls -nal or ls -n -a -l //
6-Script that creates a directory named my_first_directory in the /tmp/ directory : mkdir /tmp/my_first_directory //
7-move a file from a directory to another directory : mv /tmp/betty /tmp/my_first_directory //
8-Delete the file betty.from the directory /tmp/my_first_directory : rm /tmp/my_first_directory/betty //
9-Delete the directory my_first_directory from /tmp directory : rm -r /tmp/my_first_directory //
10-Script that changes the working directory to the previous one : cd - (don't do cd .. it won't work) //
11-script that lists all files (even ones with names beginning with a period character, which are normally hidden) in the current directory and the parent of the working directory and the /boot directory (in this order), in long format : ls -al . .. /boot //
12-Script that prints the type of the file named iamafile. The file iamafile will be in the /tmp directory when we will run your script : file /tmp/iamafile //
13-Symbolic link to /bin/ls, named __ls__. The symbolic link should be created in the current working directory : ln -s bin/ls __ls__ //
14-Script that copies all the HTML files from the current working directory to the parent of the working directory, but only copy files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory : cp -un *.html ../ PS : (-un = files that does not exist in the parent of the working directory) //*
15-Script that moves all files beginning with an uppercase letter to the directory /tmp/u : mv [[:upper:]]* /tmp/u //
16-Script that deletes all files in the current working directory that end with the character ~ : rm *~ //*
17-Script that creates the directories welcome/, welcome/to/ and welcome/to/school in the current directory : mkdir -p welcome/to/school // 
18-Command that lists all the files and directories of the current directory : ls -amvp //
19-Magic file school.mgc that can be used with the command file to detect School data files. School data files always contain the string SCHOOL at offset 0 : 
> 0 string SCHOOL School data
> !:mime School //
In your current working directory convert the file school.mgc : file -C -m school.mgc //
PS :
DON'T FORGET TO DO : chmod u+x filename after you are done with the vi or emacs //
git add . 
git commit -m "message"
git push

