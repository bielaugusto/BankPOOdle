from Clientes import*
from Contas import*
import os

if __name__ == "__main__":
    listaCarteiras = []
    listaPessoas = []
    print("Bem Vindo ao Bank POOdle.\n")
    while True:
        print ("(1) Cadastrar um novo cliente")
        print ("(2) Pesquisar clientes já cadastrados")
        print ("(3) Cadastrar uma nova carteira")
        print ("(4) Listar as contas de uma carteira existente")
        print ("(5) Finalizar Programa \n")
        opcao = int(input("Selecione a opção desejada: "))

        if opcao == 1:

            resposta = input("Deseja realmente adicionar um novo cliente? (s/n) ")
            while (resposta == 's' or resposta == 'S'):
                num = input("informe o número do seu CPF ou CNPJ: ")
                nom = input("Informe seu nome: ")
                nas = input("informe sua data de nascimento: ")
                end = input("Informe seu endereço: ")
                tip = input("Pessoa Física ou Pessoa Jurídica? ")
                if tip == "Fisica":
                   num.addCliente(PessoaFisica(num, nom, nas, end))
                elif tip == "Juridica":
                   num.addCliente(PessoaJuridica(num, nom, nas, end))
                else:
                    print("Digite novamente, por gentileza.")
                resposta = input("Deseja criar um novo cliente? (s/n) ")
                

            listaPessoas += [num]
            print (f"O cadastro do cliente de pessoa {tip} foi realizado com sucesso!")
            print ("Aperte a tecla ENTER para voltar ao menu.")
        
        elif opcao == 2:

            tip = input("Informe o tipo de pessoa: ")
            achou = False
            for carteiraTeste in listaPessoas:
                if carteiraTeste.tipo == tip:
                    achou = True
                    if carteiraTeste.listapessoas == []:
                        print(f"Esse cliente de pessoa {tip} não possui registro! \n")
                    else:
                        for cliente in carteiraTeste.listaPessoas:
                            print (cliente.retornaDadosCliente())

        elif opcao == 3:
            
            inv = input("Qual o tipo de investimento?")
            car = Carteira(inv)
            resposta = input("Deseja cadastrar uma conta? (s/n)")
            while (resposta == "s"):
                num = input("informe o número da conta: ")
                tit = input("informe o nome do titular: ") 
                sld = float(input("Qual o valor do saldo inicial?"))
                tip = input("Conta normal (N), Conta corrente (C) ou Conta poupança (P)? ")
                if tip == "N":
                    car.addConta(Conta(num, tit, sld))
                elif tip == "C":
                    car.addConta(ContaCorrente(num, tit, sld))
                else:
                    ren = float(input("Informe o rendimento mensal: "))
                    car.addConta (ContaPoupanca(num, tit, sld, ren))
                resposta = input("Deseja cadastrar uma conta? (s/n)" )
            listaCarteiras += [car]
            print (f"Cadastro da carteira {inv} foi realizada! =)\n")
        
        elif opcao == 4:

            inv = input("Informe o investimento que você deseja realizar: ")
            achou = False
            for carteiraTeste in listaCarteiras:
                if carteiraTeste.investimento == inv:
                    achou = True
                    if carteiraTeste.listaContas == []:
                        print(f"Esse carteira {inv} não possui contas cadastradas! \n")
                    else:
                        for continha in carteiraTeste.listaContas:
                            print (continha.retornaDados())
            if not achou:
                print("Não existe essa carteira! \n")

        elif opcao == 5:
            break
        else:
            print ("Opção inválida!""\n")
        input()
        os.system("cls" if os.name == "nt" else "clear")
    print ("Espero que sua experiência venha ter sido especial. Volte sempre ao Bank POOdle!")

    