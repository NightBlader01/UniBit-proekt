from models import FitnessTracker


tracker = FitnessTracker("Иван Петров", 1000)


tracker.add_workout("Бягане", 30, 320)
tracker.add_workout("Колело", 45, 410)
tracker.add_workout("Плуване", 60, 500)
tracker.add_workout("Йога", 50, 180)
tracker.add_workout("Вдигане тежести", 40, 280)


tracker.print_summary()


print("Всички тренировки:")
for workout in tracker.workouts:
    print("- " + workout["activity"] + " | " + str(workout["calories_burned"]) + " кал.")


print("")
print("Наредени по калории (от най-много):")
sorted_workouts = tracker.sort_by_calories()
for workout in sorted_workouts:
    print("- " + workout["activity"] + " | " + str(workout["calories_burned"]) + " кал.")


print("")
print("Само тренировките Бягане:")
running_workouts = tracker.filter_by_activity("Бягане")
if len(running_workouts) == 0:
    print("Няма намерени тренировки.")
else:
    for workout in running_workouts:
        print("- " + workout["activity"] + " | " + str(workout["duration_minutes"]) + " мин.")


print("")
if tracker.goal_reached() == True:
    print("Целта е постигната!")
else:
    print("Целта още не е постигната.")
