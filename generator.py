import json
from os import mkdir, chdir ,path
import re
from urllib.request import urlopen

def get_name(_srt):
    if _srt == 'str':
        return 'String'
    if _srt == 'bool':
        return 'Boolean'
    if _srt == 'int':
        return 'int'

def dump_parsers(_model_dict, _model_name, _file_name):

    __any_list = False
    _return_object = '\n\t\t\t' + _model_name + ' local_model = null;\n'
    _remote_parser_object_creation_lines = '\n'
    _parser_import_lines = 'import org.json.JSONArray;\nimport org.json.JSONException;\nimport org.json.JSONObject;\n'
    _class_name = '\nclass ' + _model_name + 'Parser {\n'
    _ending_symbol = '\n\t\t\t\n}'
    _parser_function_dec = '\n\t\tpublic ' + _model_name + ' parse' + _model_name + '(String json_object) {\n'
    _json_exception_block_start = '\t\t\ttry {'
    _json_exception_block_end = ' \t\t\t} \n\t\t\tcatch (JSONException e){\n\n \t\t\t\t e.printStackTrace();\n\t\t\t}\n\n\t\t\treturn local_model;\n\t\t}'
    _json_object_creation_line = '\n\t\t\t\t\tJSONObject jsobj = new JSONObject(json_object);'
    _array_list_creation = ''
    _return_object_attr = ''
    _model_init = ''

    for _t in _model_dict:

        if _model_dict[_t] == 'slist':
            __any_list = True
            _lib_ref = _t[0].capitalize() + _t[1:len(_t)]
            # _parser_import_lines += 'import ' + _lib_ref + '.java;\n'         // import issue is solved with package
            # _parser_import_lines += 'import ' + _lib_ref +'Parser.java;\n'    // -do-
            _return_object_attr += _t
            _array_list_creation += '\n\n\t\t\t\t\tArrayList<String>' + ' ' + _t + ' = new ArrayList<>();\n\t\t\t\t\tJSONArray ' + _t + '_arr = jsobj.getJSONArray("' + _t + '");\n'
            _array_list_creation += '\t\t\t\n\t\t\t\t\tfor(int i = 0 ;i<' + _t + '_arr.length()-1;i++){\n\n '
            _array_list_creation += '\t\t\t\t\t\t' + _t + '.add((String)' + _t + '_arr.get(i)));\n\n\t\t\t\t\t}'

        if _model_dict[_t] == 'ilist':
            __any_list = True
            _lib_ref = _t[0].capitalize() + _t[1:len(_t)]
            # _parser_import_lines += 'import ' + _lib_ref + '.java;\n'         // import issue is solved with package
            # _parser_import_lines += 'import ' + _lib_ref +'Parser.java;\n'    // -do-
            _return_object_attr += _t
            _array_list_creation += '\n\n\t\t\t\t\tArrayList<Integer>' + ' ' + _t + ' = new ArrayList<>();\n\t\t\t\t\tJSONArray ' + _t + '_arr = jsobj.getJSONArray("' + _t + '");\n'
            _array_list_creation += '\t\t\t\n\t\t\t\t\tfor(int i = 0 ;i<' + _t + '_arr.length()-1;i++){\n\n '
            _array_list_creation += '\t\t\t\t\t\t' + _t + '.add((int)' + _t + '_arr.get(i)));\n\n\t\t\t\t\t}'

        if _model_dict[_t] == 'list':
            __any_list = True
            _lib_ref = _t[0].capitalize() + _t[1:len(_t)]
            # _parser_import_lines += 'import ' + _lib_ref + '.java;\n'         // import issue is solved with package
            # _parser_import_lines += 'import ' + _lib_ref +'Parser.java;\n'    // -do-
            _remote_parser_object_creation_lines += '\t\t' + _lib_ref + 'ModelParser ' + _t + '_parser = new ' + _lib_ref + 'ModelParser();\n'
            _return_object_attr += _t + 's, '
            _array_list_creation += '\n\n\t\t\t\t\tArrayList<' + _lib_ref + 'Model>' + ' ' + _t + 's = new ArrayList<>();\n\t\t\t\t\tJSONArray ' + _t + '_arr = jsobj.getJSONArray("' + _t + '");\n'
            _array_list_creation += '\t\t\t\n\t\t\t\t\tfor(int i = 0 ;i<' + _t + '_arr.length()-1;i++){\n\n '
            _array_list_creation += '\t\t\t\t\t\t' + _t + 's.add(' + _t + '_parser.parse' + _lib_ref + 'Model((String)' + _t + '_arr.get(i)));\n\n\t\t\t\t\t}'

        if _model_dict[_t] in ('str','int','bool'):
            if _model_dict[_t] == 'int':
                _return_object_attr += 'jsobj.getInt("' + _t + '") , '
            else:
                _return_object_attr += 'jsobj.get' + get_name(_model_dict[_t]) + '("' + _t + '") , '

    if __any_list:
        _parser_import_lines += 'import java.util.ArrayList;\n'

    # tempting parser
    _model_init += '\n\n\t\t\t\t\tlocal_model = new ' + _model_name + '(' + _return_object_attr[
                                                                            :len(_return_object_attr) - 2] + ');\n'
    _parser_template = _parser_import_lines + _class_name + _remote_parser_object_creation_lines + _parser_function_dec + _return_object + _json_exception_block_start + _json_object_creation_line + _array_list_creation + _model_init + _json_exception_block_end + _ending_symbol

    with open(_file_name, 'w') as f:
        f.write(_parser_template)
        f.close()

