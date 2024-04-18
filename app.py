from flask import Flask, render_template
from views import  data_show

app = Flask(__name__)



app.add_url_rule('/', 'home', lambda: render_template('home.html')) 
app.add_url_rule('/about', 'about', lambda: render_template('about.html'))

app.add_url_rule('/data_show', 'data_show', data_show)

if __name__ == '__main__':
   
    from database import create_table
    create_table()  
    app.run( port=8001, debug=True)
