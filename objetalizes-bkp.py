import json

from objetalize import Objetalize


payload_cli1_str = open("payload_cli1.json","r").read()

print(str(Objetalize(payload_cli1_str)))
# obj_payload = Objetalize(payload_cli1_str)
#
# obj_payload_str = json.dumps(obj_payload, default=lambda o: o.__dict__)

# print(str(type(obj_payload_str)), obj_payload_str)
# obj_payload_final = json.loads(obj_payload_str)
# print(str(type(obj_payload_final)), obj_payload_final)


