import os
__menu = {
    'uri': __package__,
    'name': '파일 매니저',
}

try:
    import flaskcode
    __setting_menu = {
        'uri': f"flaskcode?open={os.path.join(os.path.dirname(__file__), 'RichFilemanager', 'config', 'filemanager.config.json')}",
        'name': '파일매니저 설정',
    }
except: 
    __setting_menu = None

setting = {
    'filepath' : __file__,
    'use_db': False,
    'use_default_setting': False,
    'home_module': None,
    'menu': __menu,
    'setting_menu': __setting_menu,
    'default_route': None,
}

from plugin import *

P = create_plugin_instance(setting)
from .filemanager import filemanager_blueprint as blueprint

P.blueprint = blueprint

from framework import F, login_required

from .mod_base import ModuleBase

P.set_module_list([ModuleBase])



@P.blueprint.route('/setting', methods=['GET', 'POST'])
@login_required
def second_menu():
    from flask import request
    return P.module_list[0].process_menu('', request)

@P.blueprint.route('/ajax/<sub>', methods=['GET', 'POST'])
@login_required
def ajax(sub):
    if sub == 'setting_save':
        ret = P.ModelSetting.setting_save(request)
        for module in P.module_list:
            module.setting_save_after()
        return jsonify(ret)
