import eel
import atexit
from data.FormSubmissionRepository import FormSubmission

form_repo = FormSubmission()

@eel.expose
def submitForm(formdata):
    try:
        form_repo.insert_form(formdata)
    except:
        return "Error: Integrity Error"

@eel.expose
def predictRating(formdata):
    
    tasks = {
        'Rating Count': int(formdata['ratingcount']) if formdata['ratingcount'] is not None and formdata['ratingcount'] != '' else 0,
        'Minimum Installs': int(formdata['installs']) if formdata['installs'] is not None and formdata['installs'] != '' else 0,
        'Price': float(formdata['price']) if formdata['price'] is not None and formdata['price'] != '' else 0,
        'Size': float(formdata['size']) if formdata['size'] is not None and formdata['size'] != '' else 0,
        'Minimum Android': float(formdata['version']) if formdata['version'] is not None and formdata['version'] != '' else 0,
        'Days Since Last Updated': int(formdata['last_update']) if formdata['last_update'] is not None and formdata['last_update'] != '' else 0,
        
        'Content Rating_Adults only 18+': 1 if formdata['contentRating'] == "adult" else 0,
        'Content Rating_Everyone': 1 if formdata['contentRating'] == "everyone" else 0,
        'Content Rating_Everyone 10+': 1 if formdata['contentRating'] == "everyone10" else 0,
        'Content Rating_Mature 17+': 1 if formdata['contentRating'] == "Mature17" else 0,
        'Content Rating_Teen': 1 if formdata['contentRating'] == "Teen" else 0,
        
        'Category_Books & Reference': 1 if formdata['category'] == "Books" else 0,
        'Category_Business': 1 if formdata['category'] == "Business" else 0,
        'Category_Education': 1 if formdata['category'] == "Education" else 0,
        'Category_Entertainment': 1 if formdata['category'] == "Entertainment" else 0,
        'Category_Finance': 1 if formdata['category'] == "Finance" else 0,
        'Category_Lifestyle': 1 if formdata['category'] == "Lifestyle" else 0,
        'Category_Music & Audio': 1 if formdata['category'] == "Music" else 0,
        'Category_Personalization': 1 if formdata['category'] == "Personalization" else 0,
        'Category_Productivity': 1 if formdata['category'] == "Productivity" else 0,
        'Category_Tools': 1 if formdata['category'] == "Tools" else 0,

        'Ad Supported': int(formdata['ad_supported']),

        #add these accoringly if needed, not used in form but used in model
        'In App Purchases': 0,
        'Editors Choice': 0,
    }
    try:
        result = form_repo.predictRating([tasks])
        return str(result[0])
    except Exception as e:
        print("Error during prediction:", str(e))
        return "Error: Unable to make a prediction"




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
