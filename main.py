

def main():
  port = "COM6"
  rate = 9600

  arduino = serial.Serial(port, rate, timeout=0.1)
  input = Input()

  input.new_action(
    "mouse",
    input.bindings.vector2("joy_x", "joy_y"),
    [
      input.processors.map(0, 1023, -1, 1),
      input.processors.deadzone(0.05)
    ]
  )

  input.new_action(
    "click",
    input.bindings.value("joy_b")
  )

  controller = Controller()

  #input.on_change("mouse", lambda value: print("new Δmouse", value))
  #input.on_change("click", lambda value: print("jump", value))

  while True:
    # Removing the last two characters to remove new line characters
    data = arduino.readline()[:-2]
    if data:
      input.update_input(json.loads(data.decode("utf-8")))
    else:
      continue

    mouse = input.get("mouse")
    if mouse != [0, 0]:
      controller.move(*[component * 60 for component in mouse])

    click = input.get("click")
    if click:
      controller.click(Button.left)

if __name__ == "__main__":
  import serial
  from pynput.mouse import Button, Controller
  from input import Input
  import os
  import json
  import time
  main()

