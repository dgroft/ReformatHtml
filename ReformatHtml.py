import sublime, sublime_plugin, re

class ReformatHtmlCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		if self.view.sel()[0].empty():
			# nothing selected, so process the entire file
			region = sublime.Region(0, self.view.size())
			sublime.status_message('Reformatting the entire file')
			contents = self.view.substr(region)

		else:
			# process the selection only
			region = self.view.line(self.view.sel()[0])
			sublime.status_message('Reformatting current selection')
			contents = self.view.substr(self.view.sel()[0])

		#replace all >< with >\n<
		contents = re.sub("><", ">\n<", contents)

		#strip out whitespace at beginning of each line
		contents = re.sub("", "", contents)

		# replace the code in Sublime Text
		self.view.replace(edit, region, contents)
