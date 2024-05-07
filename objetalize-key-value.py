import json


class Objetalize:
    def __init__(self, text: str):
        self._text = text
        self.deserialize(self._text,0)

    def type_obj(self, text: str):
        _type = []
        _type = str(text).split(' ')
        return _type[1].replace("'", "").replace(">", "")

    def deserialize(self, text: str, c: int):
        payload = json.loads(text)
        str_type_payload = self.type_obj(str(type(payload)))
        i = 0
        for key in payload:
            if "dict" not in str(type(key)) and "list" not in str(type(key)):
                return str(key)
            if "dict" in str(type(payload[i] if "list" in str_type_payload else payload[key])) or "list" in str(
                    type(payload[i] if "list" in str_type_payload else payload[key])):
                self.deserialize(json.dumps(payload[i] if "list" in str_type_payload else payload[key], default=lambda o: o.__dict__, indent=4), c + 1)
            else:
                return str(payload[i] if "list" in str_type_payload else payload[key])

            i = i + 1

