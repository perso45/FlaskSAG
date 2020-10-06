#I haave a really bad habit of creating projects
#Do with this what you will

#Imports
import os
import getpass

#Paths
path = str(input("What is the path for your project? (End with a '/') "))

if path == "":
    userName = getpass.getuser()
    path = "/home/"+userName+"/Desktop/"

print(path)

#name
projectName = str(input("What is the name of your project? "))

print(projectName)

dirName = path+projectName

#Project folder creation
try:
    os.mkdir(dirName)
except OSError:
    print("The creation of %s failed, maybe this is a sign or maybe you wrote the path wrong." % dirName)
else:
    print("Successfully created the directory %s." % dirName)

#Flask Website File
portNum = int(input("Which port would you like to use? "))

if portNum == "":
    portNum = 5000

fFile = open(os.path.join(dirName,projectName+"_flask.py"),"w+")

fFile.write("from flask import render_template\nimport connexion\n#Makes application instance\napp = connexion.App(__name__,specification_dir='./')\n#Makes URL route in application for '/'\n@app.route('/')\ndef home():\n    return render_template('home.html')\n#If run in standalone mode, run application\nif __name__ == '__main__':\n    app.run(host='0.0.0.0',port=%d,debug=True)" % portNum)

fFile.close()

#Creates home.html Template Folder/File
try:
    os.mkdir(dirName+"/templates/")
except OSError:
    print("The templates dir could not be created")
else:
    print("The templates dir was successfully created")
    
home = open(os.path.join(dirName+"/templates/","home.html"),"w+")

home.write("<!DOCTYPE html>\n<html lang='en'>\n<head>\n    <title>%s Website Template</title>\n    <h1>%s Website Template</h1>\n<body>\n    <p>This is going to be a template for your website, just open your templates folder in your project and select home.html to edit it.</p>\n" % (projectName,projectName))

home.close()

#Runs Flask File
cmd = ('cd %s && python3 %s_flask.py' % (dirName, projectName))

os.system(cmd)
