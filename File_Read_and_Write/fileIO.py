def main():
    fileData = open("Students.txt", "r") #rt (read text files) #rb (binairy text/plain text)
    students = fileData.readlines()
    fileData.close()
    fileOutput = open("output.txt", "w") #a(appends) instead of w(erases what was already there and overrides)
    for s in students:
        parts = s.split(',')
        #print(parts)
        gpa = float(parts[3])
        #print(gpa)
        fileOutput.write(parts[1] + "'s GPA is " + str(gpa) + "\n")
    fileOutput.close()

main()
