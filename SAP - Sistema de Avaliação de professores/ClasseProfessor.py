from ClasseUsuario import*
from dicionario import*
from instancias import*
from ClasseAluno import Aluno
from ClasseAvaliacao import Avaliacao
from datetime import datetime
from ClasseMural import*
from ClasseChefia import *
from ClasseProfessor import*

class Professor(UsuarioIfro):
    def __init__(self, nome, idade, login_usuario,login_senha, salario, disciplina_ministrada):
        super().__init__(nome, idade, login_usuario,login_senha)
        self.__salario = salario
        self.__disciplina_ministrada = disciplina_ministrada

    def get_avaliacao(self):
        return self.__avaliacao

    def get_salario(self):
        return(self.__salario)

    def set_salario(self,novo_salario):
        self.__salario = novo_salario

    def get_disciplina_ministrada(self):
        return(self.__disciplina_ministrada)

    def set_disciplina_ministrada(self,nova_disciplina,):
        self.__disciplina_ministrada = nova_disciplina

    def cadastrar(self):
        while True:
            nome = input("Digite seu nome: ")
            self.set_nome(nome)
            try:
                idade = int(input("Digite sua idade:"))
            except:
                print("Coloque a idade utilizando números")
                continue                                          
            self.set_idade(idade)
            login_usuario = input("Cadastre um usuário: ")
            self.set_login_usuario(login_usuario)
            login_senha = input("Cadastre uma senha: ")                        #Acrescentar um raise que, caso a senha seja menor que 8 caracteres, vai levantar um erro (Raise).
            self.set_login_senha(login_senha)
            try:
                salario = int(input("Digite seu salário: "))
            except:
                print("Coloque a idade utilizando números")                    
                continue                                    
            self.set_salario(salario)
            disciplina_ministrada = input("Digite a disciplina que você ministra: ")
            self.set_disciplina_ministrada(disciplina_ministrada)

    def visualizarMural(self,mural):
        mural.consultarAvaliacao()                                                              #Associação
        

