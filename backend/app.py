from os import pardir
from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import hmac
from flask_cors import CORS
from flask_marshmallow import Marshmallow


app = Flask(__name__)
api = Api(app)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/taskdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

ma = Marshmallow(app)

################

### DATABASE ###

################

userstasks = db.Table('userstasks',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('task_id', db.Integer, db.ForeignKey('task.id'), primary_key=True)
)

taskscategories = db.Table('taskscategories',
    db.Column('category_id', db.Integer, db.ForeignKey('category.id'), primary_key=True),
    db.Column('task_id', db.Integer, db.ForeignKey('task.id'), primary_key=True)
)


###########
class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50))
    email = db.Column(db.String(50))
    password = db.Column(db.String(50))
    created_date = db.Column(db.String(50))
    updated_date = db.Column(db.String(50))
    tasks = db.relationship('Task', secondary=userstasks, lazy='subquery',
        backref=db.backref('users', lazy=True)) 


    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.email = "NULL"


    def get_all_data_json(self):
        return {'id': self.id,'username': self.username, 'email': self.email, 'password': self.password, 
        'created_date': self.created_date, 'updated_date': self.updated_date
        ,'tasks': [task.get_data_with_category_json() for task in self.tasks]}

    def get_pure_data_json(self):
        return {'id': self.id, 'username': self.username, 'email': self.email, 'password': self.password, 
        'created_date': self.created_date, 'updated_date': self.updated_date}

    ###TOdo userin olup olmadığı kontrol edilecek
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    ###TOdo gelen datanın olup olmadığı kontrol edilecek
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def add_task(self, task: 'Task'):
        self.tasks.append(task)
        db.session.commit()

    ###TOdo userin taskda olup olmadığı kontrol edilecek ###
    def add_task_by_taskid(self, i):
        task = Task.find_by_id(i)
        self.add_task(task)

    #task ve userin bağlantısını kontrol et
    def remove_task(self, task: 'Task'):
        self.tasks.remove(task)
        db.session.commit()

    #taskin belirlenen id'de olup olmadığı kontrol
    def remove_task_by_taskid(self, id):
        task = Task.find_by_id(id)
        self.remove_task(task)

    def check_password(self, password):
        return hmac.compare_digest(self.password, password)

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def get_all_users(cls):
        return cls.query.all()

