import pyodbc

class FormSubmission:
    def __init__(self, server, database):
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
        
        rows = self.cursor.fetchall()

        # Convert rows to a list of tuples with appropriate data types
        todos = [
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
        
        return todos

    def close_connection(self):
        # Close the database connection
        self.conn.close()
