"""
Django settings for Resturant_Project project.
"""

from pathlib import Path
import os
import dj_database_url
from dotenv import load_dotenv

# Load environment variables from the .env file (for local development)
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'fallback-secret-key-for-local-use')

# SECURITY WARNING: don't run with debug turned on in production!
# Set DEBUG to False for production environment
DEBUG = False 

# Use the Render URL and ensure it works with dynamic hosts
# Replace 'your-render-url.onrender.com' with your actual Render service URL
ALLOWED_HOSTS = [
    # FIX: The protocol 'https://' must be removed from the domain name
    'restaurant-project-1-fck3.onrender.com', 
    '127.0.0.1', 
    'localhost',
    os.environ.get('ALLOWED_HOSTS') # Good practice for reading env vars if set
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Note: Use the full project path for app inclusion in INSTALLED_APPS 
    'Resturant_Project.Base_App', 
]

# Database Configuration (CRITICAL FOR RENDER)
# Use dj-database-url to parse the DATABASE_URL provided by Render
if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.config(
            default=os.environ.get('DATABASE_URL'),
            conn_max_age=600,
            conn_health_checks=True,
        )
    }
else:
    # Local SQLite setup
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # ADDED: WhiteNoise middleware for serving static files in production
    'whitenoise.middleware.WhiteNoiseMiddleware', 
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Resturant_Project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'Template'], # Using BASE_DIR for DIRS path
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Resturant_Project.wsgi.application'

# Password validation (default block - no changes needed)
AUTH_PASSWORD_VALIDATORS = [
    # ... default validators
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# Static and Media Files (CRITICAL FOR RENDER)

STATIC_URL = 'static/'

# The directory where collectstatic will place production static files
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Extra directories to look for static files (your app's 'static' folder)
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# ADDED: Use WhiteNoise for efficient static file serving
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Custom Settings and Auth
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/login/'


# Email Settings (Using Environment Variables for Security)
# You MUST set these variables in your Render Environment dashboard
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.getenv('EMAIL_HOST', 'smtp.gmail.com')
EMAIL_PORT = int(os.getenv('EMAIL_PORT', 587))
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS', 'True') == 'True'

# Read sensitive credentials from environment variables
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL')

# Retrieve the Google Maps API key from environment variables
GOOGLE_MAPS_API_KEY = os.getenv('GOOGLE_MAPS_API_KEY')
