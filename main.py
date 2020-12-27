from input import Input


def main():
  port = "COM6"
  rate = 9600

  arduino = serial.Serial(port, rate, timeout=0.1)
  input = Input()

  input.new_action(
    "mouse",
    input.bindings.vector2("joy_x", "joy_y")
    [
      input.processors.map(0, 1023, -1, 1),
      input.processors.deadzone(0.05)
    ]
  )

  input.new_action(
    "jump",
    input.bindings.value("joy_b")
  )

  input.on_change("mouse", lambda value: print("new Δmouse", value))
  input.on_change("jump", lambda value: print("jump", value))

  while True:
    # Removing the last two characters to remove new line characters
    data = arduino.readline()[:-2]
    if data:
      message = data.decode("utf-8")
      state = json.loads(message)
      input.update_input(state)

if __name__ == "__main__":
  import serial
  import pyautogui as gui
  import json
  import time
  main()