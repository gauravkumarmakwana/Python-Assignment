#Use the OS module and files functions to check if the text file named StudentDetails.txt exists In the parent folder of the assignment - 2 folder, if it does not exist create the text file. Add names of 3 students and their birthdates to the file and then close the file. Open the file again and add two more student details to the file. Finally read the details of all the students from the file and display them properly on screen. Return the names of all students in a list named snames.
import os
fileName = "StudentDetails.txt"
if os.path.exists(fileName):
    print(fileName, end = '')
    print("Exits already!")
else:
    wr = open(fileName, 'w')
    wr.write("Gaurav, 22/05/2003\n")
    wr.write("Jaydip, 28/07/2003\n")
    wr.write("Gautam, 14/11/2002\n")
    wr.close()

app = open(fileName, 'a')
app.write("Gotiyo, 14/11/2002\n")
app.write("Amdavadi, 08/07/2003\n")
app.write("Chakali, 31/08/2003\n")
app.close()

rd = open(fileName, 'r')
#print(rd.read())

snames = rd.read()
print(snames)
rd.close()
