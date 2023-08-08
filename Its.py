class IntelligentTutor:
    def __init__(self):
        self.student_progress = 0
        self.current_activity = 0
        self.activities = [
            "Activity 1: Identify Climate Change Factors",
            #"Activity 2: Plan Energy Conservation Strategy",
            #"Activity 3: Reduce Plastic Usage"
        ]
    
    def start_tutorial(self):
        print("Welcome to the Intelligent Tutor System!")
        print("Let's develop your problem-solving skills related to climate change.")
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
                "description": "Analyze different factors contributing to climate change.",
                "activities": [
                    {"name": "Activity 1", "completed": False},
                   # {"name": "Activity 4", "completed": False},
                    #{"name": "Activity 7", "completed": False}
                ]
            },
        }
    
    def mark_activity_completed(self, activity_name):
        for goal in self.goals.values():
            for activity in goal["activities"]:
                if activity["name"] == activity_name:
                    activity["completed"] = True
    
    def recommend_learning_path(self):
        recommended_path = []
        for goal_name, goal_data in self.goals.items():
            for activity in goal_data["activities"]:
                if not activity["completed"]:
                    recommended_path.append(activity["name"])
                    break
        return recommended_path
    
    def print_learning_goals(self):
        print("Learning Goals:")
        for goal_name, goal_data in self.goals.items():
            print(f"- {goal_name}:")
            print(f"  Description: {goal_data['description']}")
            print("  Activities:")
            for activity in goal_data["activities"]:
                status = "Completed" if activity["completed"] else "Not Completed"
                print(f"    {activity['name']}: {status}")
            print()

        
        

# Main program
if __name__ == "__main__":
    tutor = IntelligentTutor()
    tutor.start_tutorial()
    learning_goals = LearningGoals()
    learning_goals.recommend_learning_path()
    learning_goals.print_learning_goals()













