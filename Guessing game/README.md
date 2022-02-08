# Welcome to Gussing game! 

This is a Guess the Number game. You can try 6 times.

```python
import random
guessesTaken = 0
print("Hello, what is your name?")
myName = input()

number = random.randint(1,20)
print("Well, " + myName + ", I am thinking of a number between 1 and 20")
for guessesTaken in range(6): 
  print("Take a guess. ")
  guess = input()
  guess = int(guess)

  if guess < number:
    print("Your guess is too low")
  if guess > number:
    print("Your number is too high")
  if guess == number:
    break    
if guess == number:
  guessesTaken = str(guessesTaken + 1)
  print("Good job, " +myName+ "! You guessed my number in " + guessesTaken + " guesses!")
if guess != number:
  number = str(number)
  print("Nope. The number I was thinking of was " + number + ".") 
```

## Link to repl.it

https://replit.com/@AnastasiaLunina/guesspy#main.py
