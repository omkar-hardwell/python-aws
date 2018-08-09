"""Application setup."""
import configs

from flask import Flask


# Application instance
app = Flask(configs.APP_NAME)
