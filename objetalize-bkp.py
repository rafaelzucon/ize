import json


class Objetalize:
    def __init__(self, payload_base: str):
        self._payload_base = payload_base
        self.deserialize(self._payload_base,0)

    def type_obj(self, text: str):
        _type = []
        _type = str(text).split(' ')
        return _type[1].replace("'", "").replace(">", "")

    def deserialize(self, payload_base: str, c: int):
        payload = json.loads(payload_base)
        str_type_payload = self.type_obj(str(type(payload)))
        i = 0
        for key_base in payload:
            if "dict" not in str(type(key_base)) and "list" not in str(type(key_base)):
                key_base_arr = str(key_base).split('/')
                key_base_str = str(key_base_arr[1])
                return key_base_str
            if "dict" in str(type(payload[i] if "list" in str_type_payload else payload[key_base])) or "list" in str(
                    type(payload[i] if "list" in str_type_payload else payload[key_base])):
                self.deserialize(json.dumps(payload[i] if "list" in str_type_payload else payload[key_base], default=lambda o: o.__dict__, indent=4), c + 1)

            i = i + 1

