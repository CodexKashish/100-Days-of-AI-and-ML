import numpy as np

study_hours = np.array([2, 3, 4, 5, 6])
gpa = np.array([7.2, 7.5, 8.1, 8.8, 9.2])

slope, intercept = np.polyfit(study_hours, gpa, 1)

future_study_time = 8
predicted_gpa = (slope * future_study_time) + intercept

print(f"Trend: For every 1 hour of study, GPA increases by {slope:.2f}")
print(f"Prediction: Studying {future_study_time} hours could lead to a {predicted_gpa:.2f} GPA!")
