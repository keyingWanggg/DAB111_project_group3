import sqlite3
import csv

def create_table():
    
    conn = sqlite3.connect('data/data.db')
    
    
    c = conn.cursor()
    
 
    c.execute('''CREATE TABLE IF NOT EXISTS products
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                  release TEXT,
                  theaters INTEGER,
                  average INTEGER,
                  date DATE,
                  distributor TEXT)''')
    

    conn.commit()
    
 
    conn.close()


create_table()




def load_data_from_csv(filename):
    
 
    conn = sqlite3.connect('data/data.db')
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM products")
    count = c.fetchone()[0]
    conn.close()

    if count > 0:
        print("Data has already been loaded.")
        return
    

    with open(filename, 'r', newline='', encoding='utf-8') as file:
      
        reader = csv.reader(file)
        
        
        next(reader)
        
        conn = sqlite3.connect('data/data.db')
        
        c = conn.cursor()
        
        try:
            
            for i, row in enumerate(reader):
                if i >= 50:  
                    break
                
                release = row[0]
                theaters = int(row[4]) 
                average = int(row[5])   
                date = row[6]
                distributor = row[7]
                
                
                c.execute('''INSERT INTO products (release, theaters, average, date, distributor) 
                             VALUES (?, ?, ?, ?, ?)''', (release, theaters, average, date, distributor))
            
           
            c.execute("DELETE FROM sqlite_sequence WHERE name='products'")
            
            
            conn.commit()
            print("Data loaded successfully.")
        
        except Exception as e:
           
            conn.rollback()
            print(f"An error occurred: {str(e)}")
        
        finally:
            
            conn.close()


load_data_from_csv('group_3_dataset.csv')
