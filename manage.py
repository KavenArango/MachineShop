from app import db,app
from apps.accounts import models
from apps.StudentPage import models
from apps.StaffPage import models
from apps.Machine import models
from flask_migrate import Migrate,Config ,MigrateCommand
from flask_script import Manager


app.config.from_object(Config)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
