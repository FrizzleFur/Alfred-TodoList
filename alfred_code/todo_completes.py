# -*- coding: utf-8 -*-
import sys
import re
from workflow import Workflow3
from file import SPLIT, todo_files

reload(sys)
sys.setdefaultencoding('utf-8')


def todo_completed(wf):
	if len(wf.args):
		try:
			arg = re.findall(r'delete? (.*)', ''.join(wf.args))[0]
		except IndexError:
			arg = ''
	else:
		arg = ''
	
	file_object = todo_files(arg)
	file_items = file_object.get_todo_files(complete=True).items()
	
	todo_items = []
	
	for item in file_items:
		filename, file_obj = item
		for todo in file_obj['todos']:
			
			wf.add_item(title=todo, 
						subtitle=filename, 
						arg='{filename}{split}{todo}{split}delete'.format(filename=filename, split=SPLIT, todo=todo),
						icon='new_todo.png',
						valid=True)

	wf.send_feedback()
	

if __name__ == '__main__':
	wf = Workflow3(update_settings={
		'github_slug': 'ecmadao/Alfred-TodoList',
		'frequency': 4
	})
	logger = wf.logger
	sys.exit(wf.run(todo_completed))
	if wf.update_available:
		wf.start_update()
