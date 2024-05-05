import json

from objetalize import Objetalize

payload_cli1_str = open("payload_cli1.json","r").read()
payload_request_str = open("payload_cli1_request.json","r").read()
payload_base_str = open("payload_base.json","r").read()

res = Objetalize(payload_cli1_str, payload_base_str, payload_request_str)

print(res.str_payload_final)


