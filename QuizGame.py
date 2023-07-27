questions = [
  {
    "question": "Q1 What is the capital of France?",
        "options": ["A) London", "B) Paris", "C) Madrid", "D) Rome"],
        "correct_answer": "B"
  },
  {
    "question": "Q2 Which planet is known as the 'Red Planet'?",
        "options": ["A) Venus", "B) Mars", "C) Jupiter", "D) Saturn"],
        "correct_answer": "B"
  },
     {
        "question": "Q3 What is the capital of Australia?",
        "options": ["A) Sydney", "B) Canberra", "C) Melbourne", "D) Perth"],
        "correct_answer": "B"
    },
    {
        "question": "Q4 Which is the largest ocean in the world?",
        "options": ["A) Atlantic Ocean", "B) Indian Ocean", "C) Southern Ocean", "D) Pacific Ocean"],
        "correct_answer": "D"
    },
    {
        "question": "Q5 Who painted the Mona Lisa?",
        "options": ["A) Leonardo da Vinci", "B) Vincent van Gogh", "C) Pablo Picasso", "D) Michelangelo"],
        "correct_answer": "A"
    },
    {
        "question": "Q6 What is the chemical symbol for gold?",
        "options": ["A) Ag", "B) Au", "C) Fe", "D) Hg"],
        "correct_answer": "B"
    },
    {
        "question": "Q7 Which planet is known as the 'Red Planet'?",
        "options": ["A) Venus", "B) Mars", "C) Jupiter", "D) Saturn"],
        "correct_answer": "B"
    },
    {
        "question": "Q8 What is the largest mammal in the world?",
        "options": ["A) Elephant", "B) Blue whale", "C) Polar bear", "D) Lion"],
        "correct_answer": "B"
    },
    {
        "question": "Q9 Who wrote the play 'Romeo and Juliet'?",
        "options": ["A) William Shakespeare", "B) Charles Dickens", "C) Jane Austen", "D) Mark Twain"],
        "correct_answer": "A"
    },
    {
        "question": "Q10 Which is the largest planet in our solar system?",
        "options": ["A) Jupiter", "B) Saturn", "C) Earth", "D) Mars"],
        "correct_answer": "A"
    },
]
prize = 0
score = 0
for question in questions:
    print(question["question"])
    for option in question["options"]:
      print(option)
    print()

    ans=input("Lock your answer - ")
    if ans.upper() == question["correct_answer"]:
      print("Congratulations your answer is correct.🎉🎉")
      prize += 10000
      score += 1
      print("You have won ",prize)
    else :
      print("We are so sad to say this but this answer is wrong.😔😔")
      break
    print()
print("And the game ends here.")
print("You have won ",prize)
print("Your Scores are ",score)