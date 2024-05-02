from typing import List
import json


class Caracteristicas(object):
    def __init__(self, pessoa_ids: object, pessoa_descricao: object, pessoa_preferencias: object):
        self.pessoa_ids = pessoa_ids
        self.pessoa_descricao = pessoa_descricao
        self.pessoa_preferencias = pessoa_preferencias

    def caracteristicas(self):
        caracteristicas = [self.pessoa_ids, self.pessoa_descricao, self.pessoa_preferencias]
        return caracteristicas


class PessoaIds(object):
    def __init__(self, id_nome: int, id_sexo: int, id_cor: int):
        self.id_nome = id_nome
        self.id_sexo = id_sexo
        self.id_cor = id_cor


class PessoaDescricao(object):
    def __init__(self, nome: str, sexo: str, cor: str):
        self.nome = nome
        self.sexo = sexo
        self.cor = cor


class PessoaPreferencias(object):
    def __init__(self, prato: str, doce: str, bebida: str):
        self.prato = prato
        self.doce = doce
        self.bebida = bebida



class Qualificacoes(object):
    def __init__(self, profissionais: object, animais: object):
        self.profissionais = profissionais
        self.animais = animais


class Profissionais(object):
    def __init__(self, tempo_funcao: int, tipo_contrato: str, nome_ultima_empresa: str):
        self.tempo_funcao = tempo_funcao
        self.tipo_contrato = tipo_contrato
        self.nome_ultima_empresa = nome_ultima_empresa


class Animais(object):
    def __init__(self, domesticado: str, tipo: str):
        self.domesticado = domesticado
        self.tipo = tipo


class PayloadBase(object):
    def __init__(self, topic: str, caracteristicas: List[Caracteristicas], qualificacoes: object):
        self.topic = topic
        self.caracteristicas = caracteristicas
        self.qualificacoes = qualificacoes


