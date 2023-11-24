import eel

from data.todo import Todo
#frontend and backend connected here.

todo_app = Todo()

# @eel.expose
# def add(task):
#     todo_app.add(task)

# @eel.expose
# def delete(task):
#     todo_app.delete(task)

@eel.expose
def get_tasks():
    return todo_app.get_tasks()

@eel.expose
def submitForm(formdata):
    return todo_app.submitForm(formdata)