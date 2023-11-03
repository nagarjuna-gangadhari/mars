from .base import *
import environ
env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
DEBUG = False

if env('ENV')=='DEV': DEBUG = True