import data
import question_model
import quiz_brain

data = data.question_data

question_bank = [question_model.Question(q['question'], q['correct_answer']) for q in data]

quiz = quiz_brain.QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
    
print("You've completed the quiz!")
print(f"Your final score is {quiz.score}/{quiz.q_num}")
