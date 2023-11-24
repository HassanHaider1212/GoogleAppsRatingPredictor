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
    # Convert rows to a list of tuples with appropriate data types
    tasks = [
        (
            str(row[0]),          
            str(row[1]),          
            int(row[2]),          
            int(row[3]),          
            float(row[4]),        
            int(row[5]),          
            int(row[6]),          
            int(row[7]),          
            str(row[8]),          
            str(row[9]),          
            bool(row[10])         
        )
        for row in tasks
    ]

    return tasks

# Don't forget to close the connection when your application exits
atexit.register(form_repo.close_connection)

# Rest of your Eel and application code...