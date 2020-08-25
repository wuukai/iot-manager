from flask import Flask,render_template,request,session,url_for,redirect,json,jsonify
import sqlite3,os,random,time
from flask_cors import CORS

#主网站
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
CORS(app, resources=r'/*')  

a={"message": [
      {
       'name':'ming',
       'Rfid':'123123',
       'state':'1',
       'time':'time'
      },
      {
        'name':'wang',
        'Rfid':'456456',
        'state':'1',
        'time':'time'
      },
      {        
        'name':'wang',
        'Rfid':'789789',
        'state':'1',
        'time':'time'
      }
    ]}

print(type(a))

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index_V2.html')


@app.route('/ajax/get', methods=['GET', 'POST'])
def get():
    return jsonify(a)

@app.route('/test', methods=['GET', 'POST'])
def test():
    return render_template('test.html',abc='abcc')
  

if __name__ == '__main__':
    app.run()
