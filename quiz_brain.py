import html


class QuizBrain:
    """Gerencia a lógica do quiz, incluindo a navegação pelas perguntas, pontuação e verificação de respostas.

    Atributos:
        question_number (int): O número da pergunta atual (base 0).
        score (int): A pontuação atual do jogador.
        question_list (list): Uma lista de objetos Question.
        current_question (Question): O objeto Question da pergunta atual.
    """

    def __init__(self, q_list: list):
        """Inicializa um novo objeto QuizBrain.

        Args:
            q_list (list): Uma lista de objetos Question que compõem o quiz.
        """
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self) -> bool:
        """Verifica se ainda há perguntas no quiz.

        Returns:
            bool: True se houver mais perguntas, False caso contrário.
        """
        return self.question_number < len(self.question_list)

    def next_question(self) -> str:
        """Avança para a próxima pergunta do quiz.

        Define a pergunta atual, incrementa o número da pergunta e retorna o texto
        da pergunta formatado, com caracteres HTML escapados.

        Returns:
            str: O texto da próxima pergunta.
        """
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        # Desescapa entidades HTML no texto da pergunta para exibição correta
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text}"

    def check_answer(self, user_answer: str) -> bool:
        """Verifica se a resposta do usuário está correta.

        Compara a resposta do usuário (ignorando maiúsculas/minúsculas) com a resposta correta.
        Se estiver correta, incrementa a pontuação.

        Args:
            user_answer (str): A resposta fornecida pelo usuário.

        Returns:
            bool: True se a resposta estiver correta, False caso contrário.
        """
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False


