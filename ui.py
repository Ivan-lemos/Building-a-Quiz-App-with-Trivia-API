from tkinter import *
from quiz_brain import QuizBrain

# ---------------------------- CONSTANTES ------------------------------- #
THEME_COLOR = "#375362"  # Cor de fundo principal da interface
FONT_QUESTION = ("Arial", 20, "italic") # Fonte para o texto da pergunta
FONT_SCORE = ("Arial", 12, "normal") # Fonte para o placar

# ---------------------------- CLASSE DA INTERFACE DO QUIZ ------------------------------- #

class QuizInterface:
    """Gerencia a interface gráfica do usuário (GUI) para o aplicativo de quiz.

    Atributos:
        quiz (QuizBrain): Uma instância da classe QuizBrain que contém a lógica do quiz.
        window (Tk): A janela principal da interface gráfica.
        score_label (Label): O rótulo para exibir a pontuação.
        canvas (Canvas): A área de desenho para exibir o texto da pergunta.
        question_text (int): O ID do item de texto da pergunta no canvas.
        true_button (Button): O botão para a resposta "Verdadeiro".
        false_button (Button): O botão para a resposta "Falso".
    """

    def __init__(self, quiz_brain: QuizBrain):
        """Inicializa a interface do quiz.

        Args:
            quiz_brain (QuizBrain): Uma instância da classe QuizBrain.
        """
        self.quiz = quiz_brain

        # Configuração da janela principal
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Rótulo da pontuação
        self.score_label = Label(text="Pontuação: 0", fg="white", bg=THEME_COLOR, font=FONT_SCORE)
        self.score_label.grid(row=0, column=1, pady=(0, 20)) # Adiciona um pouco de padding abaixo do placar

        # Canvas para exibir a pergunta
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150,  # Posição X (centro do canvas)
            125,  # Posição Y (centro do canvas)
            width=280,  # Largura máxima do texto antes de quebrar a linha
            text="Texto da Pergunta Aqui",
            fill=THEME_COLOR,
            font=FONT_QUESTION,
            anchor="center" # Centraliza o texto no ponto (x,y)
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        # Botões de Verdadeiro/Falso
        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed, borderwidth=0)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed, borderwidth=0)
        self.false_button.grid(row=2, column=1)

        # Carrega a primeira pergunta
        self.get_next_question()

        # Inicia o loop principal da interface gráfica
        self.window.mainloop()

    def get_next_question(self) -> None:
        """Busca a próxima pergunta do QuizBrain e atualiza a interface.

        Se ainda houver perguntas, atualiza o texto da pergunta e a pontuação.
        Caso contrário, exibe uma mensagem de fim de quiz e desabilita os botões.
        """
        self.canvas.config(bg="white")  # Reseta a cor de fundo do canvas
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Pontuação: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="Você chegou ao fim do quiz!")
            self.true_button.config(state="disabled")  # Desabilita o botão Verdadeiro
            self.false_button.config(state="disabled") # Desabilita o botão Falso

    def true_pressed(self) -> None:
        """Chamado quando o botão "Verdadeiro" é pressionado.

        Verifica a resposta e fornece feedback visual.
        """
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self) -> None:
        """Chamado quando o botão "Falso" é pressionado.

        Verifica a resposta e fornece feedback visual.
        """
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right: bool) -> None:
        """Fornece feedback visual ao usuário (verde para correto, vermelho para incorreto).

        Após 1 segundo, carrega a próxima pergunta.

        Args:
            is_right (bool): True se a resposta do usuário foi correta, False caso contrário.
        """
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        # Agenda a chamada para get_next_question após 1000ms (1 segundo)
        self.window.after(1000, self.get_next_question)


