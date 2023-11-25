import os
from dotenv import load_dotenv

load_dotenv()
class Config:
    SECRET_KEY = 'my super secret key'
    # SECRET_KEY = os.getenv('SECRET_KEY')
    # SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_DATABASE_URI = 'postgresql://mrfjugvxzfetrd:4e96fc336363481d99919d509fccd7c3f043fdf8a8da91090388b34be79ec2b7@ec2-54-156-8-21.compute-1.amazonaws.com:5432/da7c29vbu8krn7'
    MAIL_SERVER  = 'smtp.googlemail.com'
    MAIL_PORT  = 587
    MAIL_USE_TLS  = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD  = os.environ.get('EMAIL_PASS')