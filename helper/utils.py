import os


def substitute_env_variables_in(value):
    return os.path.normpath(os.path.expanduser(value))


def apply_func_to_dict(dict_obj, func):
    for key, value in dict_obj.iteritems():
        if isinstance(value, dict):
            apply_func_to_dict(value, func=substitute_env_variables_in)
        else:
            try:
                dict_obj[key] = func(value)
            except:
                dict_obj[key] = value
    return dict_obj


