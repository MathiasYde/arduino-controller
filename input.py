class Input():
  def __init__(self):
    self.actions = {}

  def update_input(self, new_state):
    for action in self.actions:
      bindings = self.actions[action]["bindings"]
      processors = self.actions[action]["processors"]

      self.actions[action]["value"] = binding(new_state)

      for processor in processors:
        if type(self.actions[action]["value"]) is list:
          self.actions[action]["value"] = [processor(component) for component in self.actions[action]["value"]]
        else:
          self.actions[action]["value"] = processor(self.actions[action]["value"])


  def on_change(self, action, callback):
    pass



  def new_action(self, name, binding, processors=[]):
    if name in (None, ""):
      raise NameError("Action must have a name")

    self.actions[name] = {
      "value": None,
      "binding": binding,
      "processors": processors,
    }

  class bindings():
    @staticmethod
    def value(key):
      return lambda keys: keys[key]

    @staticmethod
    def vector2(horizontal_key, vertical_key):
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