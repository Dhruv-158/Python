question = [
    "1) What is the capital of France? \n A) Berlin B) London \n C) Paris D) Rome",
    "2) Who wrote Romeo and Juliet? \n A) Charles Dickens B) William Shakespeare \n C) Jane Austen D) Mark Twain",
    "3) In which year did the Titanic sink? \n A) 1905 B) 1912 \n C) 1923 D) 1931",
    "4) What is the largest planet in our solar system? \n A) Earth B) Jupiter \n C) Mars D) Saturn",
    "5) Who painted the Mona Lisa? \n A) Vincent van Gogh B) Leonardo da Vinci \n C) Pablo Picasso D) Claude Monet",
    "6) What is the capital of Bhutan? \n A) Kathmandu B) Thimphu \n C) Colombo D) Ulaanbaatar",
    "7) Who is the author of One Hundred Years of Solitude?\n A) Gabriel Garcia Marquez B) Salman Rushdie \n C) Haruki Murakami D) Isabel Allende",
    "8) In chemistry, what does pH measure?\n A) Density B) Acidity or alkalinity \n C) Temperature D) Mass",
    "9) What is the speed of light in a vacuum?\n A) 299,792 kilometers per second B) 150,000 miles per second \n C) 1,000,000 kilometers per hour D) 186,282 miles per second",
    "10) Which element has the chemical symbol 'Au'? \n A) Silver B) Gold \n C) Platinum D) Mercury",
    "11) Who was the first woman to win a Nobel Prize? \n A) Marie Curie B) Rosalind Franklin \n C) Dorothy Crowfoot Hodgkin D) Barbara McClintock",
    "12) What is the capital of Mongolia? \nA) Astana B) Tbilisi \nC) Ulaanbaatar D) Bishkek",
    ]
user_anss = []

for i in question:
    print(i)
    while True:
        your_ans = input("Enter your ans : ").upper()
        if your_ans in ["A","B","C","D"]:
            break 
        else:
            print("invald ans please chose correct ans")
    user_anss.append(your_ans)

print("\n Your Answers : ")
for i,ans in enumerate(user_anss,start=1):
    print(f"Question {i} : {ans}")
    
question_answers = [
     "C",
     "B",
     "B",
     "B",
     "B",
     "B",
     "A",
     "B",
     "A",
     "B",
     "A",
     "C",
]
for question_number, user_ans in enumerate(user_anss, start=1):
    correct_ans = question_answers.get(question_number)
    if user_ans == correct_ans:
        print(f"Question {question_number}: Your answer '{user_ans}' is correct!")
    else:
        print(f"Question {question_number}: Your answer '{user_ans}' is incorrect. Correct answer is '{correct_ans}'.")