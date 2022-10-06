import os
import shutil

from .filemanager import init
from .setup import *

name = 'base'

class ModuleBase(PluginModuleBase):
    def __init__(self, P):
        super(ModuleBase, self).__init__(P, name=name)

    def plugin_load(self):
        config_path = os.path.join(os.path.dirname(__file__), 'RichFilemanager', 'config')
        src = os.path.join(config_path, 'filemanager.config.ff.json')
        tar = os.path.join(config_path, 'filemanager.config.json')
        if os.path.exists(tar) == False:
            shutil.copy(src, tar)

        from framework import F

        #app.config['FLASKFILEMANAGER_FILE_PATH'] = path_app_root
        F.app.config['FLASKFILEMANAGER_FILE_PATH'] = '/'
        init(F.app)

    def plugin_unload(self):
        pass

