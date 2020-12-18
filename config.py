import os
from dotenv import load_dotenv


load_dotenv()

DATABASES = {
    'ENGINE': 'psycopg2',
    'HOST': os.getenv("DATABASE_HOST"),
    'USER': os.getenv("DATABASE_USER"),
    'PASSWORD': os.getenv("DATABASE_PWD"),
    'NAME': os.getenv("DATABASE_NAME"),
    'PORT': 5432
}

MS_ACCESS_KEY = os.getenv("MS_ACCESS_KEY")
