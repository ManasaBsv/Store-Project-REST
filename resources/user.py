from flask_restful import Resource,reqparse
from models.user import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('username',
    type = str,
    required = True,
    help = 'This field cannot be left empty')
    parser.add_argument('password',
    type = str,
    required = True,
    help = 'This field cannot be left empty')


    def post(self):
        data = UserRegister.parser.parse_args()
        user = UserModel.find_by_username(data['username'])
        if user:
            return {'message': 'Record with the username, {} already exists'.format(data['username'])},400
        else:
            user = UserModel(**data)
            user.save_to_db()
            return {'message':'Record saved to database succesfully'},201  #status code 201 for succesful creation