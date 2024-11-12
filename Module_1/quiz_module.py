# quiz_module.py
import requests
import json
import ipywidgets as widgets
from IPython.display import display
import random

class MatchingQuiz:
    def __init__(self, import_type:str, import_path:str, instant_feedback=False, shuffle_questions=False, shuffle_answers=False):
        self.questions = []
        self.answers = {}
        self.user_answers = []
        self.feedback_labels = []
        self.instant_feedback = instant_feedback
        self.shuffle_questions = shuffle_questions
        self.shuffle_answers = shuffle_answers
        self.distractors = []
        self.explanations = {}
        self.load_questions_from_json(import_type, import_path)

    def load_questions_from_json(self, import_type, import_path):
        if import_type == 'json':
            # Load the JSON file
            with open(import_path, 'r') as f:
                data = json.load(f)
        
        elif import_type == 'url':
            res = requests.get(import_path)
            data = res.json()
        
        else:
            print("Invalid parameter value, import_type must be a str value equal to 'json' or 'url'.")
            
        # Extract questions, answers, and explanations
        for item in data["questions"]:
            question = item["question"]
            answer = item["answer"]
            explanation = item.get("explanation", "No explanation provided.")
            self.questions.append((question, answer))
            self.answers[question] = answer
            self.explanations[question] = explanation

    def setup_quiz(self):
        # Optionally shuffle questions
        questions = self.questions[:]
        if self.shuffle_questions:
            random.shuffle(questions)

        # Clear previous user answers and feedback labels
        self.user_answers = []
        self.feedback_labels = []

        # Display each question with a dropdown for selecting the answer
        question_widgets = []
        for i, (question, correct_answer) in enumerate(questions):
            # Create answer options with distractors
            answer_options = list(self.answers.values()) + self.distractors
            if self.shuffle_answers:
                random.shuffle(answer_options)

            # Create the label, dropdown, and feedback label
            question_label = widgets.Label(value=question)
            answer_dropdown = widgets.Dropdown(options=['--Select--'] + answer_options)
            feedback_label = widgets.Label(value="")
            
            # Store reference to each dropdown and its corresponding feedback label
            self.user_answers.append(answer_dropdown)
            self.feedback_labels.append(feedback_label)
            
            question_widgets.append(widgets.HBox([question_label, answer_dropdown, feedback_label]))

            # Define the dropdown change event for instant feedback
            def on_answer_change(change, answer_dropdown=answer_dropdown, feedback_label=feedback_label, correct_answer=correct_answer):
                if self.instant_feedback and change['name'] == 'value':
                    selected_answer = answer_dropdown.value
                    if selected_answer == correct_answer:
                        feedback_label.value = "✔️"  # Checkmark for correct
                        feedback_label.layout.color = 'green'
                    elif selected_answer == '--Select--':
                        feedback_label.value = ""  # Reset for no selection
                    else:
                        feedback_label.value = "❌"  # Cross for incorrect
                        feedback_label.layout.color = 'red'
            
            # Link the dropdown to the feedback event
            answer_dropdown.observe(on_answer_change, names='value')

        # Create a button to check answers
        check_button = widgets.Button(description="Check Answers")
        reset_button = widgets.Button(description="Reset Quiz")
        result_label = widgets.HTML(value="")

        # Define the button click event for "Check Answers"
        def on_check_button_click(b):
            correct = 0
            explanations_output = ""
            
            for i, (question, _) in enumerate(questions):
                selected_answer = self.user_answers[i].value
                if selected_answer == self.answers[question]:
                    correct += 1
                else:
                    # Add explanation for incorrect answers
                    explanation = self.explanations.get(question, "No explanation provided.")
                    explanations_output += f"<li>{question}: {explanation}</li>"
            
            # Update the result label with color based on the score
            if correct == len(questions):
                result_label.value = f"<span style='color: green; font-weight: bold;'>✔️ Correct!</span>"
            else:
                result_label.value = f"<span style='color: red; font-weight: bold;'>❌ Incorrect! Try again.</span>"
                result_label.value += f"<br><ul>{explanations_output}</ul>"
        
        # Define the button click event for "Reset Quiz"
        def on_reset_button_click(b):
            for dropdown, feedback in zip(self.user_answers, self.feedback_labels):
                dropdown.value = '--Select--'
                feedback.value = ""
            result_label.value = ""

        check_button.on_click(on_check_button_click)
        reset_button.on_click(on_reset_button_click)

        # Display all components
        display(widgets.VBox(question_widgets + [check_button, reset_button, result_label]))

# Function to create and run the quiz
def run_quiz(import_type, import_path, instant_feedback=False, shuffle_questions=False, shuffle_answers=False):
    quiz = MatchingQuiz(import_type, import_path, instant_feedback, shuffle_questions, shuffle_answers)
    quiz.setup_quiz()
