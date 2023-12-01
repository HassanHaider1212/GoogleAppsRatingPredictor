import pyodbc
import pickle
import numpy as np

# Replace these values with your SQL Server details
server = 'HP\SQLEXPRESS02'
database = 'GoogleApps'

class FormSubmission:
    def __init__(self):
        # Establish a connection to the SQL Server database using Windows Authentication
        self.conn = pyodbc.connect(f'DRIVER=ODBC Driver 17 for SQL Server;SERVER={server};DATABASE={database};Trusted_Connection=yes;')
        self.cursor = self.conn.cursor()

    def insert_form(self, formdata):
        # Insert form data into the SQL Server database
        self.cursor.execute('''
            INSERT INTO app_data (appname, ratingcount, installs, price, size, version, last_update, contentRating, category, ad_supported)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (formdata['appname'], formdata['ratingcount'], formdata['installs'], formdata['price'], formdata['size'],
              formdata['version'], formdata['last_update'], formdata['contentRating'], formdata['category'], formdata['ad_supported']))

        self.conn.commit()

    def get_formdata(self):
        # Retrieve data from the SQL Server database
        self.cursor.execute('SELECT * FROM app_data')
        return self.cursor.fetchall()
    
    def predictRating(self,formdata):
        # Load the model using pickle
        with open('data\\RatingsPredictorModel\\project_model.pkl', 'rb') as file:
            loaded_model = pickle.load(file)
        
        formdata_dict = formdata[0]
        input_array = np.array(list(formdata_dict.values())).reshape(1, -1)
        rating_predict = loaded_model.predict(input_array)
        return rating_predict
        

    def close_connection(self):
        # Close the database connection
        self.conn.close()
