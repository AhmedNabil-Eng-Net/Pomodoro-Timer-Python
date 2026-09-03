
# ------------- # -- Pomodoro Timer -- # ------------- #

import time


# Display the remaining time in MM:SS format
def clocker(total_secs):
    # Convert total seconds into minutes and remaining seconds
    mins = total_secs // 60
    secs = total_secs % 60

    # Format the time as two digits for minutes and seconds
    clock = f"⏳ Time Remaining: {mins:02d}:{secs:02d}"

    # Print the timer on the same line and update it every second
    print(f"\r{clock}", end="") # or print(clock)

    # Wait one second before the next update
    time.sleep(1)


# Display an invalid-time message with animation
def invalid_time():
    # Print the message three times with increasing dots
    for dots in range(1, 4):
        print(f"\r- Invalid Time!❌{'.' * dots}", end="")
        time.sleep(0.5)

    # Move to the next line after the animation finishes
    print()


# ------------------ # -- Main -- # ----------------- #

# Display the program title
print("⏳ Welcome to the Pomodoro Timer ⌛".center(37, "-"))

# Control the main program loop
loop = True

while loop:
    try:
        # Ask the user for the timer duration in minutes
        user_time = int(input("⏰ Enter your time (in mins): "))

        # Check if the entered time is zero or negative
        if user_time <= 0:
            invalid_time()

        else:
            # Convert the user's time from minutes to seconds
            total_secs = user_time * 60

            # Keep counting down until the timer reaches zero
            while total_secs > 0:
                clocker(total_secs)

                # Decrease the remaining time by one second
                total_secs -= 1

            # Stop the main loop after the timer finishes
            loop = False

            # Notify the user that the timer has finished
            print("\n- Time is Out!🔔")

    # Handle non-numeric input
    except ValueError:
        invalid_time()

#````````````````````````````````````````````````````````````#