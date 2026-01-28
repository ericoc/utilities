from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "Example123!"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ("utilities.ericoc.com",)

REST_FRAMEWORK = {"COERCE_DECIMAL_TO_STRING": False}

# Application definition
INSTALLED_APPS = (
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "apps.CoreConfig",
    "apps.ElectricConfig",
    "apps.NaturalGasConfig",
    "apps.WaterConfig"
)

LOGIN_REDIRECT_URL = "/add/"
LOGIN_URL = "/admin/login/"
LOGOUT_URL = "/admin/logout/"

MIDDLEWARE = (
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
)

ROOT_URLCONF = "urls"
SITE_ID = 1

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "apps.core.contexts.contexts",
            ],
        },
    },
]

WSGI_APPLICATION = "wsgi.application"

# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": Path(Path(BASE_DIR), Path("utilities.sqlite3")),
        "SCHEMA": "utilities",
    },
}

UTILITIES = {
    "electric": {
        "color": "#e4a11b",
        "datatables_fmt": "datetime('DDDD, tt')",
        "icon": "lightbulb",
        "long": "Kilowatt-Hours",
        "page_length": "24",
        "short": "kWh",
        "thresholds": (1, 0.75, 0.5),
        "title": "Electric",
    },
    "natural_gas": {
        "color": "#853cfd",
        "datatables_fmt": "datetime('MMMM y')",
        "icon": "fan",
        "long": "Hundreds of Cubic Feet",
        "page_length": "12",
        "short": "CCF",
        "thresholds": (50, 25, 10),
        "title": "Natural Gas",
    },
    "water": {
        "color": "#2caffe",
        "datatables_fmt": "date('DDDD')",
        "icon": "droplet",
        "long": "Gallons",
        "page_length": "30",
        "short": "gal",
        "thresholds": (100, 75, 50),
        "title": "Water",
    },
}

# Password validation
AUTH_PASSWORD_VALIDATORS = (
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
)

# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "America/New_York"
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = "static/"
STATIC_ROOT = Path(BASE_DIR, STATIC_URL)

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

# peco_electric_usage_interval_data_Service 1_1_2023-01-21_to_2023-12-07.csv
ELECTRIC_PREFIX = "peco_electric_usage_interval_data_Service"
# UsageData12142024.xlsx (UsageDataMMDDYYYY.xlsx)
NATURAL_GAS_PREFIX = "UsageData"
WATER_FILENAME = "ChartData.csv"

USAGE_FILE_SUFFIXES = ("csv", "xlsx")

TIME_FMT = '%A, %B %d, %Y @ %I:%M:%S %p %Z %z'
WEBSITE_TITLE = "Utilities"
