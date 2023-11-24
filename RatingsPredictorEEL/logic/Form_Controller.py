import eel
import atexit
from data.FormSubmissionRepository import FormSubmission

form_repo = FormSubmission()

@eel.expose
def submitForm(formdata):
    form_repo.insert_form(formdata)

@eel.expose
def get_tasks():
    tasks = form_repo.get_formdata()
    return tasks

# Don't forget to close the connection when your application exits
atexit.register(form_repo.close_connection)

# Rest of your Eel and application code...