#Quiz Game With Scores

print("====Quiz Game====")
Score = 0
question = [
    {
        "question":"1.Which language are we learning?",
        "options": ["A.Java", "B.Python", "C.HTML", "D.C++"],
        "answer": "B"
    },
    {
        "question": "2.Which company created Python?",
        "options": ["A.Microsoft", "B.Google", "C.Python Software Foundation", "D.Apple"],
        "answer": "C"
    },
    {
        "question": "3.Which symbol is used for comments in Python?",
        "options": ["A.//", "B.#", "C./*", "D.&"],
        "answer": "B"
    },
    {
        "question": "4.Which function displays output in Python?",
        "options": ["A.input()", "B.show()", "C.print()", "D.display()"],
        "answer": "C"
    },
    {
        "question": "5.Which function takes user input?",
        "options": ["A.print()", "B.input()", "C.write()", "D.output()"],
        "answer": "B"
    },
    {
        "question": "6.Which data type stores whole numbers?",
        "options": ["A.str", "B.float", "C.int", "D.list"],
        "answer": "C"
    },
    {
        "question": "7.Which keyword is used for a condition?",
        "options": [" A.if", "B.repeat", "C.define", "D.loop"],
        "answer": "A"
    },
    {
        "question": "8.Which loop can repeat code in Python?",
        "options": ["A.repeat", "B.again", "C.loop", "D.while"],
        "answer": "D"
    },
    {
        "question": "9.Which symbol checks equality in Python?",
        "options": ["A.=", "B.==", "C.!=", "D.>"],
        "answer": "B"
    },
    {
        "question": "10.Which data type stores True or False?",
        "options": ["A.int", "B.str", "C.bool", "D.float"],
        "answer": "C"
    }
]



for q in question:
    print(q["question"])
    for option in q["options"]:
     print(option)

    user_answer = input("your answer: ").lower()
    if user_answer == q["answer"].lower():
        print("Correct Answer!")
        Score = Score+1
    else:
        print("Wrong Answer!")

print("Final Score:", Score, "/", len(question))







    
