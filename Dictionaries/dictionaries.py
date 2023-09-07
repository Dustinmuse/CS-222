def main():
    #finalExamScores = [100, 82, 93, 81, 55, 72]
    finalExamScores = {
        "Alice" : 100,
        "Bob" : 82,
        "Carol" : 93,
        "Dave" : 81,
        "Eve" : 55,
        "Frank" : 72
    }
    print("Gary" in finalExamScores.keys())
    print(finalExamScores.get('Carol')) #gets the value  of Carol
    print(finalExamScores.get("Harry")) #single quotes or doule quotes dont matter || returns nothing since Harry isnt in finalExamScores

    #print(finalExamScores["Eve"])
    finalExamScores["Eve"] = 57
    #print(finalExamScores["Eve"])

    #for key, value in finalExamScores.items(): gives both
        #print(value)

    #for v in finalExamScores.values(): gives values
        #print(v)

    for k in finalExamScores.keys(): #gives keys
        print(k)
    students = [
        {
        "firstName" : "Alice",
        "lastName" : "Smith",
        "major" : "Chemistry",
        "gpa" : 3.92,
        "courses" : ["CS 120", "CS 124", "MATH 165"]
         },

         {
        "firstName" : "Bob",
        "lastName" : "Jones",
        "major" : "Physics",
        "gpa" : 3.3,
        "courses" : ["CS 222", "MATH 166"]
         }
    ]
    #print(alice["courses"]) prints all courses in "courses"
    #print(alice["courses"][2]) prints the specific course at index 2

    #for c in bob["courses"]:
        #print(c)

    print(len(students))
    for s in students:
        if s["major"] == "Physics":
            print(s["lastName"] + ", " + s["firstName"])
        if s["gpa"] > 3:
            print(s)
        if "CS 222" in s["courses"]: #if the person is taking class CS 222 all their info will be printed
            #print(s)
            print(s["lastName"] + ", " + s["firstName"]) #print last and first name for people taking CS 222


main()
