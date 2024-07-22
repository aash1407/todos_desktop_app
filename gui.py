import modules.app1_module_functions as functions
import FreeSimpleGUI as sg
import time

sg.theme("Black")

clock = sg.Text('', key='clock')
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key='todos_list',
                      enable_events=True, size=[45, 5])
edit_button = sg.Button("Edit")
task_done_button = sg.Button("Task done")
exit_button = sg.Button("Exit")

window = sg.Window('My To-Do App',
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, task_done_button],
                           [exit_button]],
                   font=('Helvetica', 20))

while True:

    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M"))
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos_list'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values['todos_list'][0]
                new_todo = values['todo'] + "\n"
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos_list'].update(values=todos)
            except IndexError:
                sg.popup("Please select a todo item to edit!", font = ("Helvetica",20) )
        case "Task done":
            try:
                todo_done = values['todos_list'][0]
                todos = functions.get_todos()
                todos.remove(todo_done)
                functions.write_todos(todos)
                window['todos_list'].update(values=todos)
            except IndexError:
                sg.popup("Please select a todo item to mark as done!", font=("Helvetica", 20))

        case "Exit":
            break
        case "todos_list":
            window['todo'].update(value=values['todos_list'][0])
        case sg.WIN_CLOSED:
            break

window.close()