#############
class Task(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    header = db.Column(db.String(100))
    description = db.Column(db.Text)
    state = db.Column(db.String(50))
    priority = db.Column(db.String(50))
    due_date = db.Column(db.String(50))
    created_date = db.Column(db.String(50))
    updated_date = db.Column(db.String(50))
    categories = db.relationship('Category', secondary=taskscategories, lazy='subquery',
        backref=db.backref('tasks', lazy=True)) 

    def __init__(self, header, description, priority, due_date):
        self.header = header
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.state = "active"

    def get_all_data_json(self):
        return {'id': self.id, 'header': self.header, 'description': self.description, 'state': self.state, 
        'priority': self.priority, 'due_date': self.due_date, 'created_date': self.created_date,
        'updated_date': self.updated_date, 'users': [user.get_pure_data_json() for user in self.users], 'categories': [category.get_pure_data_json() for category in self.categories]}

    def get_data_with_category_json(self):
        return {'id': self.id, 'header': self.header, 'description': self.description, 'state': self.state, 
        'priority': self.priority, 'due_date': self.due_date, 'created_date': self.created_date,
        'updated_date': self.updated_date, 'categories': [category.get_pure_data_json() for category in self.categories]}

    def get_pure_data_json(self):
        return {'id': self.id, 'header': self.header, 'description': self.description, 'state': self.state, 
        'priority': self.priority, 'due_date': self.due_date, 'created_date': self.created_date,
        'updated_date': self.updated_date}


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def add_user(self, user: User):
        self.users.append(user)
        db.session.commit()

    def add_user_by_userid(self, i):
        user = User.find_by_id(i)
        self.add_user(user)

    def add_category(self, category: 'Category'):
        self.categories.append(category)
        db.session.commit() 

    def add_category_by_categoryid(self, i):
        category = Category.find_by_id(i)
        self.add_category(category)  

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

############
class Category(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    created_date = db.Column(db.String(50))
    updated_date = db.Column(db.String(50))

    def __init__(self, name):
        self.name = name

    def get_all_data_json(self):
        return {'id': self.id, 'name': self.name,'created_date': self.created_date, 
        'updated_date': self.updated_date, 'tasks': [task.get_pure_data_json() for task in self.tasks]}
    
    def get_pure_data_json(self):
        return {'id': self.id, 'name': self.name,'created_date': self.created_date, 'updated_date': self.updated_date}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def add_task(self, task: Task):
        self.tasks.append(task)
        db.session.commit()

    def add_task_by_taskid(self, i):
        task = Task.find_by_id(i)
        self.add_task(task)


    def remove_task(self, task: Task):
        self.tasks.remove(task)
        db.session.commit()

    def remove_task_by_taskid(self, id):
        task = Task.find_by_id(id)
        self.remove_task(task)

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User

class TaskSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Task

class CategorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Category

##############

### ROUTES ###

##############

class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, help="Username is required", required=True)
    parser.add_argument('password', type=str, help="Password is required", required=True)
    
    def post(self):
        data = UserRegister.parser.parse_args()

        if User.find_by_username(data['username']):
            return {'message': 'Username has already been taken'}, 400

        user = User(**data)
        user.save_to_db()
        return {'message':  'User has been created successfully'}, 201


class UserPureInformation(Resource):

    def get(self, name):
        a = User.find_by_username(name)
        if not a:
            return {'message': "Could not find user with that username"}, 404
        return a.get_pure_data_json()

class UserInformation(Resource):

    def get(self, name):
        result = User.find_by_username(name)
        if not result:
            return {'message': "Could not find user with that username"}, 404
        return result.get_all_data_json()


class AllUsersInformation(Resource):

    def get(self):
        users = User.get_all_users()
        if not users:
            return {'message': "Could not find any user"}, 404
        user_schema = UserSchema(many=True)
        output = user_schema.dump(users)
        return jsonify(output)


class AllTasksInformation(Resource):

    def get(self):
        tasks = Task.query.all()
        if not tasks:
            return {'message': "Could not find any task"}, 404
        task_schema = TaskSchema(many=True)
        output = task_schema.dump(tasks)
        return jsonify(output)

class TaskInformation(Resource):

    def get(self, id):
        result = Task.find_by_id(id)
        if not result:
            return {'message': "Could not find task with that task id"}, 404
        return result.get_all_data_json()


class TaskPureInformation(Resource):

    def get(self, id):
        result = Task.find_by_id(id)
        if not result:
            return {'message': "Could not find task with that task id"}, 404
        return result.get_pure_data_json()

class TaskAdd(Resource):

    add_parser = reqparse.RequestParser()
    add_parser.add_argument('header', type=str, help="Header is required", required=True)
    add_parser.add_argument('description', type=str, help="Description is required", required=True)
    add_parser.add_argument('priority', type=str, help="Priority is required", required=True)
    add_parser.add_argument('due_date', type=str, help="Due date is required", required=True)
    

    def post(self, id):
        data = TaskAdd.add_parser.parse_args()
        user = User.find_by_id(id)

        if not user:
            return {'message': 'User could not find'}, 404

        task = Task(**data)
        task.save_to_db()
        user.add_task(task)

        return {'message':  'Task has been created successfully'}, 201



class TaskEdit(Resource):
    
    edit_parser = reqparse.RequestParser()
    edit_parser.add_argument('header', type=str, help="Header")
    edit_parser.add_argument('description', type=str, help="Description")
    edit_parser.add_argument('priority', type=str, help="Priority")
    edit_parser.add_argument('due_date', type=str, help="Due date")
    edit_parser.add_argument('state', type=str, help="State")

    
    def patch(self, id):
        data = TaskEdit.edit_parser.parse_args()
        result = Task.find_by_id(id)
        if not result:
            return {'message': "Task doesn't exist, cannot update"}, 404

        if data['header']:
            result.header = data['header']
        if data['description']:
            result.description = data['description']
        if data['priority']:
            result.priority = data['priority']
        if data['due_date']:
            result.due_date = data['due_date']
        if data['state']:
            result.state = data['state']

        db.session.commit()
        return result.get_all_data_json()

    def delete(self, id):
        result = Task.find_by_id(id)
        if not result:
            return {'message': 'Task couldnt find'}, 404       
        result.delete_from_db()
        return {'message': 'Task successfully deleted'}, 204
        
        

class AllCategoriesInformation(Resource):

    def get(self):
        categories = Category.query.all()
        if not categories:
            return {'message': "Could not find any category"}, 404
        category_schema = CategorySchema(many=True)
        output = category_schema.dump(categories)
        return jsonify(output)

class CategoryInformation(Resource):
    def get(self, id):
        result = Category.find_by_id(id)
        if not result:
            return {'message': "Could not find category with that category id"}, 404
        return result.get_all_data_json()


class CategoryPureInformation(Resource):
    def get(self, id):
        result = Category.find_by_id(id)
        if not result:
            return {'message': "Could not find category with that category id"}, 404
        return result.get_pure_data_json()


class CategoryAdd(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, help="Category name is required", required=True)

    def post(self):
        data = CategoryAdd.parser.parse_args()
    
        category = Category(**data)
        category.save_to_db()
        return {'message':  'Category has been created successfully'}, 201


class CategoryEdit(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, help="Category name")

    def patch(self, id):
        data = CategoryEdit.parser.parse_args()
        result = Category.find_by_id(id)
        if not result:
            return {'message': "Category doesn't exist, cannot update"}, 404

        if data['name']:
            result.name = data['name']

        db.session.commit()
        return result.get_all_data_json()

    def delete(self, id):
        result = Category.find_by_id(id)
        if not result:
            return {'message': "Category couldn't find"}, 404       
        result.delete_from_db()
        return {'message': 'Category successfully deleted'}, 204

class AddTaskToUser(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('task_id', type=int, help="Task id is required", required=True)

    def post(self, id):
        data = AddTaskToUser.parser.parse_args()
        user = User.find_by_id(id)

        if not user:
            return {'message': 'User could not find'}, 404

        task_id = data['task_id']
        user.add_task_by_taskid(task_id)

        return {'message':  'Task successfully assigned to user'}, 201



class AddTaskToCategory(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('task_id', type=int, help="Task id is required", required=True)

    def post(self, id):
        data = AddTaskToCategory.parser.parse_args()
        category = Category.find_by_id(id)

        if not category:
            return {'message': 'Category could not find'}, 404

        task_id = data['task_id']
        category.add_task_by_taskid(task_id)

        return {'message':  'Task successfully assigned to category'}, 201


class RemoveTaskFromUser(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('task_id', type=int, help="Task id is required", required=True)

    def delete(self, id):
        data = RemoveTaskFromUser.parser.parse_args()
        user = User.find_by_id(id)

        if not user:
            return {'message': 'User could not find'}, 404

        task_id = data['task_id']
        user.remove_task_by_taskid(task_id)

        return {'message':  'Task successfully removed from user'}, 204


class RemoveTaskFromCategory(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('task_id', type=int, help="Task id is required", required=True)

    def delete(self, id):
        data = RemoveTaskFromCategory.parser.parse_args()
        category = Category.find_by_id(id)

        if not category:
            return {'message': 'Category could not find'}, 404

        task_id = data['task_id']
        category.remove_task_by_taskid(task_id)

        return {'message':  'Task successfully removed from category'}, 204



api.add_resource(UserRegister, "/register") #POST ,parameters: username:str, password:str
api.add_resource(UserPureInformation, "/userpureinformation/<string:name>") #GET, byusername
api.add_resource(UserInformation, "/userinformation/<string:name>") #GET, byusername
api.add_resource(AllUsersInformation, "/allusersinformation") #GET, 
api.add_resource(AllTasksInformation, "/alltasksinformation") #GET, 
api.add_resource(TaskInformation, "/taskinformation/<int:id>") #GET, bytaskid
api.add_resource(TaskPureInformation, "/taskpureinformation/<int:id>") #GET, bytaskid
api.add_resource(TaskAdd, "/taskadd/<int:id>") #POST, parameters: header, description, priority, due_date; byuserid
api.add_resource(AllCategoriesInformation, "/allcategoriesinformation") #GET, 
api.add_resource(CategoryInformation, "/categoryinformation/<int:id>") #GET, bycategoryid
api.add_resource(CategoryPureInformation, "/categorypureinformation/<int:id>") #GET, bycategoryid
api.add_resource(CategoryAdd, "/categoryadd") #POST, parameters: name
api.add_resource(AddTaskToUser, "/addtasktouser/<int:id>") #POST, parameters: task_id; byuserid
api.add_resource(AddTaskToCategory, "/addtasktocategory/<int:id>") #POST, parameters: task_id; bycategoryid
api.add_resource(TaskEdit, "/taskedit/<int:id>") #PATCH,DELETE, parameters: header, description, priority, due_date; bytaskid
api.add_resource(CategoryEdit, "/categoryedit/<int:id>") #PATCH, DELETE, parameters: name; bycategoryid
api.add_resource(RemoveTaskFromUser, "/removetaskfromuser/<int:id>") #DELETE, parameters: task_id; byuserid
api.add_resource(RemoveTaskFromCategory, "/removetaskfromcategory/<int:id>") #DELETE, parameters: task_id; bycategoryid




if __name__ == "__main__":
    # db.drop_all()
    # db.create_all()
    app.run(debug=True)