# mongodb_tutorial
 
 a) Download MongoDB from www.mongodb.com : Resources -> Server... -> On LHS click 'Installation' -> On RHS , choose your option...

b) Also download Mongosh from same site. Its a zipped file, so you have to  unzip it and follow steps listed below to get command 'mongosh'
working from command line.

######################################
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

c) If u use Visual Studio editor, then install extension 'MongoDB for VS Code'. On LHS, click the mongodb icon. 


COMMON COMMANDS:
cls : clear screen

exit: exit the shell

show dbs : show databases

use dbName : Create a new or switch databases ...e.g. 'use school'

db.dropDatabase() : delete DB

show collections : show all coll.

db.createCollection('students') : make sure u are in  school database to create this collection 

db.students.drop() : drop collection named students.

db.students.insertOne({ name: 'Bob', ht: 28, score: 5.2, isMale: True, DOB: new Date('2001-01-25')}) : Insert One Row

db.students.insertOne({ name: 'Kat', ht: 28, score: 5.2, isMale: False, DOB: new Date('2001-01-25'),
                        graDate:null, courses:['chemistry','physics'],
                        address: {HouseNo: 123, city: 'New York'}}) : Insert One Row

db.students.insertMany([{ name: 'Tom', ht: 28, score: 5.2, isMale: True, DOB: new Date('2001-01-25')},
                        { name: 'Jim', ht: 30, score: 7.2, isMale: True, DOB: new Date('2002-01-25')},
                        { name: 'Ash', ht: 26, score: 1.2, isMale: True, DOB: new Date('2006-01-25')}])


db.students.find() : Show all Rows/documents in a Collection students

db.students.find().pretty() : Show all Rows in a Collection (Prettified)

db.students.find().count() : count all students 

db.students.find().sort({name:1}) : sort by name desc. order ...use -1 for asc. order

db.students.find().limit(2) : Show 2 Rows/documents in a Collection students

db.students.findOne({name: 'Bob'}) : Find the first row matching the object

db.students.find({name: 'Bob'}) 

db.students.find({isMale: False}) 

db.students.find({}, {_id: False, name: True}) : return all doc. but only show name field

db.students.find({isMale: False}, {_id: False, name: True, DOB: True} ) show all docu. where male=False and display only names and DOB

db.students.updateOne({name:'Ash'},  { $set:{ht:25} }   ) : For name 'Ash', update ht to 25

db.students.updateOne({name:'Ash'},  { $unset:{ht:''} }   ) : For name 'Ash', remove ht 

db.students.updateOne({_id:ObjectId},  { $set:{ht:25} }   ) : For certain object ID, update ht to 25

db.students.updateMany({},  { $set:{favColor:null} }   ) : create new field and set its value to  null

db.students.updateMany({favColor:{$exists:False}},  { $set:{favColor:'blue'} }   ) : anyone who does not have fav. color, set their fav color to blue

