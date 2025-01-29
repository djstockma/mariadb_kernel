from mariadb_kernel.maria_magics.line_magic import LineMagic

# Sets an llm model for the kernel

help_text = """"""

class Set_llm(LineMagic):
    def __init__(self, args):
        self.args = args
        
    def name(self):
        return "%set_llm"
    
    def help(self):
        return help_text
    
    def execute(self, kernel, data):
        self.set_llm(kernel, data)