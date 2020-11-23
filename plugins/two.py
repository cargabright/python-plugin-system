"""
Plugin #2
"""

class Plugin:
    def __init__(self, *args, **kwargs):
        print("Plugin two initialised")
        print("Plugin two args: ", args, kwargs)

    def execute(self):
        print("Executing plugin two")