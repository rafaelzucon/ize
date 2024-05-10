import json

from objetalize import Objetalize

payload_cli1_str = open("payload_cli1.json","r").read()
payload_request_str = open("payload_cli1_request.json","r").read()
payload_base_str = open("payload_base.json","r").read()

print(payload_request_str)
print("\n")

res = Objetalize(payload_cli1_str, payload_base_str, payload_request_str)

# print(json.dumps(res.payload_final, indent=4))


