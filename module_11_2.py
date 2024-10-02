import inspect
def introspection_info(obj):
    info = {}
    info['type'] = str(type(obj))
    info['attributes'] = [attr for attr in dir(obj) if not callable(getattr(obj,attr)) and not attr.startswith('__')]
    info['methods'] = [method for method in dir(obj) if not callable(getattr(obj,method)) and not method.startswith('__')]
    info['module'] = obj.__mod__
    if hasattr(obj,'__dict__'):
        info['properties'] = vars(obj)
    return info
class InfoClass:
    def __init__(self):
        attribute1 = 'value1'
    def method1(self):
        return 'method1'
info_obj = InfoClass()
number_info = introspection_info(42)
print(number_info)

