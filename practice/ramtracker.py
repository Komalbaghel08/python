import psutil
import time
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def system_monitor():
    try:
        while True:
            clear_screen()

            cpu = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory()

            print("🖥️ SYSTEM MONITOR")
            print("-" * 30)
            print(f"CPU Usage     : {cpu}%")
            print(f"RAM Usage     : {memory.percent}%")
            print(f"Total Memory  : {round(memory.total / (1024**3), 2)} GB")
            print(f"Available RAM : {round(memory.available / (1024**3), 2)} GB")

            time.sleep(1)

    except KeyboardInterrupt:
        print("\n👋 Exiting monitor...")


if __name__ == "__main__":
    system_monitor()