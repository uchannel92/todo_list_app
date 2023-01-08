from datetime import datetime
from datetime import timedelta

now = datetime.now()
date_added_key = now.strftime("%c")

# Sample dates used to populate example todos.
yesterday = (now - timedelta(days = 1))
two_days_ago = (now - timedelta(days = 2))
date_added_yesterday_key = yesterday.strftime("%c")
date_added_two_days_ago_key = two_days_ago.strftime("%c")

todo_items = [
	# example todos
    {
        'title': 'Walk the dog',
        'task': 'Walk dog 3x today',
        'priority': 'low',
        'date_added': f'{date_added_yesterday_key}',
    },
    {
        'title': 'Make bed',
        'task': 'Clean bedsheets, add to wash pile.',
        'priority': 'high',
        'date_added': f'{date_added_two_days_ago_key}',
    },
]

todo_item = {}

def create_new_todo(todo_item):
	priorities = ['high', 'medium', 'low']

	title = input('title: ')
	task = input('task: ')
	priority = input('Enter todo urgency (high/medium/low) : ' )

	todo_item['title'] = title
	todo_item['task'] = task
	todo_item['date_added'] = date_added_key

	while True:
		if priority.lower() in priorities:
			todo_item['priority'] = priority
			break
		else:
			print('Enter the listed priority')
			continue

	return todo_item


def add_todo_to_list(new_todo_item, todo_items_list):
	
	todo_items_list.append(new_todo_item)
	print('Todo has been added')
	return todo_items_list
	

def print_all_todos(todo_items_list):

	if len(todo_items_list) == 0:
		print("You have no todo's, start creating some! ")
	else:
		for index, todo in enumerate(todo_items_list):
			title = todo['title']
			task = todo['task']
			date_added = todo['date_added']
			priority = todo['priority']
			print(f'{index})\n\tTitle: {title}\n\tTask: {task}\n\tDate Added: {date_added}\n\tPriority: {priority}')
			print('\t\t\t---')


def delete_todo_from_list(todo_items_list):
	print('Enter the todo number to delete.')
	print_all_todos(todo_items)
	value = int(input('Enter number here: '))
	print(f'You have deleted:\n{todo_items_list[value]}')
	del todo_items_list[value]

	return todo_items_list


def update_todo_entry(todo_items_list):
	print('Select the todo you would like to update: ')

	for index, todo in enumerate(todo_items_list):
		print(f"{index})\n\tTitle: {todo['title']}\n\tTask: {todo['task']}")

	# add try catch to ensure user enter index that exists in dict
	todo_index = int(input('Enter the corresponding number: '))
	
	# add try catch here to ensure user enters key that exists in dict
	key = input('Enter the relevant key: ')
	new_value = input(f'Was "{todo_items_list[todo_index][key]}": ')

	todo_items_list[todo_index][key] = new_value
	print('Changes made.')
	pass


# Working functions here

# Create
# create_todo = create_new_todo(todo_item)
# add_new_todo = add_todo_to_list(create_todo, todo_items)

# Read
# print_todos = print_all_todos(todo_items)

# Update
# update_todo = update_todo_entry(todo_items)

# Delete
# delete_todo = delete_todo_from_list(todo_items)

# print(todo_items)

# while True:
# 	todo = new_todo(new_task)
# 	grow_todos = add_todo(todo, todo_list)
	# print(todo_list)

# Todo options selctions question
# print(
# """Select one of the following options below:

# 1) Create a new todo
# 2) Show remaining todos
# 3) Update a todo
# 4) Delete a todo
# 5) Quit
# """)