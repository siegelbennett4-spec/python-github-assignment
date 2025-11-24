# ---------------------------------------------
# Study Time Tracker Program
# A simple program that estimates your weekly
# study time based on your daily number.
# ---------------------------------------------

print("Welcome to my Python program!")

# --- Ask the user for input (Task 2) ---
daily_hours = input("How many hours did you study today? ")

# --- Convert input & perform calculation (Task 3) ---
try:
    daily_hours = float(daily_hours)  # convert to number

    weekly_hours = daily_hours * 7    # estimate weekly study hours

# --- Error handling (Task 5) ---
except ValueError:
    print("Please enter a valid number.")
    exit()

# --- Display result clearly (Task 4) ---
print(f"You are on track to study approximately {weekly_hours} hours this week!")

# --- Final cleanup & comments complete (Task 6) ---
 