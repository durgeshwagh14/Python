import time

def countdown_timer():
    total_seconds = int(input("⏱️ Enter countdown time in seconds: "))

    for remaining in range(total_seconds, 0, -1):
        mins, secs = divmod(remaining, 60)
        timer_display = f"{mins:02d}:{secs:02d}"
        print(f"⏳ Time left: {timer_display}", end='\r')
        time.sleep(1)

    print("\n🎉 Time's up! ⏰")

# Run the countdown timer
countdown_timer()
