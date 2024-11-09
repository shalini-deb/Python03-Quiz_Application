# Quiz Application with Tkinter

This is a simple multiple-choice quiz application built using Python's `tkinter` library. The app features a clean and intuitive GUI where users can answer questions, receive feedback, and track their progress. At the end of the quiz, users can see their final score.

## Features

- **Simple GUI:** A clean and user-friendly interface built with tkinter, allowing users to interact easily with the quiz.
- **Multiple Choice Questions:** Users are presented with multiple-choice questions, each having four answer options to choose from.
- **Real-Time Scoring:** The score is updated after each question based on whether the user's selected answer is correct.
- **Feedback Messages:** After each answer, a pop-up message box provides feedback, showing whether the answer was correct or incorrect. If incorrect, the correct answer is displayed.
- **Final Score:** At the end of the quiz, users are shown their score out of the total number of questions.
- **Quiz Navigation:** Users can progress through the questions by selecting answers, and the app automatically moves to the next question after each answer.

## Code Explanation

### Quiz Data Structure

The quiz questions, answer options, and correct answers are stored in a list called `quiz_data`. Each item in `quiz_data` is a dictionary containing:

- **question:** A string representing the question text.
- **options:** A list of four possible answer choices.
- **answer:** The correct answer for that question.

### Functions

- **`start_quiz(state, question_label, option_buttons)`**
  - Initializes the score and question index to 0 when the quiz is started.
  - Calls the `show_question()` function to display the first question.

- **`show_question(state, question_label, option_buttons)`**
  - Displays the current question and its available answer options on the window.
  - Updates the option buttons with the corresponding choices and binds the `check_answer` function to each button.

- **`check_answer(selected_answer, state, question_label, option_buttons)`**
  - Checks if the selected answer matches the correct answer from `quiz_data`.
  - If correct, the score is increased, and a success message is displayed.
  - If incorrect, the correct answer is shown with an error message.
  - The app then moves to the next question. Once all questions are answered, it shows the final score and ends the quiz.

### Tkinter Widgets

- **`question_label`:** A Label widget used to display the question text.
- **`option_buttons`:** A list of four Button widgets representing the answer choices. The buttons are updated with options for each question.
- **`start_button`:** A Button widget that starts the quiz when clicked.

### State Management

- **`state`:** A dictionary used to track the user's current score (`score`) and the index of the current question (`question_index`).

### App Flow

1. The app starts with the "Start Quiz" button. Once clicked, it initializes the score and question index and displays the first question.
2. After each question, the app waits for the user to select an answer. Once an answer is selected, the app checks if it is correct, updates the score, and displays feedback.
3. The quiz progresses to the next question after each answer. Once all questions are answered, the final score is displayed, and the app ends.

## Installation

To run the quiz app, you will need to have Python installed on your machine. You will also need the `tkinter` library, which is included with Python's standard library.

1. Clone or download the repository to your local machine.
2. Run the Python script to launch the application:

    ```bash
    python quiz_application.py
    ```

## Thank You

Thank you for using the Quiz Application! We hope this tool provides a fun and interactive way to test your knowledge.


