class Question:
    """Representa uma única pergunta de quiz com seu texto e resposta correta.

    Atributos:
        text (str): O texto da pergunta.
        answer (str): A resposta correta para a pergunta.
    """

    def __init__(self, q_text: str, q_answer: str):
        """Inicializa um novo objeto Question.

        Args:
            q_text (str): O texto da pergunta.
            q_answer (str): A resposta correta para a pergunta.
        """
        self.text = q_text
        self.answer = q_answer


