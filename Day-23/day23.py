import html
import tkinter as tk
import requests


# ---------------------------- API & DATA ------------------------------- #

def fetch_questions():
    """Fetch 10 true/false trivia questions from the Open Trivia Database."""
    url = "https://opentdb.com/api.php?amount=10&type=boolean"

    response = requests.get(url)
    response.raise_for_status()

    data = response.json()
    return data["results"]


# ---------------------------- QUIZ BRAIN ------------------------------- #

class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1

        # Unescape HTML entities
        q_text = html.unescape(self.current_question["question"])

        return f"Q.{self.question_number}: {q_text}"

    def check_answer(self, user_answer):
        correct_answer = self.current_question["correct_answer"]

        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True

        return False


# ---------------------------- GUI INTERFACE ------------------------------- #

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain):
        self.quiz = quiz_brain

        self.window = tk.Tk()
        self.window.title("Day 34: Trivia Quiz App")
        self.window.config(
            padx=20,
            pady=20,
            bg=THEME_COLOR
        )

        # Score Label
        self.score_label = tk.Label(
            text="Score: 0",
            fg="white",
            bg=THEME_COLOR,
            font=("Arial", 12)
        )
        self.score_label.grid(
            row=0,
            column=1,
            pady=10
        )

        # Canvas for Question Display
        self.canvas = tk.Canvas(
            width=300,
            height=250,
            bg="white"
        )

        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Question text goes here...",
            fill=THEME_COLOR,
            font=("Arial", 14, "italic")
        )

        self.canvas.grid(
            row=1,
            column=0,
            columnspan=2,
            pady=20
        )

        # TRUE Button
        self.true_btn = tk.Button(
            text="TRUE",
            fg="white",
            bg="#2ecc71",
            font=("Arial", 12, "bold"),
            width=10,
            height=2,
            command=self.true_pressed
        )

        self.true_btn.grid(
            row=2,
            column=0,
            padx=10
        )

        # FALSE Button
        self.false_btn = tk.Button(
            text="FALSE",
            fg="white",
            bg="#e74c3c",
            font=("Arial", 12, "bold"),
            width=10,
            height=2,
            command=self.false_pressed
        )

        self.false_btn.grid(
            row=2,
            column=1,
            padx=10
        )

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")

        if self.quiz.still_has_questions():

            self.score_label.config(
                text=f"Score: {self.quiz.score}"
            )

            q_text = self.quiz.next_question()

            self.canvas.itemconfig(
                self.question_text,
                text=q_text
            )

            self.true_btn.config(state="normal")
            self.false_btn.config(state="normal")

        else:

            self.canvas.itemconfig(
                self.question_text,
                text=(
                    f"You've reached the end of the quiz!\n\n"
                    f"Final Score: "
                    f"{self.quiz.score}/"
                    f"{len(self.quiz.question_list)}"
                )
            )

            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(
            self.quiz.check_answer("True")
        )

    def false_pressed(self):
        self.give_feedback(
            self.quiz.check_answer("False")
        )

    def give_feedback(self, is_correct):

        self.true_btn.config(state="disabled")
        self.false_btn.config(state="disabled")

        if is_correct:
            self.canvas.config(bg="#2ecc71")
        else:
            self.canvas.config(bg="#e74c3c")

        self.window.after(
            1000,
            self.get_next_question
        )


# ---------------------------- DRIVER CODE ------------------------------- #

if __name__ == "__main__":

    raw_questions = fetch_questions()

    quiz = QuizBrain(raw_questions)

    quiz_ui = QuizInterface(quiz)
