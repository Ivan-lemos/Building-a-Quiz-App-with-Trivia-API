GOAL
Running the program will display the original quiz application in the console. You can type "true" or "false" to answer questions, and the program will provide feedback on whether your answer was correct or incorrect, along with your current score.

Key Takeaways
The project upgrades a text-based quiz to fetch questions dynamically from the Open Trivia Database API.
The API request uses parameters to specify the number of questions and question type.
The fetched data replaces hard-coded questions to provide varied quiz content each run.
The program maintains compatibility with existing code by using the same variable names for question data.

Implemented on-screen feedback by changing the canvas background color to green or red based on correct or incorrect answers.
Used the window.after method in Tkinter to delay actions without freezing the GUI.
Added score keeping by updating the score label dynamically after each question.
Handled end-of-quiz scenarios by disabling buttons and updating the canvas to indicate quiz completion.