from flask import Flask, render_template, request, jsonify, session, redirect, render_template_string
from Its import IntelligentTutor, LearningGoals, LearningResource
import json

app = Flask(__name__,
            static_folder='learning_resources',
            template_folder='templates')
app.secret_key = 'your_secret_key'

# Crea una instancia
learning_goals = LearningGoals()


@app.route('/')
def init():
    return render_template('index.html')

@app.route('/diagnosisrender')
def diagnosisState():
    return render_template('diagnosisState.html')

@app.route('/diagnosis', methods=['POST'])
def diagnosis_lowlvl():
    questions = [
        {"activity_name": "t1", "correct_answer": "a"},
        {"activity_name": "t2", "correct_answer": "c"},
        {"activity_name": "t3", "correct_answer": "a"},
        {"activity_name": "t4", "correct_answer": "d"},
        {"activity_name": "t5", "correct_answer": "a"},
        {"activity_name": "t6", "correct_answer": "d"},
        {"activity_name": "t7", "correct_answer": "b"},
        {"activity_name": "t8", "correct_answer": "b"},
        {"activity_name": "t9", "correct_answer": "c"},
        {"activity_name": "t10", "correct_answer": "a"},
        {"activity_name": "t11", "correct_answer": "c"},
        {"activity_name": "t12", "correct_answer": "a"},
        {"activity_name": "t13", "correct_answer": "d"},
        {"activity_name": "t14", "correct_answer": "a"},
        {"activity_name": "t15", "correct_answer": "d"},
        {"activity_name": "t16", "correct_answer": "b"},
        {"activity_name": "t17", "correct_answer": "b"},
        {"activity_name": "t18", "correct_answer": "c"},
        {"activity_name": "t19", "correct_answer": "a"},
        {"activity_name": "t20", "correct_answer": "c"},
        {"activity_name": "t21", "correct_answer": "a"},
        {"activity_name": "t22", "correct_answer": "d"},
        {"activity_name": "t23", "correct_answer": "a"},
        {"activity_name": "t24", "correct_answer": "d"},
        {"activity_name": "t25", "correct_answer": "b"},
        {"activity_name": "t26", "correct_answer": "b"},
        {"activity_name": "t27", "correct_answer": "c"}
    ]

    incorrect_activities = {}
    incorrect_answer = []
    
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
                print("Incorrect Answer for", activity_name)
                incorrect_activities[activity_name] = student_answer

    for activity_name, answer in incorrect_activities.items():
        incorrect_answer.append(activity_name)

            
        
    response = learning_goals.print_learning_goals()
    recommended_path = learning_goals.recommend_learning_path()
    
    session['recommended_path'] = recommended_path
    session['incorrect_activities'] = incorrect_answer

    return render_template('diagnosisStyles.html')
    

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

    session['results'] = results
    
    return render_template("responsestyles.html", results=results)


@app.route('/Activity', methods=['GET', 'POST'])
def activity():
    incorrect_activities = session.get('incorrect_activities')
    recommended_path = session.get('recommended_path')
    style_list_n = session.get('results')
    last_item = style_list_n.pop()
    style_list = style_list_n
    #nav_menu = last_item['dominant_style']
    nav_menu = 'Secuencial'
    #nav_menu = 'Global'




    combined_styles = []
    for entry in style_list:
        dominant_style = entry['dominant_style']
        style = entry['style']
        combined_style = f"{style}: {dominant_style}"
        combined_styles.append(combined_style)
        
    print("style", style_list, "nav", nav_menu, "combined", combined_styles)

    Learning_Resource = LearningResource('localhost', 'root', '', 'climate')
    
    resource_list = Learning_Resource.find_resource(recommended_path, combined_styles)
    print("list", resource_list)

    for resource in resource_list:
        print("Activity:", resource["name"])
        print("Goal:", resource["goal"])
        print("Level:", resource["lvl"])
        print("URL:", resource["url"])
        print("PT:", resource["pt"])
        print("LC:", resource["lc"])

    Learning_Resource.close_connection()

    print('incorrect_activities', incorrect_activities)

    
    incorrect_activities.append('send')
    data_sequential = render_template("ActivitySequential.html", resources=resource_list)
    data_global = render_template("ActivityGlobal.html", resources=resource_list)
    data_incorrect_answer = render_template('diagnosisStateEvaluation.html', incorrect_activities=incorrect_activities )
    print("icorrect:", data_incorrect_answer)


    return render_template('activity.html', nav_menu=nav_menu, data_sequential=data_sequential, data_global=data_global, data_incorrect_answer=data_incorrect_answer)


if __name__ == '__main__':
    app.run(debug=True)
