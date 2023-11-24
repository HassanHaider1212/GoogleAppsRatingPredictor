class Todo:
    tasks = []

    def get_tasks(self):
        return self.tasks
    
    def submitForm(self, formdata):
        self.tasks.append(formdata)
        return self.tasks