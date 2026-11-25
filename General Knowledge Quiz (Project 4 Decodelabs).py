# PROJECT 4: GENERAL KNOWLEDGE QUIZ

score = 0

print("=" * 45)
print("WELCOME TO THE GENERAL KNOWLEDGE QUIZ")
print("=" * 45)

print("Answer the following 3 questions.")
print("Each correct answer earns 1 point.\n")


# QUESTION 1
answer = input("1. What is the capital of France? ")
answer = answer.strip().lower()

if answer == "paris":
    print("Correct! +1 point.\n")
    score += 1
else:
    print("Incorrect. The correct answer is Paris.\n")


# QUESTION 2
answer = input("2. Which planet is known as the Red Planet? ")
answer = answer.strip().lower()

if answer == "mars":
    print("Correct! +1 point.\n")
    score += 1
else:
    print("Incorrect. The correct answer is Mars.\n")


# QUESTION 3
answer = input("3. What is the largest ocean on Earth? ")
answer = answer.strip().lower()

if answer == "pacific ocean" or answer == "pacific":
    print("Correct! +1 point.\n")
    score += 1
else:
    print("Incorrect. The correct answer is the Pacific Ocean.\n")


# FINAL SCORE
print("=" * 45)
print("QUIZ RESULT")
print("=" * 45)

print(f"Your final score is: {score}/3")

if score == 3:
    print("Excellent work!")
elif score == 2:
    print("Great job!")
elif score == 1:
    print("Good effort! Keep practising.")
else:
    print("Keep learning. Try again!")

print("=" * 45)