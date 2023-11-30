# add is a function pointer, no name for function, and it adds x + y
# before : is the arguments (variables the need to be entered) ----   after : is the functionality of it
add = lambda x, y: x + y

result = add(3,5)
print(result)

numbers = [1, 2, 3, 4, 5]
squareNumbers = list(map(lambda x: x ** 2, numbers))
print(squareNumbers)

fahrenheitTemperatures = [212, 32, 100]
celsiusTemperatures = list(map(lambda f: (f - 32) * 5.0 / 9.0, fahrenheitTemperatures))
print(celsiusTemperatures)

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
#sort the list in reverse order (high to low) ----  remove the reverse to sort in order (low to high)
sortedNumbers = sorted(numbers, reverse = True)
print(sortedNumbers)

midterm = {'Carol': 92, 'Alice': 95, 'Bob': 88, 'Dave': 70, 'Eve': 100}
#sorts the names in alphabetical order (sorts by key not value)
sortedScores = sorted(midterm)
print(sortedScores)

#sorts the score in reverse order (high to low) based off the score instead of the name (value instead of key)
sortedScores2 = sorted(midterm.items(), key = lambda i: i[1], reverse = True)
print(sortedScores2)

#list of tupils (2D)
points = [(1, 3), (2, 1), (4, 2)]
#sorts it in ascending order based off 2nd number
sortedPoints = sorted(points, key = lambda x: x[1])
print(sortedPoints)

#list of tupils (3 tupil) (3D)
points = [(1, 3, 10), (2, 1, 20), (4, 2, 15)]
#sorts it in ascending order based off 3nd number
sortedPoints2 = sorted(points, key = lambda x: x[2])
print(sortedPoints2)