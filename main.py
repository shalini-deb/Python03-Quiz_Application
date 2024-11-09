import tkinter as tk
from tkinter import messagebox

# List of questions, options, and correct answers
quiz_data = [
    {
        "question": "Who was the fourth Prime Minister of India?",
        "options": ["Jawaharlal Nehru", "Mahatma Gandhi", "Lal Bahadur Shastri", "Moraji Desai"],
        "answer": "Moraji Desai"
    },
    {
        "question": "What is the danceform of Tamil Nadu?",
        "options": ["Kathak", "Mohiniyattam", "Kuchipudi", "Bharatnatyam"],
        "answer": "All of the above"
    },
    {
        "question": "Which year was Python created?",
        "options": ["1995", "1991", "1985", "2000"],
        "answer": "1991"
    },
    {
        "question": "How many states are there in India?",
        "options": ["29", " 21", " 27", " 28"],
        "answer": "28"
    }
]

# Function to start the quiz and load the first question
def start_quiz(state, question_label, option_buttons):
    state["score"] = 0
    state["question_index"] = 0
    show_question(state, question_label, option_buttons)

# Function to display the current question
def show_question(state, question_label, option_buttons):
    question_index = state["question_index"]
    question = quiz_data[question_index]["question"]
    options = quiz_data[question_index]["options"]
    
    question_label.config(text=question)
    
    # Clear previous options and update buttons
    for i in range(len(options)):
        option_buttons[i].config(text=options[i], command=lambda opt=options[i]: check_answer(opt, state, question_label, option_buttons))

# Function to check the answer
def check_answer(selected_answer, state, question_label, option_buttons):
    correct_answer = quiz_data[state["question_index"]]["answer"]
    
    if selected_answer == correct_answer:
        state["score"] += 1
        messagebox.showinfo("Correct!", "Correct answer!")
    else:
        messagebox.showerror("Incorrect", f"Incorrect! The correct answer is: {correct_answer}")
    
    # Move to the next question
    state["question_index"] += 1
    
    if state["question_index"] < len(quiz_data):
        show_question(state, question_label, option_buttons)
    else:
        messagebox.showinfo("Quiz Finished", f"Quiz finished! Your score is: {state['score']}/{len(quiz_data)}")
        root.quit()  # Close the app

# Create the tkinter window
root = tk.Tk()
root.title("Python Quiz App")

# Dictionary to store the state (score and question index)
state = {"score": 0, "question_index": 0}

# Create a label for the question
question_label = tk.Label(root, text="", font=("Helvetica", 16), width=50, height=2)
question_label.pack(pady=20)

# Create buttons for the options
option_buttons = [tk.Button(root, text="", font=("Helvetica", 14), width=20, height=2) for _ in range(4)]

# Pack the buttons
for button in option_buttons:
    button.pack(pady=5)

# Start Button to begin the quiz
start_button = tk.Button(root, text="Start Quiz", font=("Helvetica", 16), width=20, height=2, command=lambda: start_quiz(state, question_label, option_buttons))
start_button.pack(pady=20)

# Run the tkinter event loop
root.mainloop()
