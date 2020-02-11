import json
class Obj():
	def __init__(self,name):
		self.name = name

def read_json(json_file_direction="obj.json"):
	json_file = open(json_file_direction,"r")
	return json.load(json_file)

def read_znach(obj1):
	cl_ret = []
	for i in obj1.keys():
		cl_ret.append(Obj(i))
		for j in obj1[i].keys():
			cl_ret[-1].__setattr__(str(j),str(obj1[i][j]))

	return cl_ret

