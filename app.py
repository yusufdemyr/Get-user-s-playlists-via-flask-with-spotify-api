from flask import Flask, render_template, request, redirect, url_for
import os
import requests
import startup
import json
import jyserver.Flask as jsf
from flask_mysqldb import MySQL
import MySQLdb.cursors
import emoji




app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config['SESSION_COOKIE_NAME'] = 'My Cookie'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'YOUR-PASSWORD'
app.config['MYSQL_DB'] = 'playlists'




mysql = MySQL(app)



@jsf.use(app) # Connect Flask object to JyServer
class App():
    def __init__(self):
        pass




@app.route('/',methods =['GET', 'POST'])
def index():

    if request.method == 'POST':
        global username
        response = startup.getUser()
        username_link = request.form.get("username")
        username = username_link.split('/')[-1].split('?')[0]
        return redirect(response)

    return App.render(render_template('index.html'))

@app.route('/callback', methods=['GET'])
def callback():
    global access_token
    access_token = startup.getUserToken(request.args['code'])
    
    return redirect('results')


@app.route('/results', methods = ['GET','POST'])
def results():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    
    cursor.execute('DELETE FROM users')
    mysql.connection.commit()

    
    url = 'https://api.spotify.com/v1/users/{}/playlists'.format(username)
    r = requests.get(url, headers=access_token[1])
    data = json.loads(r.content)
    i = 0
    sozluk = {}
    keys = []
    values = []
    while i < len(data['items']):
        cursor.execute('INSERT INTO users VALUES (NULL,%s, %s)', [emoji.demojize(data['items'][i]['name']), data['items'][i]['external_urls']['spotify']])
        keys.append((data['items'][i]['name']))
        values.append((data['items'][i]['external_urls']['spotify']))
        mysql.connection.commit()
        i+= 1
    for i in range(len(keys)):
        sozluk[keys[i]] = values[i]

    print('Success')
        
    
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('results.html',data=sozluk)


if __name__ == '__main__':
    app.run()
