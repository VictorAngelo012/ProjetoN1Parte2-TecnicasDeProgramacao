def menu_opcoes(menu):
    i = False
    exit = False

    print('--------------------------')
    print('Você está no menu principal.\nSelecione uma opção para prosseguir:\n')
    print('1: Cadastrar novo Usuário.\n2: Listar Usuários por ordem de cadastro.\n3: Listar Usuários por ordem alfabética.')
    print('4: Buscar Usuário.\n5: Remover Usuário.\n6: Alterar o nome de um Usuário.\n7: Fechar o Programa.')
    print('--------------------------\n')
    menu = int(input())

    while(i == False):
        if(menu == 1):
            #Inserir função 1
            i = True
        elif(menu == 2):
            #Inserir função 2
            i = True
        elif(menu == 3):
            #Inserir função 3
            i = True
        elif(menu == 4):
            #Inserir função 4
            i = True
        elif(menu == 5):
            #Inserir função 5
            i = True
        elif(menu == 6):
            #Inserir função 6
            i = True
        elif(menu == 7):
            i = True
            exit = True
        else:
            menu = int(input('Menu inválido. Por favor, digite o menu desejado:\n'))
    return(exit)

#Daqui pra cima são as funções 
##################################################################################
#Daqui pra baixo é o programa principal

dicionario_usuarios = dict()
exit = False
menu = 0

while(exit == False):
    exit = menu_opcoes(menu)