class IntelligentTutor:
    def __init__(self):
        self.student_progress = 0
        self.current_activity = 0
        self.activities = [
            "Activity 1: Identify Climate Change Factors",
            "Activity 2: Plan Energy Conservation Strategy",
            "Activity 3: Reduce Plastic Usage"
        ]
    
    def start_tutorial(self):
        print("Welcome to the Intelligent Tutor System!")
        print("Let's develop your probtemplates/activity/High/Global/Activo/activity1lem-solving skills related to climate change.")
        self._display_activity()
    
    def _display_activity(self):
        if self.current_activity < len(self.activities):
            print("\nCurrent Activity:", self.activities[self.current_activity])
            self._provide_guidance()
        else:
            print("\nCongratulations! You've completed all activities.")
    
    def _provide_guidance(self):
        
        activity_info = {
            0: "Analyze different factors contributing to climate change.",
           #1: "Plan a strategy to reduce energy consumption at home.",
            #2: "Devise a plan to minimize plastic usage in your daily life."
        }
        
        print("Guidance:", activity_info.get(self.current_activity, "No guidance available."))
        self._simulate_student_interaction()
    
    def _simulate_student_interaction(self):
        print("Simulating student interaction...")
        # Here, you can simulate the student's decisions and actions.
        # You would provide feedback based on their choices and update progress.
        self.student_progress += 10
        self.current_activity += 1
        self._display_activity()
        
        
        
        
class LearningGoals:
    def __init__(self):
        self.goals = {
            "ClimateChangeFactors": {
                "levels": {
                    "Low": [
                        {"name": "Activity 1", "completed": False},
                        {"name": "Activity 2", "completed": False},
                        {"name": "Activity 3", "completed": False}
                    ],
                    "Medium": [
                        {"name": "Activity 10", "completed": False},
                        {"name": "Activity 11", "completed": False},
                        {"name": "Activity 12", "completed": False}
                    ],
                    "High": [
                        {"name": "Activity 19", "completed": False},
                        {"name": "Activity 20", "completed": False},
                        {"name": "Activity 21", "completed": False}
                    ]
                }
            },

            "EnergyConservation": {
                "levels": {
                    "Low": [
                        {"name": "Activity 4", "completed": False},
                        {"name": "Activity 5", "completed": False},
                        {"name": "Activity 6", "completed": False}
                    ],
                    "Medium": [
                        {"name": "Activity 13", "completed": False},
                        {"name": "Activity 14", "completed": False},
                        {"name": "Activity 15", "completed": False}
                    ],
                    "High": [
                        {"name": "Activity 22", "completed": False},
                        {"name": "Activity 23", "completed": False},
                        {"name": "Activity 24", "completed": False}
                    ]
                }
            },

            "PlasticReduction": {
                "levels": {
                    "Low": [
                        {"name": "Activity 7", "completed": False},
                        {"name": "Activity 8", "completed": False},
                        {"name": "Activity 9", "completed": False}
                    ],
                    "Medium": [
                        {"name": "Activity 16", "completed": False},
                        {"name": "Activity 17", "completed": False},
                        {"name": "Activity 18", "completed": False}
                    ],
                    "High": [
                        {"name": "Activity 25", "completed": False},
                        {"name": "Activity 26", "completed": False},
                        {"name": "Activity 27", "completed": False}
                    ]
                }
            }
        }  
    
    def mark_activity_completed(self, activity_name):
        for goal in self.goals.values():
            for level_activities in goal["levels"].values():
                for activity in level_activities:
                    if activity["name"] == activity_name:
                        activity["completed"] = True
    
    def recommend_learning_path(self):
        recommended_path = []
        for goal_name, goal_data in self.goals.items():
            for level_name, level_activities in goal_data["levels"].items():
                for activity in level_activities:
                    if not activity["completed"]:
                        recommended_path.append({
                            "goal": goal_name,
                            "level": level_name,
                            "activity": activity["name"]
                    })
        return recommended_path

    
    def print_learning_goals(self):
        print("Learning Goals:")
        for goal_name, goal_data in self.goals.items():
            print(f"- {goal_name}:")
            for level, level_activities in goal_data["levels"].items():
                print(f"  {level} Level:")
                for activity in level_activities:
                    status = "Completed" if activity["completed"] else "Not Completed"
                    print(f"    {activity['name']}: {status}")
            print()


    def calculate_learning_style_score(self, selected_styles):
        styles_data = {
            'style_1': {
                'Activo': 0,
                'Reflexivo': 0
        },
            'style_2': {
                'Sensorial': 0,
                'Intuitivo': 0
        },
            'style_3': {
                'Visual': 0,
                'Verbal': 0
        },
            'style_4': {
                'Secuencial': 0,
                'Global': 0
        },
    }

        results = []

        for question, data in selected_styles.items():
            style, response = data['style'], data['response']
            first_style, second_style = style.split('/')
            styles_key = None
        
            if 'Activo' in style and 'Reflexivo' in style:
                styles_key = 'style_1'
            elif 'Sensorial' in style and 'Intuitivo' in style:
                styles_key = 'style_2'
            elif 'Visual' in style and 'Verbal' in style:
                styles_key = 'style_3'
            elif 'Secuencial' in style and 'Global' in style:
                styles_key = 'style_4'
        
            if styles_key is not None:
                if response == 'a':
                    styles_data[styles_key][first_style] += 1
                elif response == 'b':
                    styles_data[styles_key][second_style] += 1
    
        for style_key, style_scores in styles_data.items():
            style_difference = max(style_scores.values()) - min(style_scores.values())
            dominant_style = max(style_scores, key=style_scores.get)
            results.append({'style': style_key, 'dominant_style': dominant_style, 'subtraction': style_difference})
            
        return results

        
        

# Main program
if __name__ == "__main__":
    tutor = IntelligentTutor()
    tutor.start_tutorial()
    learning_goals = LearningGoals()
    learning_goals.recommend_learning_path()
    learning_goals.print_learning_goals()













