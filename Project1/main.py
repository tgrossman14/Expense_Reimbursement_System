from src.app import flask_app, sess
from src.controllers import employee_controller, manager_controller, login_controller

if __name__ == '__main__':
    flask_app.secret_key = "cynic"
    flask_app.config['SESSION_TYPE'] = 'filesystem'
    sess.init_app(flask_app)
    flask_app.run(debug=True)

