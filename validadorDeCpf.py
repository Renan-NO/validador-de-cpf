listaCpf = []
listaPrimD = []
listaSegD = []
cpf = input('Digite seu cpf: \n')
mult1 = 10
mult2 = 11
primD = 0
segD = 0


if len(cpf) == 11:
    for el in cpf:
        listaCpf.append(int(el))
        if mult1 >= 2:
            listaPrimD.append(int(el)*mult1)
        if mult2 >= 2:
            listaSegD.append(int(el)*mult2)
        mult1 -= 1
        mult2 -= 1

    conta1 = sum(listaPrimD)%11
    conta2 = sum(listaSegD)%11

    if conta1 == 0 or conta1 == 1:
        primD = 0
    else:
        primD = 11 - conta1
    
    if conta2 == 0 or conta2 == 1:
        segD = 0
    else:
        segD = 11 - conta2
    
    if listaCpf[9] == primD and listaCpf[10] == segD:
        print('CPF Válido')
    else:
        print('CPF Inválido')