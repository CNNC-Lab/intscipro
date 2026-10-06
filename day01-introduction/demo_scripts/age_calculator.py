"""Tiny first script: how many years until you turn 100?"""

my_age = int(input("How old are you? "))

if my_age >= 100:
    print("You have already turned 100!")
else:
    years_to_go = 100 - my_age
    print(f"You will turn 100 in {years_to_go} years.")
