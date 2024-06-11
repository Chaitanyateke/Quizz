import random

# Function to read questions from the text file
def read_questions(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        questions = []
        current_question = {}
        for line in lines:
            line = line.strip()
            if line.startswith("Question"):
                if current_question:
                    questions.append(current_question)
                current_question = {'question': line[len("Question"):].strip()}
            elif line.startswith(("A)", "B)", "C)", "D)")):
                option, text = line.split(")", 1)
                current_question[option.strip()] = text.strip()
            elif line.startswith("Correct Answer:"):
                current_question['correct_answer'] = line.split(":")[1].strip()
        if current_question:
            questions.append(current_question)
    return questions

# Function to generate HTML code for questions
def generate_html(questions):
    html = ""
    for idx, question in enumerate(questions, 1):
        html += f"<div class='question'>\n"
        html += f"<p>{idx}. {question['question']}</p>\n"
        for option, text in question.items():
            if option in ['A)', 'B)', 'C)', 'D)']:
                html += f"<label><input type='radio' name='q{idx}' value='{option}' /> {text}</label><br />\n"
        html += "</div>\n"
    return html

# Main function
def main():
    file_path = 'basic_c.txt'
    # file_path = 'questions.txt'
    num_questions = 5  # Change this to the number of questions you want to display
    
    # Read questions from the file
    questions = read_questions(file_path)
    
    # Check if the number of questions available is sufficient
    if len(questions) < num_questions:
        print("Error: Not enough questions available.")
        return
    
    # Select random questions
    selected_questions = random.sample(questions, num_questions)
    
    # Generate HTML code for selected questions
    html_code = generate_html(selected_questions)
    
    # Write the HTML code to an HTML file
    with open('quiz.html', 'w') as html_file:
        html_file.write("<!DOCTYPE html>\n<html>\n<head>\n<title>MCQ Quiz</title>\n</head>\n<body>\n")
        html_file.write(html_code)
        html_file.write("</body>\n</html>")

if __name__ == "__main__":
    main()
