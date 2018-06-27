from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import app, db

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

@manager.command
def run(host='127.0.0.1', port=5000, debug=True):
    app.run(host, port, debug)

if __name__ == '__main__':
    manager.run()