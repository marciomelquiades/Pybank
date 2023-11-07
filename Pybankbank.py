saldo_atual = 10000

menu=''' 
  ----------------------------
  Menu de Operação
  ----------------------------
  (a) Mostrar Saldo
  (b) Efetuar Depósito
  (c) Efetuar Saque
  (d) Finalizar
  -----------------------------
'''
print(menu)
opcao = input('Qual operacao deseja realizar? ')

def deposito():
  valor_deposito = float(input('Qual o valor a ser depositado? '))
  saldo_total = valor_deposito + saldo_atual
  print(f'Deposito realizado com sucesso, seu saldo atual é R${saldo_total}.')

def saldo():
  print('Seu saldo atual é de R$ {}.'.format(saldo_atual))

def saque():
  valor_saque = float(input('Qual o valor do saque? '))
  if valor_saque>saldo_atual:
    print('Saldo insuficiente, tente um novo valor.')
  elif valor_saque<=saldo_atual:
    saldo_total = saldo_atual-valor_saque
    print(f'Saque realizado com sucesso, seu saldo atual é de R${saldo_total:.2f}')

while True:
    if opcao == 'a':
      saldo()
      break
    elif opcao == 'b':
      deposito()
      break
    elif opcao == 'c':
      saque()
      break
    elif opcao == 'd':
      print('Obrigado por utilizar o Py Bank! Sempre Com você!')
      break