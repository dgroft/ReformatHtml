import sublime, sublime_plugin, re

class ReformatHtmlCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		if self.view.sel()[0].empty():
			# nothing selected, so process the entire file
			region = sublime.Region(0, self.view.size())
			self.view.sel().add(region)
			sublime.status_message('Reformatting the entire file')
		else:
			sublime.status_message('Reformatting current selection')
		
		region = self.view.line(self.view.sel()[0])
		contents = self.view.substr(self.view.sel()[0])

		#replace all >< with >\n<
		contents = re.sub("><", ">\n<", contents)

		#strip out whitespace at beginning and end of each line
		contents = re.sub("\n[\s]+", "\n", contents)
		contents = re.sub("[\s]+\n", "\n", contents)

		# update the buffer
		self.view.replace(edit, region, contents)

		#reindent, using preexisting sublime command "reindent"
		self.view.run_command("reindent")
