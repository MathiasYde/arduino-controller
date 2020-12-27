class Input():
  def __init__(self):
    self.actions = {}

  def update_input(self, new_state):
    for action in self.actions:
      binding = self.actions[action]["binding"]
      processors = self.actions[action]["processors"]

      # Ask the binding to update this actions value
      self.actions[action]["value"] = binding(new_state)

      # Apply this actions processors to this actions value
      for processor in processors:
        if type(self.actions[action]["value"]) is list:
          self.actions[action]["value"] = [processor(component) for component in self.actions[action]["value"]]
        else:
          self.actions[action]["value"] = processor(self.actions[action]["value"])

  def on_change(self, action, callback):
    pass

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