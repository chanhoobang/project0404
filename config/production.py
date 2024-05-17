from config.default import *

SQLALCHEMY_DATABASE_URI = "sqlite:///{}".format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY=b'\xb1\x15\x83\x906\xd4\x9c\x8e\x07\xa7\x9eF\xc8|-\x94'