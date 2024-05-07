import json


class Objetalize:
    def __init__(self, text: str, text_base: str, text_request: str):
        self._text = text
        self._base = text_base
        self._text_request = text_request
        self.str_payload_final: str
        self.str_payload_final = ""
        self.deserialize(self._text_request, self._base, self._text,"", "",0)

    def type_obj(self, text: str):
        _type = []
        _type = str(text).split(' ')
        return _type[1].replace("'", "").replace(">", "")

    def is_object(self, text):
        return bool("dict" in str(type(text)) or "list" in str(type(text)))

    def deserialize(self, text_request, text_base: str, text: str, last_key: str, last_type: str, c: int):
        payload_request = json.loads(text_request)
        payload_base = json.loads(text_base)
        payload = json.loads(text)
        txt_tab = ""
        for i in range(c):
            txt_tab += "\t "
        str_type_payload = self.type_obj(str(type(payload)))
        str_type_payload_base = self.type_obj(str(type(payload_base)))
        str_type_payload_req = self.type_obj(str(type(payload_request)))
        n=0
        for key_req in payload_request:
            i = 0
            for key in payload:
                j = 0
                for key_base in payload_base:
                    if not self.is_object(key_req):
                        if str(str(key).split('/')[0]).strip() == key_req and str(str(key).split('/')[1]).strip() == key_base:
                            chave = '"' + str(key_base).strip() + '" : '
                            if "dict" in self.type_obj(
                                    str(type(payload_request[n] if "list" in str_type_payload_req else payload_request[
                                        key_req]))
                            ) and "dict" in self.type_obj(
                                str(type(payload[i] if "list" in str_type_payload else payload[key]))
                            ) and "dict" in self.type_obj(str(type(
                                payload_base[j] if "list" in str_type_payload_base else payload_base[key_base]))):
                                chave += "{"
                            if "list" in self.type_obj(
                                    str(type(payload_request[n] if "list" in str_type_payload_req else payload_request[key_req]))
                            ) and "list" in self.type_obj(
                                str(type(payload[i] if "list" in str_type_payload else payload[key]))
                            ) and "list" in self.type_obj(str(type(payload_base[j] if "list" in str_type_payload_base else payload_base[key_base]))):
                                chave += "[{"
                            valor = '"' + str(payload_request[key_req]) + '",\n' if not self.is_object(payload_request[key_req]) else str("")
                            self.str_payload_final += chave + valor
                    if "dict" in str(type(payload_request[n] if "list" in str_type_payload_req else payload_request[key_req])) or "list" in str(
                            type(payload_request[n] if "list" in str_type_payload_req else payload_request[key_req])):
                        self.deserialize(
                            json.dumps(payload_request[n] if "list" in str_type_payload_req else payload_request[key_req], default=lambda o: o.__dict__, indent=4),
                            json.dumps(payload_base[j] if "list" in str_type_payload_base else payload_base[key_base], default=lambda o: o.__dict__, indent=4),
                            json.dumps(payload[i] if "list" in str_type_payload else payload[key], default=lambda o: o.__dict__, indent=4),
                            last_key if '{' in str(key_req).strip()[-len(str(key_req).strip())] else str(key_req),
                            str(self.type_obj(str(type(payload_request[n] if "list" in str_type_payload_req else payload_request[key_req])))), c + 1)
                    j = j + 1
                i = i + 1
            n = n + 1
