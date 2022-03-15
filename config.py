import os

class Config:
  SQLALCHEMY_TRACK_MODIFICATIONS=True
  SECRET_KEY = os.environ.get('SECRET_KEY')
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://access:1234@localhost/bblog'
  #Simplemde cofigurations
  SIMPLEMDE_JS_IIFE = True
  SIMPLEMDE_USE_CDN = True
  
   #Email configurations
  MAIL_SERVER = 'smtp.googlemail.com'
  MAIL_PORT = 587
  MAIL_USE_TLS = True
  MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
  MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
  #PHOTOS UPLOAD CONFIGURATION
  url = 'http://quotes.stormconsultancy.co.uk/random.json'
  UPLOADED_PHOTOS_DEST = 'app/static/photos'
  @staticmethod
  def init_app(app):
        pass