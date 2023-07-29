import time

def start_pomodoro_timer(minutes):
    seconds * 60
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer_display = f"{mins:02d}:{secs:02d}"
        print(timer_display, end='\r')
        time.sleep(1)
        seconds -= 1
    
    print("Time's up! Take a break.")

# 使用示例：运行一个 25 分钟的专注时钟
start_pomodoro_timer(25)