def dump_model(_model_dict, _model_name, _file_name):
    _import_lines = ''
    _attrs_dec = ''  # fields
    _const_params = ''
    _cons_assignments = ''
    __any_list = False

    # templating import statements
    for _t in _model_dict:
        if _model_dict[_t] =='slist':
            __any_list = True
            # _import_lines += 'import '+_lib_ref+'.java;\n'
            _attrs_dec += '\t\tpublic ArrayList<String> ' + _t + ';\n'
            _const_params += 'ArrayList<String> ' + _t + ', '
            _cons_assignments += '\t\tthis.' + _t + ' = ' + _t + ';\n'

        if _model_dict[_t] == 'ilist':
            __any_list = True
            # _import_lines += 'import '+_lib_ref+'.java;\n'
            _attrs_dec += '\t\tpublic ArrayList<Integer> ' + _t + ';\n'
            _const_params += 'ArrayList<Integer> ' + _t + ', '
            _cons_assignments += '\t\tthis.' + _t + ' = ' + _t + ';\n'

        if _model_dict[_t] == 'list':
            __any_list = True
            _lib_ref = _t[0].capitalize() + _t[1:len(_t)]
            # _import_lines += 'import '+_lib_ref+'.java;\n'
            _attrs_dec += '\t\tpublic ArrayList<' + _lib_ref + 'Model> ' + _t + ';\n'
            _const_params += 'ArrayList<' + _lib_ref + 'Model> ' + _t + ', '
            _cons_assignments += '\t\tthis.' + _t + ' = ' + _t + ';\n'

        if _model_dict[_t] in ('str','int','bool'):
            _attrs_dec += '\t\tpublic ' + get_name(_model_dict[_t]) + ' ' + _t + ';\n'
            _const_params += get_name(_model_dict[_t]) + ' ' + _t + ', '
            _cons_assignments += '\t\tthis.' + _t + ' = ' + _t + ';\n'

    if __any_list:
        _import_lines = 'import java.util.ArrayList;\n' + _import_lines

    _class_name = 'class ' + _model_name + ' {\n'
    _ending_symbol = '\n}'

    # templating constructor items
    _const_dec = 'public ' + _model_name + '(' + _const_params[
                                                 :len(_const_params) - 2] + ') {\n\n' + _cons_assignments + '\n\t}\n'

    # templating model
    model_template = _import_lines + '\n' + _class_name + '\n' + _attrs_dec + '\n' + _const_dec + _ending_symbol

    with open(_file_name, 'w') as f:
        f.write(model_template)
        f.close()

def create_base(_json, _model_name):
    _dict = {}
    _json_dict = json.loads(_json)

    # preparing dictionary
    for _key in _json_dict:

        if type(_json_dict[_key]) is str:
            _dict[_key] = 'str'

        if type(_json_dict[_key]) is list:

            # check for type-array or json object array
            _suspect_json = json.dumps(list(_json_dict[_key])[0])

            if _suspect_json[0] == '"':
                _dict[_key] = 'slist'

            if _suspect_json[0] == '{':
                _dict[_key] = 'list'
                _new_model_name = _key[0].capitalize() + _key[1:len(_key)]
                _new_json = _suspect_json
                create_base(_new_json, _new_model_name)
            else:
                _dict[_key] = 'ilist'

        if type(_json_dict[_key]) is bool:
            _dict[_key] = 'bool'

        if type(_json_dict[_key]) is int:
            _dict[_key] = 'int'

    _model_name += 'Model'
    _parser_file_name = _model_name + 'Parser.java'
    _model_file_name = _model_name + '.java'

    dump_model(_dict, _model_name, _model_file_name)
    dump_parsers(_dict, _model_name, _parser_file_name)

def re_format_json(_json):

    _obs = '\r\n'
    _json = re.compile(_obs).sub(' ',_json)
    data = json.loads(_json)
    if json.dumps(list(data)[0])[0] == '{':
        _target_json = '{"j_array" :' + _json + '}'
        return _target_json
    else:
        return _json

# =====================================#
#            function calls            #
# =====================================#

#TODO:    Option 1 :   substitute url with your api below
#TODO:    Option 2 :   place your local json between three quoutes

#TODO                              =================-----------  And You Set To Go  -----------------=====================

#========#
#Option 1#
#========#
# _url = 'www.example.com/api'
# _target_json  = str(urlopen(_url).read())


#=========#
#Option 2 #
#=========#
#_target_json = """<Your Json Here>"""

_target_json = re_format_json(_target_json)
if not path.isdir('Parsers'):
    mkdir('Parsers')
chdir('Parsers')
create_base(_target_json, 'Root')
