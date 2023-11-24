async function getTasks() {
    const tasks = await eel.get_tasks()();
    const divTasks = document.getElementById('tasks');
    divTasks.innerHTML = '';

    let taskDisplay = '';

    if (tasks && tasks.length > 0) {
        for (let task of tasks) {
            const [appId, appName, ratingCount, installs, price, size, version, lastUpdate, contentRating, category, adSupported] = task;

            
            taskDisplay += `
            <p>App ID: ${appId}</p>
            <p>App Name: ${appName || 'N/A'}</p>
            <p>Rating Count: ${ratingCount}</p>
            <p>Installs: ${installs}</p>
            <p>Price: ${price}</p>
            <p>Size: ${size}</p>
            <p>Version: ${version}</p>
            <p>Days Since Last Updated: ${lastUpdate}</p>
            <p>Content Rating: ${contentRating}</p>
            <p>Category: ${category}</p>
            <p>Ad Supported: ${adSupported}</p><br>`;
        }
    } 
    else {
        taskDisplay = '<p>No tasks yet</p>';
    }

    divTasks.innerHTML = taskDisplay;
}
getTasks()

document.getElementById('submitform').addEventListener('click', async(event) => {

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