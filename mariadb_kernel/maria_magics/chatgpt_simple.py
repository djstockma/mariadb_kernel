from mariadb_kernel.maria_magics.line_magic import LineMagic
""" This class implements a simple magic for calling genAI. It uses no database image/state (yet), and is only a POC"""

#FIXME: Add a help text
help_text = """ """

class Chatgpt_simple(LineMagic):
    def __init__(self, args):
        self.args = args
        
    def name(self):
        return "%ChatGPT"
    
    def help(self):
        return help_text
    
    def execute(self, kernel, data):
        self.simple_chat(kernel, data)
        
        