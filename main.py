from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizInterface
from data import get_trivia_questions

# Obtém os dados das perguntas da API de trivia
# O número de perguntas e o tipo podem ser ajustados aqui
question_data = get_trivia_questions(amount=10, question_type="boolean")

# Cria uma lista de objetos Question a partir dos dados obtidos
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# Inicializa o cérebro do quiz com o banco de perguntas
quiz = QuizBrain(question_bank)

# Inicializa a interface do usuário do quiz
quiz_ui = QuizInterface(quiz)

# O loop principal do quiz é gerenciado pela interface do usuário (Tkinter mainloop)
# O código abaixo é apenas para demonstração de como o quiz_brain funcionaria sem a UI
# while quiz.still_has_questions():
#     quiz.next_question()

print("Você completou o quiz")
print(f"Sua pontuação final foi: {quiz.score}/{quiz.question_number}")


