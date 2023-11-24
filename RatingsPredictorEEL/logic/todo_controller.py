import eel
import pyodbc
#from data.todo import Todo
#frontend and backend connected here.

# Replace these values with your SQL Server details
server = 'HP\SQLEXPRESS02'
database = 'GoogleApps'

# Establish a connection to the SQL Server database using Windows Authentication
conn = pyodbc.connect(f'DRIVER=ODBC Driver 17 for SQL Server;SERVER={server};DATABASE={database};Trusted_Connection=yes;')
cursor = conn.cursor()

@eel.expose
def submitForm(formdata):
    # Insert form data into the SQL Server database
    cursor.execute('''
        INSERT INTO app_data (appname, ratingcount, installs, price, size, version, last_update, contentRating, category, ad_supported)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (formdata['appname'], formdata['ratingcount'], formdata['installs'], formdata['price'], formdata['size'],
          formdata['version'], formdata['last_update'], formdata['contentRating'], formdata['category'], formdata['ad_supported']))

    conn.commit()

@eel.expose
def get_tasks():
    # Retrieve data from the SQL Server database
    cursor.execute('SELECT * FROM app_data')
    
    rows = cursor.fetchall()

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
        for row in rows
    ]
    
    return tasks