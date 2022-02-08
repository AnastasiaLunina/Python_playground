# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is his/her name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combined_name = (name1 + name2).lower()

t = combined_name.count('t')
r = combined_name.count('r')
u = combined_name.count('u')
e = combined_name.count('e')

l = combined_name.count('l')
o = combined_name.count('o')
v = combined_name.count('v')
e = combined_name.count('e')

true_score = int(t+r+u+e)
love_score = int(l+o+v+e)

total_score = str(true_score) + str(love_score)
match_score = int(total_score)

if match_score < 10 or match_score > 90:
    print(f"Your love score is {match_score}, you go together like coke and mentos.")
elif 40 <= match_score <= 50:
    print(f"Your love score is {match_score}, you are alright together.")
else:
    print(f"Your love score is {match_score}.")