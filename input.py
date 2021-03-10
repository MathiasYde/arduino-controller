class Input():
  def __init__(self):
    self.actions = {}
    self.previous_state = {}
    self.on_change_listeners = {}

  def update_input(self, new_state):
    for action, attributes in self.actions.items():
      binding = attributes["binding"]
      processors = attributes["processors"]

      # Get value from binding
      attributes["value"] = binding(new_state)

      # Apply processors
      for processor in processors:
        if type(attributes["value"]) is list:
          attributes["value"] = [processor(component) for component in attributes["value"]]
        else:
          attributes["value"] = processor(attributes["value"])

      # set previous state to None if none existant
      if action not in self.previous_state:
        self.previous_state[action] = None

      # check for changes
      if self.previous_state[action] == attributes["value"]:
        continue

      # notify all listeners for this action
      for listener in self.on_change_listeners:
        if listener == action:
          for callback in self.on_change_listeners[listener]:
            callback(attributes["value"])

      # update previous state for this action
      self.previous_state[action] = attributes["value"]

  def on_change(self, action, callback):
    if action not in self.on_change_listeners:
      self.on_change_listeners[action] = []

    self.on_change_listeners[action].append(callback)

  def get(self, action):
    return self.actions[action]["value"]

  def new_action(self, name, binding, processors=[]):
    if name in (None, ""):
      raise NameError("Action must have a name")

    if binding == None:
      raise ValueError("Action must have a binding")

    self.actions[name] = {
      "value": None,
      "binding": binding,
      "processors": processors,
    }

  class bindings():
    """
    Bindings are used to map new state input to action values
    """

    @staticmethod
    def value(key):
      """
      Maps one new input state to one action value
      Ideal for jumping, opening GUI and changing state like running.
      """
      return lambda keys: keys[key]

    @staticmethod
    def vector2(horizontal_key, vertical_key):
      """
      Maps two new input state to two action values
      Ideal for mouse movement and WASD movement
      """
      return lambda keys: [keys[horizontal_key], keys[vertical_key]]
    
  class processors():
    """
    Processors are used for post-processing action values
    """
    @staticmethod
    def deadzone(thredshold):
      """
      Axis deadzone will return the original value if it is too similar
      """
      return lambda v: v if abs(v) > thredshold else 0

    @staticmethod
    def map(old_min, old_max, new_min, new_max):
      # Yeeted from https://www.arduino.cc/reference/en/language/functions/math/map/
      return lambda v: (v - old_min) * (new_max - new_min) / (old_max - old_min) + new_min