Task = input("Enter your task: ")
Priority = input("Priority (high/medium/low): ").lower()
Time_Bound = input("Is it Time-Bound? (yes/no): ").lower()

match Priority:
    case "high":
        reminder = f"'{Task}' is a high priority task"
    case "medium":
        reminder = f"'{Task}' is a medium priority task"
    case "low":
        reminder = f"'{Task}' is a low priority task"
        
if Time_Bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."
# Provide a Customized Reminder
print(f"{reminder}")    
