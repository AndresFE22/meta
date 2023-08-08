from flask import Flask, render_template, request, jsonify
from Its import IntelligentTutor

app = Flask(__name__)

@app.route('/')
def init():
    
    return render_template('index.html')


@app.route('/diagnosis')
def diagnosis():
    
    return render_template('diagnosis.html')

@app.route('/activity1', methods=['POST'])
def diagnosis():
    
    tutor = IntelligentTutor()
    tutor._display_activity()

    
    return render_template('diagnosis.html')



