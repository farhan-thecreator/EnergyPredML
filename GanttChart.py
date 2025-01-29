import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta

# Define project tasks and durations
tasks = [
    ("Project Planning", "2024-01-29", "2024-02-11"),
    ("Data Collection & Preprocessing", "2024-02-12", "2024-03-10"),
    ("Feature Engineering & Selection", "2024-03-11", "2024-03-24"),
    ("Model Selection & Training", "2024-03-25", "2024-04-21"),
    ("Evaluation & Testing", "2024-04-22", "2024-05-05"),
    ("Deployment & Implementation", "2024-05-06", "2024-05-19"),
    ("Final Report & Presentation", "2024-05-20", "2024-06-02")
]

# Adjust dates to fit the April 1st deadline
tasks = [
    ("Project Planning", "2024-01-29", "2024-02-04"),
    ("Data Collection & Preprocessing", "2024-02-05", "2024-02-25"),
    ("Feature Engineering & Selection", "2024-02-26", "2024-03-03"),
    ("Model Selection & Training", "2024-03-04", "2024-03-17"),
    ("Evaluation & Testing", "2024-03-18", "2024-03-24"),
    ("Deployment & Implementation", "2024-03-25", "2024-03-31"),
    ("Final Report & Presentation", "2024-04-01", "2024-04-07")
]

# Convert to DataFrame
df = pd.DataFrame(tasks, columns=["Task", "Start", "End"])
df["Start"] = pd.to_datetime(df["Start"])
df["End"] = pd.to_datetime(df["End"])

# Plot Gantt chart
fig, ax = plt.subplots(figsize=(10, 5))
for i, (task, start, end) in enumerate(zip(df["Task"], df["Start"], df["End"])):
    ax.barh(task, (end - start).days, left=start, color="skyblue")

# Format x-axis
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %d"))
ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))
plt.xticks(rotation=45)
plt.xlabel("Timeline")
plt.ylabel("Tasks")
plt.title("Gantt Chart - Machine Learning Project")

# Show plot
plt.tight_layout()
plt.show()
