
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
    // else {
    //     taskDisplay = '<p>No tasks yet</p>';
    // }

    divTasks.innerHTML = taskDisplay;
}
// getTasks()

document.getElementById('submitform').addEventListener('click', async(event) => {

    event.preventDefault();
    var appName = document.getElementById('appname').value;

    // Check if the App Name is not empty
    if (appName.trim() === '') {
        // Display an alert or error message (you can customize this)
        // alert('Please enter the App Name.');
        $("#appnamediv").show();
        // $("#ratingcountdiv").show();

        // Scroll up to the error div
        $('html, body').animate({
            scrollTop: $("#appnamediv").offset().top
        }, 1000); // 1000 milliseconds = 1 second

        // Hide the divs after 10 seconds
        setTimeout(function() {
            $("#appnamediv").hide();
            // $("#ratingcountdiv").hide();
        }, 10000); // 10000 milliseconds = 10 seconds
    } 
    else 
    {
        var checkbox = document.getElementById("ad_supported");
        // Update the value based on the checked status
        if (checkbox.checked) {
            checkbox.value = 1;
        } else {
            checkbox.value = 0;
        }

        var checkbox1 = document.getElementById("InAppPurchases");
        // Update the value based on the checked status
        if (checkbox1.checked) {
            checkbox1.value = 1;
        } else {
            checkbox1.value = 0;
        }

        var checkbox2 = document.getElementById("EditorsChoice");
        // Update the value based on the checked status
        if (checkbox2.checked) {
            checkbox2.value = 1;
        } else {
            checkbox2.value = 0;
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
            InAppPurchases: checkbox1.value,
            EditorsChoice: checkbox2.value,
        };
        
        const divTasks = document.getElementById('tasks');

        // divTasks.innerHTML = "In Porgress!";

        str = await eel.submitForm(formData)() //storing data in database. Uncomment it when use.
        if(str == "Error: Integrity Error"){
            $("#formDbdiv").show();
            // Hide the divs after 10 seconds
            setTimeout(function() {
                $("#formDbdiv").hide();
                // $("#ratingcountdiv").hide();
            }, 10000); // 10000 milliseconds = 10 seconds
        }

        if(str != "Error: Integrity Error")
        {
            // Predict rating
            const taskDisplay = await eel.predictRating(formData)();
            debugger;console.log("Task Display:", taskDisplay);

            // const parsedResult = parseFloat(taskDisplay);
            // console.log("Task Display parseFloat:", taskDisplay);
            var str;
            const result_range = document.getElementById('result_range');
            const result_range_text = document.getElementById('result_range_text');
            if(taskDisplay==0){ 
                str = "0 - 2"
                result_range_text.value  = str;
                result_range_text.removeAttribute('disabled');
                result_range.style.display = "block";
            }
            else if(taskDisplay==1){
                str = "2 - 3"  
                result_range_text.value  = str;
                result_range.style.display = "block";
            }
            else if(taskDisplay==2){
                str = "3 - 4"  
                result_range_text.value  = str;
                result_range.style.display = "block";
            }
            else if(taskDisplay==3){
                str = "4 - 5"
                result_range_text.value  = str;
                result_range.style.display = "block";
            }

            parsedResult = parseInt(taskDisplay)
            if (!isNaN(taskDisplay)) {
                // Update the UI with the parsed result
                divTasks.innerHTML = `<canvas id="ratingChart" width="400" height="400"></canvas>`;

                // Create a pie chart using Chart.js
                const ctx = document.getElementById('ratingChart').getContext('2d');
                const ratingChart = new Chart(ctx, {
                    type: 'doughnut',
                    data: {
                        labels: ['Rating', 'Remaining'],
                        datasets: [{
                            data: [parsedResult, 5 - parsedResult], // Assuming a rating scale of 0 to 5
                            backgroundColor: ['#2ecc71', '#9b59b6'], // Colors for the chart segments
                        }],
                        borderColor: "transparent"
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        legend: {
                            display: true,
                            legend: {
                                display: false,
                            },
                        },
                    },
                });


            } 
            else {
                // Handle the case where the result is not a valid number
                // divTasks.innerHTML = "Error: Invalid result";
                $("#resultdiv").show();
                setTimeout(function() {
                    $("#resultdiv").hide();
                    // $("#ratingcountdiv").hide();
                }, 10000); // 10000 milliseconds = 10 seconds
            }
        }
        $("#submissionform").trigger('reset');
        // getTasks()
    }

})