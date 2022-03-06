# next: secure
from flask import Flask, render_template, request, session
import sqlite3

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home_func():
    return render_template('login.html')

@app.route('/login', methods=['GET','POST'])
def login_func():
    session['id'] = request.form['key']
    if session['id'] in ['admin', 'name1', 'name2']:
        return render_template('login.html', x='hi %s'%session['id'])
    else:
        return render_template('login.html', x='please enter correct id')

@app.route('/button_val_to_sqlite', methods=['GET', 'POST'])
def on_off_results_func():
    state = request.form['key']
    sqlite_method(state)
    return render_template('login.html', x='pressed: %s'%state, id=session['id'])

def sqlite_method(switch_state):
    conn = sqlite3.connect('/var/www/FlaskApp/FlaskApp/my_db.db')
    cur = conn.cursor()
    if session['id'] == 'admin':
        cur.execute('UPDATE on_off3 SET state=?', (switch_state,))
    else:
        cur.execute('UPDATE on_off3 SET state=? WHERE id=?', (switch_state, session['id'],))
    conn.commit()
    conn.close()

@app.route('/return_data/<var>', methods=['GET', 'POST'])
def return_data_func(var):
    conn = sqlite3.connect('/var/www/FlaskApp/FlaskApp/my_db.db')
    cur = conn.cursor()
    cur.execute('SELECT state FROM on_off3 WHERE id = ?',(var,))
    data = cur.fetchall()[0][0]
    conn.close()
    return {'test': data}

############# retrieve data from board ####################
@app.route('/data_from_board_to_sql_url/<var>', methods=['GET', 'POST'])
def data_from_board_to_sql_func(var):
    conn = sqlite3.connect('/var/www/FlaskApp/FlaskApp/my_db.db')
    cur = conn.cursor()
    cur.execute('UPDATE sensor_table SET data=? WHERE id=?', (var[4:], var[:4],))
    conn.commit()
    conn.close()
    return render_template('login.html')

@app.route('/sensor_data_results_app_route/', methods=['GET', 'POST'])
def sensor_data_results_func():
    conn = sqlite3.connect('/var/www/FlaskApp/FlaskApp/my_db.db')
    cur = conn.cursor()
    cur.execute('SELECT data FROM sensor_table WHERE id = ?',(str(session['id']),))
    data = cur.fetchall()[0][0]
    conn.close()
    return render_template('login.html', x='data: ' + str(data), id=str(session['id']))    
