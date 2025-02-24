import os
from flask import Flask

app = Flask(__name__)
app.config.from_object('bikers.default_settings')

if not app.debug:
    import logging
    from logging.handlers import TimedRotatingFileHandler
    file_handler = TimedRotatingFileHandler(os.path.join(app.config['LOG_DIR'], 'bikers.log'), 'midnight')
    file_handler.setLevel(logging.WARNING)
    file_handler.setFormatter(logging.Formatter('<%(asctime)s> <%(levelname)s> %(message)s'))
    app.logger.addHandler(file_handler)

import bikers.views
