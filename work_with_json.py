import json
class Obj():
	def __init__(self,name):
		self.name = name

def read_json(json_file_direction="obj.json"):
	json_file = open(json_file_direction,"r")
	return json.load(json_file)

def json_obj_to_class(json_obj,atr):
	return_class = Obj(json_obj["name"])
	for i in atr:
		if i in json_obj.keys():
			return_class.__setattr__(i,json_obj[i])
		
		else:
			return_class.__setattr__(i,None)

	return return_class

def return_class(json_file_direction1,atr1):
	obj_list_1 = read_json(json_file_direction1)
	obj_list = dict()
	for i in obj_list_1.keys():
		cl = json_obj_to_class(obj_list_1[i],atr1)
		obj_list.update({cl.name:cl})

	return obj_list