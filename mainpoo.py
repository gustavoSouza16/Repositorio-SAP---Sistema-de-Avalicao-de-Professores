#2°Ano Vespertino - Informática, Programação Orientada a Objetos
#Integrantes: Gabriel Lima Rosa, Gustavo Neves, Luiz Guilherme, Wellington Pereira
from ClasseAluno import*
from ClasseProfessor import*
from ClasseUsuario import*
from dicionario import*
from instancias import*
from ClasseMural import*
from ClasseAvaliacao import*
from ClasseChefia import*

# mural = Mural()

while True:
  print("-" * 12, "MENU DO SAP", "-" * 12)
  print("\n1 - Cadastrar Usuário\n2 - Logar com uma conta\n3 - Sair")
  opcao = input(">")

  if opcao == "1":
    print("\nCadastrar como:\n[1] - Aluno\n[2] - Professor\n[3] - Chefe Imediato")
    cadastrar_usuario = input("Coloque sua resposta:\n> ")

    if cadastrar_usuario == "1":
      criar_usuario_obj = Aluno(0,0,0,0,0,0)
      criar_usuario_obj.cadastrar()
      dicionario_de_usuario_alunos_cadastrados[criar_usuario_obj.get_login_usuario()] = f"{criar_usuario_obj.get_nome()}", (criar_usuario_obj.get_idade()), f"{criar_usuario_obj.get_login_usuario()}", f"{criar_usuario_obj.get_login_senha()}", f"{criar_usuario_obj.get_ano_escolar()}", f"{criar_usuario_obj.get_curso()}"
      print(f"Você foi cadastrado {criar_usuario_obj.get_nome()}")

    elif cadastrar_usuario == "2":
      criar_usuario_obj = Professor(0,0,0,0,0,0)
      criar_usuario_obj.cadastrar()
      dicionario_de_profs_cadastrados[criar_usuario_obj.get_login_usuario()] = f"{criar_usuario_obj.get_nome()}", criar_usuario_obj.get_idade(), f"{criar_usuario_obj.get_login_usuario()}", f"{criar_usuario_obj.get_login_senha()}", criar_usuario_obj.get_salario() , f"{criar_usuario_obj.get_disciplina_ministrada()}"
      print(f"Você foi cadastrado {criar_usuario_obj.get_nome()}")

    elif cadastrar_usuario == "3":
      criar_usuario_obj = ChefiaImediata(0,0,0,0,0,0)
      criar_usuario_obj.cadastrar()
      dicionario_de_chefia[criar_usuario_obj.get_login_usuario()] = f"{criar_usuario_obj.get_nome()}", criar_usuario_obj.get_idade(), f"{criar_usuario_obj.get_login_usuario()}", f"{criar_usuario_obj.get_login_senha()}", criar_usuario_obj.get_idChefia() , f"{criar_usuario_obj.get_email()}"
      print(f"Você foi cadastrado {criar_usuario_obj.get_nome()}")
    else:
      print("Coloque uma resposta válida")


  elif opcao == "2":
    print("\nRealizar login como:\n[1] - Aluno\n[2] - Professor\n[3] - Chefe Imediato")
    tipo_usuario = input("Coloque sua resposta:\n> ")
    if tipo_usuario == "1":
      login_usuario = input("Coloque seu usuário para login:")
      login_senha = input("Coloque sua senha para login:")
      logar(login_usuario, login_senha,dicionario_de_usuario_alunos_cadastrados)
      opcao_escrever = input("[1] Escrever Avaliação de professor\n[2] Retornar ao menu")

      if opcao_escrever == "1":
        usuario = dicionario_de_usuario_alunos_cadastrados[login_usuario]
        Aluno_logado = Aluno (usuario[0],usuario[1],usuario[2],usuario[3],usuario[4],usuario[5])
        conteudo = Aluno_logado.escreverAvaliacao()                                                            
        avaliacao = Avaliacao(0, conteudo , conteudo, Aluno_logado, 0)                                           #Associação     
        mural.adicionarAvaliacao(avaliacao)                                                                      #Agregação
        mural.consultarAvaliacao()
        nome_profs = [valor[0] for valor in dicionario_de_profs_cadastrados.values()]
        print (nome_profs)
        DadoProfessor = input("Por favor, coloque o nome do professor a quem deseja avaliar")  #OBS: INVERTER POSIÇÕES, PARA PERGUNTAR A QUE PROF DESEJA ENVIAR PRIMEIRO E DEPOIS AVALIAR
        if DadoProfessor not in nome_profs:
          print ("Coloque uma resposta válida")
          continue
        else:
          avaliacao = Avaliacao(0, conteudo , conteudo, Aluno_logado, DadoProfessor)
          print("Sua avaliação está completa")

    elif tipo_usuario == "2":
      login_usuario = input("Coloque seu usuário para login:")
      login_senha = input("Coloque sua senha para login:")
      logar(login_usuario, login_senha, dicionario_de_profs_cadastrados)

    elif tipo_usuario == "3":
      login_usuario = input("Coloque seu usuário para login:")
      login_senha = input("Coloque sua senha para login:")
      logar(login_usuario, login_senha, dicionario_de_chefia)
      
  elif opcao == "3":
    print("Bem, Adeus")
    break








