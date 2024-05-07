from typing import List
from typing import Any
from dataclasses import dataclass
import json
@dataclass
class Animais:
    domesticado: str
    tipo: str

    @staticmethod
    def from_dict(obj: Any) -> 'Animais':
        _domesticado = str(obj.get("domesticado"))
        _tipo = str(obj.get("tipo"))
        return Animais(_domesticado, _tipo)

@dataclass
class PessoaIds:
    id_nome: str
    id_sexo: str
    id_cor: str

@dataclass
class PessoaDescricao:
    nome: str
    sexo: str
    cor: str

@dataclass
class PessoaPreferencias:
    prato: str
    doce: str
    bebida: str

@dataclass
class Caracteristica:
    pessoa_ids: PessoaIds
    pessoa_descricao: PessoaDescricao
    pessoa_preferencias: PessoaPreferencias

    @staticmethod
    def from_dict(obj: Any) -> 'Caracteristica':
        _pessoa_ids = PessoaIds.from_dict(obj.get("pessoa_ids"))
        _pessoa_descricao = PessoaDescricao.from_dict(obj.get("pessoa_descricao"))
        _pessoa_preferencias = PessoaPreferencias.from_dict(obj.get("pessoa_preferencias"))
        return Caracteristica(_pessoa_ids, _pessoa_descricao, _pessoa_preferencias)

    @staticmethod
    def from_dict(obj: Any) -> 'PessoaDescricao':
        _nome = str(obj.get("nome"))
        _sexo = str(obj.get("sexo"))
        _cor = str(obj.get("cor"))
        return PessoaDescricao(_nome, _sexo, _cor)

    @staticmethod
    def from_dict(obj: Any) -> 'PessoaIds':
        _id_nome = str(obj.get("id_nome"))
        _id_sexo = str(obj.get("id_sexo"))
        _id_cor = str(obj.get("id_cor"))
        return PessoaIds(_id_nome, _id_sexo, _id_cor)

    @staticmethod
    def from_dict(obj: Any) -> 'PessoaPreferencias':
        _prato = str(obj.get("prato"))
        _doce = str(obj.get("doce"))
        _bebida = str(obj.get("bebida"))
        return PessoaPreferencias(_prato, _doce, _bebida)

@dataclass
class Profissionais:
    tempo_funcao: str
    tipo_contrato: str
    nome_ultima_empresa: str

    @staticmethod
    def from_dict(obj: Any) -> 'Profissionais':
        _tempo_funcao = str(obj.get("tempo_funcao"))
        _tipo_contrato = str(obj.get("tipo_contrato"))
        _nome_ultima_empresa = str(obj.get("nome_ultima_empresa"))
        return Profissionais(_tempo_funcao, _tipo_contrato, _nome_ultima_empresa)

@dataclass
class Qualificacoes:
    profissionais: Profissionais
    animais: Animais

    @staticmethod
    def from_dict(obj: Any) -> 'Qualificacoes':
        _profissionais = Profissionais.from_dict(obj.get("profissionais"))
        _animais = Animais.from_dict(obj.get("animais"))
        return Qualificacoes(_profissionais, _animais)

@dataclass
class Root:
    topic: str
    caracteristicas: List[Caracteristica]
    qualificacoes: Qualificacoes

    @staticmethod
    def from_dict(obj: Any) -> 'Root':
        _topic = str(obj.get("topic"))
        _caracteristicas = [Caracteristica.from_dict(y) for y in obj.get("caracteristicas")]
        _qualificacoes = Qualificacoes.from_dict(obj.get("qualificacoes"))
        return Root(_topic, _caracteristicas, _qualificacoes)

# Example Usage
# jsonstring = json.loads(myjsonstring)
# root = Root.from_dict(jsonstring)
