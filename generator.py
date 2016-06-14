import json
from os import mkdir , chdir


def getName(_srt ):
    if _srt == 'str':
        return 'String'
    if _srt == 'bool':
        return 'Boolean'
    if _srt == 'int':
        return 'int'

def dumpParsers(_model_dict, _model_name , _file_name):

    __any_list = False
    _return_object ='\n\t\t\t'+ _model_name+' local_model = null;\n'
    _remote_parser_object_creation_lines = '\n'
    _parser_import_lines ='import org.json.JSONArray;\nimport org.json.JSONException;\nimport org.json.JSONObject;\n'
    _class_name = '\nclass ' + _model_name + 'Parser {\n'
    _ending_symbol = '\n\t\t\t\n}'


    _parser_function_dec = '\n\t\tpublic '+_model_name +' parse'+_model_name+'(String json_object) {\n'
    _json_exception_block_start = '\t\t\ttry {'
    _json_exception_block_end = ' \t\t\t} \n\t\t\tcatch (JSONException e){\n\n \t\t\t\t e.printStackTrace();\n\t\t\t}\n\n\t\t\treturn local_model;\n\t\t}'
    _json_object_creation_line = '\n\t\t\t\t\tJSONObject jsobj = new JSONObject(json_object);'
    _array_list_creation = ''
    _return_object_attr = ''
    _model_init = ''
    _lib_ref =''
#                ArrayList<Model2> model2s = new ArrayList<>();
                #JSONArray model2_arr = jobj.getJSONArray("array_key");
                #for(int i =0;i<model2_arr.length()-1;i++){
                 #   model2s.add(model2_parser.parseModel2(model2_arr.get(i));
                #}


    for _t in _model_dict:
        if _model_dict[_t] == 'list':
            __any_list = True
            _lib_ref = _t[0].capitalize() + _t[1:len(_t)]
           # _parser_import_lines += 'import ' + _lib_ref + '.java;\n'
           # _parser_import_lines += 'import ' + _lib_ref +'Parser.java;\n'

            _remote_parser_object_creation_lines += '\t\t'+_lib_ref + 'Parser '+_t + '_parser = new '+ _lib_ref + 'Parser();\n'

            _return_object_attr += _t+'s, '
            _array_list_creation += '\n\n\t\t\t\t\tArrayList<'+_lib_ref+'>'+' '+_t+'s = new ArrayList<>();\n\t\t\t\t\tJSONArray '+_t+'_arr = jsobj.getJSONArray("'+_t+'");\n'
            _array_list_creation += '\t\t\t\n\t\t\t\t\tfor(int i = 0 ;i<'+_t+'_arr.length()-1;i++){\n\n '
            _array_list_creation +='\t\t\t\t\t\t'+ _t+'s.add('+_t+'_parser.parse'+_lib_ref+'((String)'+_t+'_arr.get(i)));\n\n\t\t\t\t\t}'

        else:
            if _model_dict[_t] == 'int':
                _return_object_attr += 'jsobj.getInt("'+_t+'") , '
            else:
                _return_object_attr += 'jsobj.get'+getName(_model_dict[_t])+'("'+_t + '") , '

    if __any_list:
        _parser_import_lines+='import java.util.ArrayList;\n'
    #templating parser
    _model_init += '\n\n\t\t\t\t\tlocal_model = new ' + _model_name + '(' + _return_object_attr[:len(_return_object_attr)-2] + ');\n'
    _parser_template = _parser_import_lines+_class_name+_remote_parser_object_creation_lines+_parser_function_dec+_return_object+_json_exception_block_start+_json_object_creation_line+_array_list_creation+_model_init+_json_exception_block_end+_ending_symbol
    with open(_file_name , 'w') as f:
        f.write(_parser_template)
    print(_parser_template)

def dumpModel(_model_dict ,_model_name  , _file_name):

    _import_lines = ''
    _attrs_dec = ''             # fields
    _const_params =''
    _cons_assignments =''
    __any_list = False
    # templating import statements
    for _t in _model_dict:
        if _model_dict[_t] == 'list':
            __any_list = True
            _lib_ref = _t[0].capitalize()+_t[1:len(_t)]
           # _import_lines += 'import '+_lib_ref+'.java;\n'
            _attrs_dec +='\t\tpublic ArrayList<'+_lib_ref+'> '+ _t+';\n'
            _const_params += 'ArrayList<'+_lib_ref+'> '+ _t +', '
            _cons_assignments += '\t\tthis.'+_t+' = '+_t+';\n'
        else:
            _attrs_dec += '\t\tpublic ' + getName(_model_dict[_t]) +' '+_t+';\n'
            _const_params += getName(_model_dict[_t]) + ' ' + _t + ', '
            _cons_assignments += '\t\tthis.' + _t + ' = ' + _t + ';\n'

    if __any_list:
        _import_lines = 'import java.util.ArrayList;\n' + _import_lines
     # templating class names[0].capitalize()+s[1:len(s)]

    _class_name = 'class '+_model_name+' {\n'
    _ending_symbol = '\n}'
    #templating constructor items
    _const_dec = 'public '+_model_name+'('+_const_params[:len(_const_params)-2]+') {\n\n'+_cons_assignments+'\n\t}\n'





    #templating model
    model_template = _import_lines+'\n'+_class_name +'\n'+_attrs_dec +'\n' + _const_dec + _ending_symbol

    with open(_file_name , 'w') as f:
        f.write(model_template)
        print(model_template)


def createModel(_json , _model_name):

    file_name = _model_name + '.java'
    with open(file_name,'w') as model_f:
        model_f.write('')

    _dict = {}
    _json_dict = json.loads(_json)

    # preparing dictionary

    for _key in _json_dict:

        if type(_json_dict[_key]) is str:
            _dict[_key] = 'str'
        if type(_json_dict[_key]) is list:
            _dict[_key] = 'list'

            #recurssive model creation
            _new_model_name = _key[0].capitalize()+_key[1:len(_key)]
            _new_json = json.dumps(list(_json_dict[_key])[0])
            createModel(_new_json,_new_model_name)
        if type(_json_dict[_key]) is bool:
            _dict[_key] = 'bool'
        if type(_json_dict[_key]) is int:
            _dict[_key] = 'int'

        #print(_dict)
    dumpModel(_dict , _model_name , file_name)
    dumpParsers(_dict , _model_name ,_model_name+'Parser.java')
#=====================================#
#            function calls           #
#=====================================#

#mkdir('Files')
#chdir('Files')

sample = '{"search_type":"lyrics","status_code":200,"results":[{ "terms":[{"t_id":"t1","t_desc":"nothing:"}],"title":"Sanam re","sub_text":"sanam re , tu mera sanam hua re"}],"artist":[{"fname":"arjit","lname":"singh"}]}'

data = json.loads(sample)
#print(json.dumps(list(data['results'])[0]))
mkdir('Parsers')
chdir('Parsers')
createModel(sample,'model')
