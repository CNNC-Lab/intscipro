# Exercise 0.3: this script has a mistake. Run it, read the error message, fix it.
# First run it from the main course folder:  python day02-fundamentals/setup/broken_4.py
# (Hint: the code is fine. Where does Python look for the file?)
with open("recording_notes.txt") as notes:
    print(notes.read())
