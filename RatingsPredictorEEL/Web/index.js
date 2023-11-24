async function getTasks(){
    const tasks = await eel.get_tasks()()
    const divTasks = document.getElementById('tasks')
    divTasks.innerHTML = ''

    let taskDisplay = '' 

    for (let task of tasks) {
        taskDisplay += `<p>App Name: ${task.appname}<br> Rating Count: ${task.ratingcount}<br>
                        Installs: ${task.installs}<br> Price: ${task.price}<br> Size: ${task.size}<br> Version: ${task.version}<br>
                        Days Since Last Updated: ${task.last_update}<br> Content Rating: ${task.contentRating}<br> Category: ${task.category}<br> 
                        Ad Supported: ${task.ad_supported}</p><br>`;
    }

    divTasks.innerHTML = taskDisplay
}

// document.getElementById('addbtn').addEventListener('click', async() => {
//     await eel.add(document.getElementById('taskinput').value)
//     getTasks()  
// })

// document.getElementById('removebtn').addEventListener('click', async() => {
//     await eel.delete(document.getElementById('taskinput').value)
//     getTasks()
// })

document.getElementById('submitform').addEventListener('click', async() => {

    event.preventDefault();

    var checkbox = document.getElementById("ad_supported");

        // Update the value based on the checked status
        if (checkbox.checked) {
            checkbox.value = 1;
        } else {
            checkbox.value = 0;
        }

    const formData = {
        appname: document.getElementById('appname').value,
        ratingcount: document.getElementById('ratingcount').value,
        installs: document.getElementById('installs').value,
        price: document.getElementById('price').value,
        size: document.getElementById('size').value,
        version: document.getElementById('version').value,
        last_update: document.getElementById('last_update').value,
        contentRating: document.getElementById('contentRating').value,
        category: document.getElementById('category').value,
        ad_supported: checkbox.value,
    };

    await eel.submitForm(formData)()
    getTasks()
})