import json

from objetalize import Objetalize
from ize.payload_base import PayloadBase, Qualificacoes, Profissionais, Caracteristicas, PessoaIds, Animais, PessoaDescricao, PessoaPreferencias


qualificacoes = Qualificacoes(Profissionais(tempo_funcao=2, tipo_contrato="CLT", nome_ultima_empresa="BMW"), Animais(domesticado="não", tipo="felino"))
caracteristicas = Caracteristicas(pessoa_ids=PessoaIds(id_nome=1, id_sexo=1, id_cor=3), pessoa_descricao=PessoaDescricao(nome="Asdrubal", sexo="masculino",cor="caucasiano"), pessoa_preferencias=PessoaPreferencias(prato="feijoada",doce="brigadeiro", bebida="cerveja"))
payload = PayloadBase("Pessoa",[caracteristicas], qualificacoes)

# Serialization
json_data = json.dumps(payload, default=lambda o: o.__dict__)
# print(str(type(json_data)), json_data)
obj_payload = Objetalize(json_data)
# print(str(type(obj_payload)), obj_payload)

retoro_json=json.dumps(obj_payload, default=lambda o: o.__dict__)
print(str(retoro_json))
print(str(type(retoro_json)), retoro_json)
payload_final_json=json.loads(retoro_json)
print(payload_final_json)
