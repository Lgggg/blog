from flask_script import Manager, Server
import main
import models

manager = Manager(main.app)

manager.add_command("server", Server(host='0.0.0.0', port=8080))

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
    )

if __name__ == '__main__':
    manager.run()
