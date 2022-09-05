# a dictionary that stores questions and answers
# have a variable that tracks the score of the player
# loop through the dictionary using the key values pairs
# display each question to the user and allow then to answer
# tell them if they are right or wrong
# show the final result when quiz is completed
quiz = {
    "question1": {
        "question": "What is the capital of Cuba?",
        "answer": "Cuba"
    },
    "question2": {
        "question": "What is the capital of France?",
        "answer": "Paris"
    },
    "question3": {
        "question": "What is the capital of Italy?",
        "answer": "Roma"
    },
    "question4": {
        "question": "What is the capital of Spain?",
        "answer": "Madrid"
    },
    "question5": {
        "question": "What is the capital of Portugal?",
        "answer": "lisboa"
    },
    "question6": {
        "question": "What is the capital of China?",
        "answer": "Pekin"
    },
    "question7": {
        "question": "What is the capital of Austria?",
        "answer": "Viena"
    }
}

score = 0

for key, value in quiz.items():
    print(value['question'])
    answer = input("Answer?")

    if answer.lower() == value['answer'].lower():
        print("Correct")
        score = score + 1
        print("Your score is: " + str(score) + "\n")

    else:
        print("Wrong!!!")
        print("The answer is:" + value['answer'])
        print("Your score is:" + str(score) + "\n")

print("You got " + str(score) + " out of 7 questons correctly")
print("Your percentage is " + str(score/7 * 100) + "%")
