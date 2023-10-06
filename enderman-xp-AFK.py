import pynput.mouse
import keyboard
import time
import threading


###########NOT WORKING YET###########



program_running = False
def move_mouse():
    global program_running
    mouse = pynput.mouse.Controller()

    while True:
        if program_running:
            for i in range(40):
                mouse.move(i, 0)
                time.sleep(0.01)
            for i in range(40):
                mouse.move(-i, 0)
                time.sleep(0.01)


        else:
            time.sleep(0.01)

def toggle_program_state(e):
    global program_running
    program_running = not program_running
    print("Program is now", "on" if program_running else "off")

mouse_thread = threading.Thread(target=move_mouse)
mouse_thread.daemon = True
mouse_thread.start()

keyboard.on_press_key("F6", toggle_program_state)

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    pass
