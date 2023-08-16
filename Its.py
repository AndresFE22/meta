import mysql.connector

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
                    "low": [
                        {"name": "t1", "completed": False},
                        {"name": "t2", "completed": False},
                        {"name": "t3", "completed": False}
                    ],
                    "medium": [
                        {"name": "t10", "completed": False},
                        {"name": "t11", "completed": False},
                        {"name": "t12", "completed": False}
                    ],
                    "high": [
                        {"name": "t19", "completed": False},
                        {"name": "t20", "completed": False},
                        {"name": "t21", "completed": False}
                    ]
                }
            },

            "EnergyConservation": {
                "levels": {
                    "low": [
                        {"name": "t4", "completed": False},
                        {"name": "t5", "completed": False},
                        {"name": "t6", "completed": False}
                    ],
                    "medium": [
                        {"name": "t13", "completed": False},
                        {"name": "t14", "completed": False},
                        {"name": "t15", "completed": False}
                    ],
                    "high": [
                        {"name": "t22", "completed": False},
                        {"name": "t23", "completed": False},
                        {"name": "t24", "completed": False}
                    ]
                }
            },

            "PlasticReduction": {
                "levels": {
                    "low": [
                        {"name": "t7", "completed": False},
                        {"name": "t8", "completed": False},
                        {"name": "t9", "completed": False}
                    ],
                    "medium": [
                        {"name": "t16", "completed": False},
                        {"name": "t17", "completed": False},
                        {"name": "t18", "completed": False}
                    ],
                    "high": [
                        {"name": "t25", "completed": False},
                        {"name": "t26", "completed": False},
                        {"name": "t27", "completed": False}
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
                            "lvl": level_name,
                            "name": activity["name"]
                    })
        return recommended_path

    
    def print_learning_goals(self):
        print("Learning Goals:")
        for goal_name, goal_data in self.goals.items():
            print(f"- {goal_name}:")
            for level, level_activities in goal_data["levels"].items():
                print(f"  {level} lvl:")
                for activity in level_activities:
                    status = "Completed" if activity["completed"] else "Not Completed"
                    print(f"    {activity['name']}: {status}")
            print()


    def calculate_learning_style_score(self, selected_styles):
        styles_data = {
            'perception': {
                'Activo': 0,
                'Reflexivo': 0
        },
            'processing': {
                'Sensorial': 0,
                'Intuitivo': 0
        },
            'reception': {
                'Visual': 0,
                'Verbal': 0
        },
            'nav': {
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
                styles_key = 'perception'
            elif 'Sensorial' in style and 'Intuitivo' in style:
                styles_key = 'processing'
            elif 'Visual' in style and 'Verbal' in style:
                styles_key = 'reception'
            elif 'Secuencial' in style and 'Global' in style:
                styles_key = 'nav'
        
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
    
class LearningResource:
    def __init__(self, host, user, password, database):
        try:
            self.connection = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
            print("Connected to database successfully")
            self.cursor = self.connection.cursor(buffered=True)
        except mysql.connector.Error as err:
            print("Error connecting to database:", err)
                

    
    def find_resource(self, recommended_path, combined_styles):
        results = []
        pt_values = []
        

        for entry in recommended_path:
            name = entry['name']
            goal = entry['goal']
            lvl = entry['lvl']
            query = (
                "SELECT url, pt, lc FROM learningresource "
                "WHERE name= %s AND goal= %s AND lvl= %s"
            )
            print("voy por las de", name, goal, lvl)
            values = (name, goal, lvl)
            self.cursor.execute(query, values)
            results_for_entry = self.cursor.fetchall()
            print('result', results_for_entry)

            for result in results_for_entry: 
                url, pt, lc = result
                resource_info = {
                    "name": name,
                    "goal": goal,
                    "lvl": lvl,
                    "url": url,
                    "pt": pt,
                    "lc": lc
            }
                results.append(resource_info)
            else:
            
                print("No resource found for:", name, goal, lvl)
        
        combined_style_values = [(style, dominant_style) for style, dominant_style in (cs.split(': ') for cs in combined_styles)]

        for combined_style_value in combined_style_values:
            style, dominant_style = combined_style_value
            pt_values.append(dominant_style)

        style_query = (
            "SELECT pt FROM learningstyle "
            "WHERE perception = %s AND processing = %s AND reception = %s"
        )

        values_styles = (pt_values[1], pt_values[0], pt_values[2])
        print("values styles", values_styles)
        self.cursor.execute(style_query, values_styles)
        results_style_for_entry = self.cursor.fetchall()
        print("result", results_style_for_entry)

        print('pedagogic_tactic:', pt_values)
        style_result_flat = [item[0] for item in results_style_for_entry]
        print('flat', style_result_flat)


        filtered_styles = [resource for resource in results if resource['pt'] in style_result_flat]

        level_order = {'low': 0, 'medium': 1, 'high': 2}
        ordered_resources = sorted(filtered_styles, key=lambda x: level_order[x['lvl']])



        print("Final resources", ordered_resources)

        return ordered_resources
    
    def close_connection(self):
        self.cursor.close()
        self.connection.close()


        
        

# Main program
if __name__ == "__main__":
    tutor = IntelligentTutor()
    tutor.start_tutorial()
    learning_goals = LearningGoals()
    learning_goals.recommend_learning_path()
    learning_goals.print_learning_goals()
    Learning_Resource = LearningResource()
    Learning_Resource.find_resource











