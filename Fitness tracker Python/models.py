from datetime import datetime


class FitnessTracker:

    def __init__(self, user_name, goal_calories):
        self.user_name = user_name
        self.goal_calories = goal_calories
        self.workouts = []

    def add_workout(self, activity, duration_minutes, calories_burned):
        date_now = datetime.now().strftime("%Y-%m-%d %H:%M")

        workout = {
            "date": date_now,
            "activity": activity,
            "duration_minutes": duration_minutes,
            "calories_burned": calories_burned
        }

        self.workouts.append(workout)
        print("Тренировката " + activity + " е добавена успешно.")

    def total_calories_burned(self):
        total = 0
        for workout in self.workouts:
            total = total + workout["calories_burned"]
        return total

    def total_duration(self):
        total = 0
        for workout in self.workouts:
            total = total + workout["duration_minutes"]
        return total

    def sort_by_calories(self):
        sorted_list = []
        remaining = list(self.workouts)

        while len(remaining) > 0:
            best = remaining[0]
            for workout in remaining:
                if workout["calories_burned"] > best["calories_burned"]:
                    best = workout
            sorted_list.append(best)
            remaining.remove(best)

        return sorted_list

    def filter_by_activity(self, activity):
        result = []
        for workout in self.workouts:
            if workout["activity"] == activity:
                result.append(workout)
        return result

    def goal_reached(self):
        total = self.total_calories_burned()
        if total >= self.goal_calories:
            return True
        else:
            return False

    def print_summary(self):
        print("")
        print("")
        print("СПРАВКА ЗА: " + self.user_name)
        print("")
        print("Брой тренировки : " + str(len(self.workouts)))
        print("Общо минути     : " + str(self.total_duration()))
        print("Общо калории    : " + str(self.total_calories_burned()))
        print("Цел             : " + str(self.goal_calories) + " кал.")

        if self.goal_reached() == True:
            print("Целта е ПОСТИГНАТА!")
        else:
            remaining = self.goal_calories - self.total_calories_burned()
            print("Остават още: " + str(remaining) + " кал.")

        print("")
        
