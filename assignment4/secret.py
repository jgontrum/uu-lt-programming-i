from random import randint

secret = randint(0, 100)
user_guess = None
guesses = 0


def evaluate_user_performance(score):
    if score == 1:
        return "Magic! Only one guess!"
    elif score < 4:
        return "Only %s guesses. Very impressive." % score
    elif score < 8:
        return "You needed %s guesses. That not so good." % score
    else:
        return "Booo! %s guesses needed. Try better!" % score


while user_guess != secret:
    try:
        user_guess = int(input("What is your guess? "))
    except ValueError:
        print("That was not a number. Guess again!")
        continue

    if user_guess > secret:
        print("Your guess is too high.")
    elif user_guess < secret:
        print("Your guess is too low.")
    guesses += 1

print(evaluate_user_performance(guesses))
