from flask import Flask, render_template, request, jsonify
from Its import IntelligentTutor, LearningGoals
import json

app = Flask(__name__)

# Crea una instancia de LearningGoals
learning_goals = LearningGoals()

@app.route('/')
def init():
    return render_template('index.html')

@app.route('/diagnosisrender')
def diagnosisState():
    return render_template('diagnosisState.html')

@app.route('/diagnosisStyles')
def diagnosisStyles():
    return render_template('diagnosisStyles.html')


@app.route('/diagnosis', methods=['POST'])
def diagnosis_lowlvl():
    questions = [
        {"activity_name": "Activity 1", "correct_answer": "a"},
        {"activity_name": "Activity 2", "correct_answer": "c"},
        {"activity_name": "Activity 3", "correct_answer": "a"},
        {"activity_name": "Activity 4", "correct_answer": "d"},
        {"activity_name": "Activity 5", "correct_answer": "a"},
        {"activity_name": "Activity 6", "correct_answer": "d"},
        {"activity_name": "Activity 7", "correct_answer": "b"},
        {"activity_name": "Activity 8", "correct_answer": "b"},
        {"activity_name": "Activity 9", "correct_answer": "c"},
        {"activity_name": "Activity 10", "correct_answer": "a"},
        {"activity_name": "Activity 11", "correct_answer": "c"},
        {"activity_name": "Activity 12", "correct_answer": "a"},
        {"activity_name": "Activity 13", "correct_answer": "d"},
        {"activity_name": "Activity 14", "correct_answer": "a"},
        {"activity_name": "Activity 15", "correct_answer": "d"},
        {"activity_name": "Activity 16", "correct_answer": "b"},
        {"activity_name": "Activity 17", "correct_answer": "b"},
        {"activity_name": "Activity 18", "correct_answer": "c"},
        {"activity_name": "Activity 19", "correct_answer": "a"},
        {"activity_name": "Activity 20", "correct_answer": "c"},
        {"activity_name": "Activity 21", "correct_answer": "a"},
        {"activity_name": "Activity 22", "correct_answer": "d"},
        {"activity_name": "Activity 23", "correct_answer": "a"},
        {"activity_name": "Activity 24", "correct_answer": "d"},
        {"activity_name": "Activity 25", "correct_answer": "b"},
        {"activity_name": "Activity 26", "correct_answer": "b"},
        {"activity_name": "Activity 27", "correct_answer": "c"}
    ]

    for i in range(1, 28):
        student_answer = request.form.get('student_answer' + str(i))

        if student_answer:
            question = questions[i - 1]
            activity_name = question['activity_name']

            if student_answer == question["correct_answer"]:
                print("Student Answer:", student_answer)
                print("Correct Answer for", activity_name)
                learning_goals.mark_activity_completed(activity_name)  
            else:
                activity_name = question['activity_name']
                print("Incorrect Answer for", activity_name)
        
    response = learning_goals.print_learning_goals()
    recommended_path = learning_goals.recommend_learning_path()

    return render_template('response.html', response=response, recommended_path=recommended_path)
    

@app.route('/test', methods=['POST'])
def testStyles():
    answers = request.form
        
    learning_styles = {
        'Activo/Reflexivo': [1, 5, 9, 13, 17],
        'Sensorial/Intuitivo': [2, 6, 10, 14, 18],
        'Visual/Verbal': [3, 7, 11, 15, 19],
        'Secuencial/Global': [4, 8, 12, 16, 20]
    }
    
    selected_styles = { }
    
    for ask, response in answers.items():
        ask_num = int(ask.lstrip('pregunta'))
        for style, asks in learning_styles.items():
            if ask_num in asks:
                selected_styles[ask_num] = {'style': style, 'response': response}
                break
                
    print(selected_styles)
    
    results = learning_goals.calculate_learning_style_score(selected_styles)
    print(results)

    for result in results:
        print(f"Estilo: {result['dominant_style']}, Resta: {result['subtraction']}")

    return render_template("responsestyles.html", results=results)



if __name__ == '__main__':
    app.run(debug=True)
