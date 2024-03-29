class Config(object):
    """Base config class"""
    pass

class ProdConfig(Config):
    """Production config class"""
    pass

class DevConfig(Config):
    """Development config class"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Cjl_123456@127.0.0.1:3306/blog'
