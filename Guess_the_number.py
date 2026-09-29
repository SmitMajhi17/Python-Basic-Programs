a = 34
count = 0

while True:
     no = int(input("Enter a number between 1 to 100: "))
     count+=1
     if no==a:
        print('Congratulationss!! You guessed the correct number👏')
        break
     elif no>a:
        print('Too high!')
     else:
        print('Too low!')
        
print("You guessed the correct number in", count, "attempts")
