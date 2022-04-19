from pynput.mouse import Listener as mouse_listener
from pynput.keyboard import Listener as keyboard_listener, Key
from time import time

class listener():
    def __init__(self, file, wait=False, mouse_mov=False):
        # custimization
        self.mouse_mov = mouse_mov
        self.wait = wait
        
        self.file = file
        
        # create listeners
        self.keyboard_listener = keyboard_listener(on_press=self.on_press, on_release=self.on_release)
        self.mouse_listener = mouse_listener(on_move=self.on_move, on_click=self.on_click, on_scroll=self.on_scroll)
        
        # to calculate the wait between opperations
        self.last_time = time()

    
    # file writeing utill
    def write(self, data):
        with open(self.file, "a") as f:
            # append the wait
            if self.wait:
                f.write(f"\nW {time() - self.last_time}")
                self.last_time = time()
            
            f.write(f"\n{data}")
            
    
    # start listeners
    def start(self):
        self.keyboard_listener.start()
        self.mouse_listener.start()
        
        self.keyboard_listener.join()
        self.mouse_listener.join()
        
    # stop all listeners
    def end(self):
        self.keyboard_listener.stop()
        self.mouse_listener.stop()

    # keypresses
    def on_press(self, key):
        self.write(f"P {key}")
        
    def on_release(self, key):
        self.write(f"R {key}")
        
        # end on keypress
        if key == Key.ctrl_l:
            self.end()

    # mouse events
    def on_move(self, x, y):
        if self.mouse_mov:
            self.write(f"M {x},{y}")

    def on_click(self, x, y, button, pressed):
        self.write(f"{'C' if pressed else 'U'} {x},{y},{button}")

    def on_scroll(self, x, y, dx, dy):
        self.write(f"S {x},{y}")