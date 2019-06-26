from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand

import main
import models

manager = Manager(main.app)
migrate = Migrate(main.app, models.db)

manager.add_command("server", Server(host='0.0.0.0', port=8080))
manager.add_command("db", MigrateCommand)

@manager.shell
def make_shell_context():
    """create a python client,
    return default imoprt obj
    type: dict
    """
    return dict(
            app  = main.app,
            db   = models.db,
            User = models.User,
            Post = models.Post,
            Comment = models.Comment,
            Tag = models.Tag
    )

if __name__ == '__main__':
    manager.run()
