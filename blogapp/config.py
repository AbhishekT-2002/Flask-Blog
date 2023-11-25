import os
from dotenv import load_dotenv

load_dotenv()
class Config:
    SECRET_KEY = 'my super secret key'
    # SECRET_KEY = os.getenv('SECRET_KEY')
    # SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_DATABASE_URI = 'postgresql://mpmuxidhaekftp:0969c6b91cea6949f11af3217340d15e79d7d08db88302b130b1610afe6b2b0f@ec2-44-213-228-107.compute-1.amazonaws.com:5432/d92kavj4prbqok'
    MAIL_SERVER  = 'smtp.googlemail.com'
    MAIL_PORT  = 587
    MAIL_USE_TLS  = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD  = os.environ.get('EMAIL_PASS')