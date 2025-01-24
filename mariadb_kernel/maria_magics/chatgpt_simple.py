from mariadb_kernel.maria_magics.line_magic import LineMagic

""" This class implements a simple magic for calling genAI. It uses no database image/state (yet), and is only a POC"""
class ChatGPT(LineMagic):
    def __init__(self, args):
	    self.args = args
		
    def name(self):
	    return "%ChatGPT"
	
	def help(self):
	    return help_text
	
	def execute(self, kernel, data):
		message = { 'name': 'stdout', 'text': self.args}
		kernel.send_response(self.iopub_socket, 'stream', message)