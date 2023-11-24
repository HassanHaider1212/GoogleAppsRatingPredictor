class Todo:
    tasks = []

    # def add(self, task):
    #     self.tasks.append(task)
    #     print(self.tasks)
        
    # def delete(self, task):
    #     self.tasks.remove(task)
    #     print(self.tasks)

    def get_tasks(self):
        return self.tasks
    
    def submitForm(self, formdata):
        self.tasks.append(formdata)
        return self.tasks