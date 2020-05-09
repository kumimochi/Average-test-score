#Get the average of three test scores

print('Enter your name: ')
name = input()
print('Hello, ' + name)


test1 = float(input('Enter your first test score: '))
test2 = float(input('Enter your second test score: '))
test3 = float(input('Enter your third test score: '))

#Calculate the average score
average_score = (test1 + test2 + test3) / 3.0
print('Your average score is ', average_score)