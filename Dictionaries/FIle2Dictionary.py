def main():
    students = {} #{} means it is a dictionary
    fileHandle = open("../File_Read_and_Write/Students.txt", "r")
    fileData = fileHandle.readlines() # read lines: reads every lines

    for lines in fileData:
        parts = lines.split(',')
        students[parts[0]] = [parts[1], parts[2], parts[3], parts[4]]
    fileHandle.close()

main()
