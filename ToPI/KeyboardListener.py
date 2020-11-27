from pynput import keyboard

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(key.char))
    except AttributeError:
        print('special key {0} pressed'.format(key))

        if key == keyboard.Key.up:
            up()
        elif key == keyboard.Key.down:
            down()
        elif key == keyboard.Key.right:
            right()
        elif key == keyboard.Key.left:
            left()

def up():
    print("***UP***")

def down():
    print("***DOWN***")

def left():
    print("***left***")

def right():
    print("***right***")
    

def on_release(key):
    print('{0} released'.format(key))
    if key == keyboard.Key.esc:
        #stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press= on_press,
        on_release= on_release) as listener:
    listener.join()

# .. or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()




