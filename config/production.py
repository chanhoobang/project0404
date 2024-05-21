from config.default import *
from logging.config import dictConfig

SQLALCHEMY_DATABASE_URI = "sqlite:///{}".format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY=b'\xb1\x15\x83\x906\xd4\x9c\x8e\x07\xa7\x9eF\xc8|-\x94'

dictConfig(
    {
        "version": 1,
        "formatters": {
            "default": {
                "format": "[%(asctime)s in %(module)s: %(message)s]"
            }

        },
        "handlers": {
            "file":{
                "level": "info",
                "class": "logging.handlers.RotatingFileHandler",
                "filename": os.path.join(BASE_DIR, 'logs/project0404.log'),
                "maxBytes": 1*1024*1024*5,
                "backupCount": 5,
                "formatter": "default"
            }
        },
        "foot": {
            "level": "info", # debug -> info -> warning -> error -> critical
            "handlers": ["file"]
        }
    }
)