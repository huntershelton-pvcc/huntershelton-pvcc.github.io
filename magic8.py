# Name: Hunter Shelton
#   Prog Purpose: This Magic 8-Ball code uses a Python tuple since the
#   user does not have the ability to change the 8-Ball answers.
#   However, the program could have used a Python list instead of a tuple.
#   NOTE: Tuples use parentheses; lists use square braces.
#   We use a tuple because tuples are faster and use less memory than lists.
#   Tuples, unlike lists, are immutable.

import random
answers_8_ball = ( "As I see it, yes", "Ask again later",
                  "Better not tell you now", "Cannot predict now",
                  "Concentrate and ask again", "Don't count on it",
                  "It is certain", "It is decidedly so",
                  "Most likely", "My reply is no",
                  "Outlook not so good", "Reply hazy, try again",
                  "Signs point to yes", "Very doubtful",
                  "Without a doubt", "Yes",
                  "Yes, definitely", "You may rely on it", )

def main():
    print("I am the MAGIC 8-BALL and can answer any YES or NO question!")
    
    another_question = True

    while another_question:
        answer = random.choice(answers_8_ball) # the answer is determined before the question is even asked
        print("\nShake the MAGIC 8-BALL")
        print("...and now...")
        question = input("\nWhat is your YES or NO question? ") # note: the question input is never actually utilized
        print("The MAGIC 8-BALL says: " + answer)

        repeat = input("\nWould you like to ask the MAGIC 8-BALL another question? (Y/N): ")
        while(repeat.upper() != "Y" and repeat.upper() != "N"): # loop to actually require Y/y to repeat cycle. otherwise, loop was default
            repeat = input("Please press Y if you wish to ask another question, or N to end the program.\n")
        if repeat.upper() == "N":
            another_question = False
    
    print("\nCome back anytime you have more YES/NO questions.")
    print("...Magic 8-Ball OUT.")

main()
