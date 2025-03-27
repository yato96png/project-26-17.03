from flask import request, jsonify
from flask_jwt_extended import JWTManager, create_access_token
from app import db, app
from models import User, Course

jwt = JWTManager(app)

def setup_routes(app):
    @app.route('/api/register', methods=['POST'])
    def register():
        data = request.json
        user = User(username=data['username'])
        user.set_password(data['password'])
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'Пользователь зарегистрирован!'})

    @app.route('/api/login', methods=['POST'])
    def login():
        data = request.json
        user = User.query.filter_by(username=data['username']).first()
        if user and user.check_password(data['password']):
            token = create_access_token(identity={'username': user.username})
            return jsonify({'token': token})
        return jsonify({'message': 'Неправильный логин или пароль'}), 401

    @app.route('/api/courses', methods=['GET'])
    def get_courses():
        courses = Course.query.all()
        return jsonify([{
            'id': course.id,
            'title': course.title,
            'description': course.description,
            'price': course.price
        } for course in courses])
