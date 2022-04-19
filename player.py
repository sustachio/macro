from pynput.mouse import Button, Controller as mController
from pynput.keyboard import Key, Controller as kController
from time import sleep

class player():
  def __init__(self, file):
    # controlers
    self.keyboard = kController()
    self.mouse = mController()
    
    # read off the macro file
    with open(file, "r") as f:
      # clean the string and split the command
      self.commands = [tuple(i.strip().split(" ")) for i in f.readlines()[1:]]
      
          
  def play(self):
    for line in self.commands:
      command = line[0]
      
      if command == "W":
        wait = float(line[1])
        sleep(wait)
        
      
      # press key
      if command == "P":
        key = line[1].strip("'")
        
        # handle special keys
        if key.startswith("Key."):
          self.keyboard.press(Key[key[4:]])
          continue
        
        self.keyboard.press(key)
      
      # relese key (same as press almost)
      elif command == "R":
        key = line[1].strip("'")
        if key.startswith("Key."):
          self.keyboard.release(Key[key[4:]])
          continue
        self.keyboard.release(key)
        
      elif command == "M":
        # get the x and y from the line
        [x, y] = [int(i) for i in line[1].split(",")]
        
        self.mouse.position = (x,y)
        
      # move and click
      elif command == "C":
        [x, y, button] = line[1].split(",")
        self.mouse.position = (int(x),int(y))
        self.mouse.press(Button[button[7:]])
      
      # relese click
      elif command == "U":
        [x, y, button] = line[1].split(",")
        self.mouse.position = (int(x),int(y))
        self.mouse.release(Button[button[7:]])

