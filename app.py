from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'todo_db'
app.config['MONGO_URI']='mongodb://todouser123:todouser123@ds123562.mlab.com:23562/todo_db'

mongo = PyMongo(app)

@app.route('/add')
def add():
    task = mongo.db.tasks
    task.insert({'id':'1', 
                'title':'Short Task',
                'description':'Task NO 1',
                'done':'true'})
    return 'add task'

@app.route('/find')    
def find():
    task = mongo.db.tasks
    findtask = task.find_one({'title':'Short Task'})
    return 'Task found : Title is '+findtask['title'] + ', Description is '+findtask['description']+' & Status of Complete is  '+findtask['done']

@app.route('/update')
def update():
    task = mongo.db.tasks
    updatetask = task.find_one({'title':'Short Task'})
    updatetask['description']="Task No 11"
    updatetask['done']='false'
    task.save(updatetask)
    return 'Task updated'

@app.route('/delete')
def delete():
    task = mongo.db.tasks
    deletetask = task.find_one({'title':'Short Task'})
    task.remove(deletetask)
    return 'Task Deleted'


if __name__ == '__main__':
    app.run(debug=True)