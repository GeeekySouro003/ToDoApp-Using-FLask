from flask import Flask,render_template,request,redirect,url_for

app=Flask(__name__,template_folder="templates")

todos=[{"task":"Sample Todo","done":False}]

@app.route('/')
def index():
    return render_template('index.html',todos=todos)

@app.route('/add',methods=['POST'])
def add():
    todo=request.form['todo']
    todos.append({"task":todo,"done":False})

if __name__ == '__main__':
    app.run(debug=True)