# -*- coding: utf-8 -*-
"""
Rich File Manager for Flask
"""
from .filemanager import filemanager_blueprint as blueprint
from .filemanager import init, set_access_control_function

__author__ = 'Stephen Brown (Little Fish Solutions LTD)'
"""

plugin_info = {
    'version' : '1.0.0',
    'name' : '파일 매니저',
    'category_name' : 'system',
    'icon' : '',
    'developer' : 'soju6jan',
    'description' : 'RichFilemanager를 Flask에서 동작하도록 한 FlaskFileManager 포크',
    'home' : 'https://github.com/soju6jan/flaskfilemanager',
    'more' : '',
}
"""
