import keyboard

def bind_movement_keys():
    keyboard.on_press_key("down", lambda _:print("pressed down"),suppress=True)


    