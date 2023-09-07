def main():
    finalExamScores = [100, 82, 93, 81, 55, 72]
    print(finalExamScores[2:]) #prints everything at and after the index 2 of the list (called "Slicing the list")
    print(finalExamScores[:3]) #prints everything at index 0 to 2 doesnt include 3 (similar to range function)
    finalExamScores[3] = 10
    print(finalExamScores[1:4]) #prints everything at index 1 to 3 doesnt include 4 (similar to range function)

    bsu = "Ball State University"
    bsu[2] = 'x'
    print(bsu[:12]) #prints everything before index 12 including spaces
    print(bsu[-5]) #starts backwards and prints the letter
    print(bsu[-5:-3]) #starts backwwards at "r" then gots to index "-3" but doesnt print it
    print(bsu[-3:-5]) #doesnt print anything because you cant go forward till index -5

    #for letter in bsu:
        #print(letter) #prints out each letter in a string



main()
