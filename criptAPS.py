print('''   1-2-3-4-5-6
1-|A|B|C|D|E|F|   
2-|G|H|I|J|K|L|  
3-|M|N|O|P|Q|R|  Gráfico ilustrativo
4-|S|T|U|V|W|X|  da cifra de Políbio
5-|Y|Z|0|1|2|3|
6-|4|5|6|7|8|9|
        ''')

polibio = {'A':'11','B':'12','C':'13','D':'14','E':'15','F':'16',
           'G':'21','H':'22','I':'23','J':'24','K':'25','L':'26',
           'M':'31','N':'32','O':'33','P':'34','Q':'35','R':'36',
           'S':'41','T':'42','U':'43','V':'44','W':'45','X':'46',
           'Y':'51','Z':'52','0':'53','1':'54','2':'55','3':'56',
           '4':'61','5':'62','6':'63','7':'64','8':'65','9':'66'}



#encriptador de codigo
while True:
    descripto = ""
    cripto = ""
    cript = input('O que você deseja fazer? Criptografar(C), descriptografar(D) ou Sair(S)? ')
    if cript == "C":
        frase = input('Informe a frase a ser criptografada: ')
        for i in frase.upper():
            if i == " ": cripto += "_ "
            cripto += polibio[i]
        print(cripto, '\n')


#desencriptador de codigo
    elif cript == "D":
        cod = input("Informe o código a ser desencriptado: ")
        while True:
            for i in polibio:
                if cod[:2] == polibio[i]:
                    descripto += i
                    cod = cod[2:]
                    break
                else:
                    continue
            if cod == '': break
        print(descripto, '\n')


#Finaliza o programa
    elif cript == "S":
        print("\033[1:33mPrograma finalizado!\033[m")
        break


#mostra uma mensagem de erro caso coloque uma alternativa inexistente
    elif cript != "C" or 'D' or "S" or "l":
        print("\033[1:31mColoque uma das alternativas citadas!\033[m \n")












