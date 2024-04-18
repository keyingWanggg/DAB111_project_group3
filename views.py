from flask import render_template
import sqlite3

def data_show():
    
    conn = sqlite3.connect('data/data.db')  
    c = conn.cursor()
    c.execute("SELECT id, release, theaters, average, date, distributor FROM products")  
    data = c.fetchall()  
    conn.close()  
    
    
    return render_template('data_show.html', data=data)
