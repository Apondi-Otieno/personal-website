import os

class Config:
  SQLALCHEMY_TRACK_MODIFICATIONS=True
  SECRET_KEY = os.environ.get('SECRET_KEY')
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://access:1234@localhost/bblog'
  #Simplemde cofigurations
  SIMPLEMDE_JS_IIFE = True
  SIMPLEMDE_USE_CDN = True