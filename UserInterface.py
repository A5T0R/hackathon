import keyboard

def bind_movement_keys(c):
    keyboard.on_press_key("down",  lambda e:c.move(e),suppress=True)
    keyboard.on_press_key("up",    lambda e:c.move(e),suppress=True)
    keyboard.on_press_key("left",  lambda e:c.move(e),suppress=True)
    keyboard.on_press_key("right", lambda e:c.move(e),suppress=True)


    