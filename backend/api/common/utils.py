# Pass sql object to function, convert into dictionary
def sql_to_dict(obj):
    obj = obj.__dict__
    obj.pop('_sa_instance_state', None)
    return obj