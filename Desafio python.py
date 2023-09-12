x = 0
print("=================")
print("Digite 1 para realizar f°g\n")
print("Digite 2 para realizar g°f\n")
print("Digite 3 para realizar g°g\n")
print("Digite 4 para realizar f°f\n")
print("=================")
escolha = int(input("Digite a composição de função que deseja usar: "))
print("=================")
print("Digite 1 para usar um valor para x\n")
print("Digite 2 para nao usar x\n")
print("=================")
escolhax = int(input("Digite sua escolha: "))
if escolhax == 1:
  x = int(input("Digite um valor para x: "))

  ##
  ## É aqui que você pode mudar as funções de f(x) e g(x)
  fx = x**2
  gx = x - 1

  ##

  if escolha == 1:
    fx = (gx)**2
    print(fx)

  elif escolha == 2:
    gx = (fx) - 1
    print(gx)

  elif escolha == 3:
    gx = (gx) - 1
    print(gx)

  elif escolha == 4:
    fx = (fx)**2
    print(fx)
  else:
    print("Digite uma opção válida")

elif escolhax == 2:
  if escolha == 1:
    print(" f°g = f(gx) = (x-1)**2")

  elif escolha == 2:
    print("g°f = g(fx) = (x**2)-1")

  elif escolha == 3:
    print("g°g = g(gx) = (x-1)-1")

  elif escolha == 4:
    print("f°f = f(fx) = (x**2)**2")
  else:
    print("Digite uma opção válida")
