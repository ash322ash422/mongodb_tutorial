# mongodb_tutorial
 Tutorial on MongoDB

Steps to get command 'mongosh' working from  command line:
 
1)Get the filepath to the "mongosh.exe" file (The file path without the "\mongosh.exe" at the end, so it should look something like this: "...\mongosh-1.10.6-win32-x64\bin").

2)Type 'environment variable' in the start menu and under Advanced tab,  open 'environment variables

3)In the "User variables for your user", there will be a box containing a number of variables and in these there will be one called "Path", this is the one we are going to edit, so click on it.

4)To edit this variable, still in the top part, click on the button that says "Edit..." (notice that this is the button that is below all the variables in the top section, I specify this since there is two sections that contain the same buttons, so just stick to the top one).
Once you clicked edit, it should have opened another tab called "Edit environment variable", this tap is a list of file paths (or with none in case you have never enter a file path there), with some buttons on the left. You need to click the button that says "New".
Once you clicked "New" it should have added a place where you can put the filepath to the "mongosh.exe" file, put the file path, and hit enter.
Then press "ok" at the bottom left, to confirm the changes.
In the "Environment Variables" tab, press "ok" in the bottom left to finalize the process.
#################################################################