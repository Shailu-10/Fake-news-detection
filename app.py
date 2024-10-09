from flask import Flask, abort, jsonify, request, render_template
#from sklearn.externals import joblib
import joblib
from feature import *
import json
import sklearn.linear_model._logistic

pipeline = joblib.load('./pipeline.sav')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/api',methods=['POST'])#api is just a page name types..
def get_delay():
    result=request.form
    query_title = result['title']
    query_author = result['author']
    query_text = result['maintext']
    print(query_text)
    query = get_all_query(query_title, query_author, query_text)
    user_input = {'query':query}
    pred = pipeline.predict(query)
    print(pred)
    dic = {1:'real',0:'fake'}
    return f'<html><body><h1>{dic[pred[0]]}</h1> <form action="/"> <button type="submit">back </button> </form></body></html>'
    # the f is called f string.. it is formatted string, means placeholder value will 
    #value will be inserted whatever variable is between cruly braces {}
    #html is for back button

if __name__ == '__main__':
    app.run(port=8080, debug=True)
