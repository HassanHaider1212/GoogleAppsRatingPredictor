async function getTasks(){
    const tasks = await eel.get_tasks()()
    const divTasks = document.getElementById('tasks')
    divTasks.innerHTML = ''

    let taskDisplay = '' 

    for(let task of tasks){
        taskDisplay += `<p>${task}</p>`
    }

    divTasks.innerHTML = taskDisplay
}

document.getElementById('addbtn').addEventListener('click', async() => {
    await eel.add(document.getElementById('taskinput').value)
    getTasks()  
})

document.getElementById('removebtn').addEventListener('click', async() => {
    await eel.delete(document.getElementById('taskinput').value)
    getTasks()
})