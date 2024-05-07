import json
from functools import reduce

# objRs = reduce((lambda x, y: x + y), [1, 1, 1, 1])
# print(str(type(objRs)), str(objRs))

obj_list = [1,2,3,4,5,6]
obj_str=' '.join(str(e) for e in obj_list)
# print(obj_str)

json_str = '{"topic": "nome_topico", "caracteristicas" : [{ "id": 1, "total": 50.00 }, { "id": 2, "total": 70.00 }]}';
json_obj = json.loads(json_str);

obj_map = (map((lambda x: x), json_obj))
obj_str = ' '.join(str(e) for e in obj_map)
# print(str(type(obj_str)), str(obj_str))

json_str = open("teste.json","r").read()
data = json.loads(json_str)
h = list(filter(
    lambda i: i['Key'] == "Project",
    filter(
        lambda x: x['Key'],
        [e for elements in list(map(
            lambda y: y['Tags'],
            data['Vpcs'])) for e in elements
         ]
    )
))
print(str(type(h)), str(h), h)