DON'T FORGET : #!/bin/bash in vi or vim.
Path name of the current directory : pwd //
list content of the current directory : ls //
change from directory to user's home directory : cd ~ //
Display current directory contents in a long format : ls -l //
Display current directory contents in a long format,including files starting with(.) : ls -al or ls -a -l //
Display current directory contents : LongFormat/user,groupids(n)/hiddenFiles(.) : ls -nal or ls -n -a -l //
Script that creates a directory named my_first_directory in the /tmp/ directory : mkdir /tmp/my_first_directory //
move a file from a directory to another directory : mv /tmp/betty /tmp/my_first_directory //
Delete the file betty.from the directory /tmp/my_first_directory : rm /tmp/my_first_directory/betty //
Delete the directory my_first_directory from /tmp directory : rm -r /tmp/my_first_directory //
Script that changes the working directory to the previous one : cd - (don't do cd .. it won't work) //
script that lists all files (even ones with names beginning with a period character, which are normally hidden) in the current directory and the parent of the working directory and the /boot directory (in this order), in long format : ls -al . .. /boot //



