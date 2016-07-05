# -*- coding: UTF-8 -*-
import sys
import re
from workflow import Workflow3
from file import SPLIT, todo_actions

reload(sys)
sys.setdefaultencoding('utf-8')


def todo_new_action(wf):
	if len(wf.args):
		arg = ''.join(wf.args)
	else:
		arg = ''
		
	try:
		filename, todo = arg.split(SPLIT)
		actions_obj = todo_actions()
		
		for actions in actions_obj.actions.items():
			action_name, action_icon = actions
			
			wf.add_item(title=action_name, 
						subtitle='{action} this todo in todos/{filename}.md'.format(action=action_name, filename=filename), 
						arg='{filename}{split}{todo}{split}{action}'.format(filename=filename, split=SPLIT, todo=todo, action=action_name),
						icon=action_icon,
						valid=True)

	except ValueError:
		pass
	finally:
		wf.send_feedback()


if __name__ == '__main__':
	wf = Workflow3()
	logger = wf.logger
	sys.exit(wf.run(todo_new_action))
