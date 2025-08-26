from time import sleep

loop = True
while loop:
    count = 0
    count_bi_years = 0
    print("Descubra quantos anos bissextos existem de 2000 até x (Limite 4000)")
    basis_year = int(input("Insira o ano referência para o cálculo de anos bissextos:"))

    if basis_year <= 4000 and basis_year >= 2000:
        for year in range(2000, basis_year):
            if count == 4:
                count_bi_years += 1
                count = 0
            count += 1

        sleep(1.5)
        print(f"Até o ano de {basis_year} existe(m) {count_bi_years} ano(s) bissexto(s)")
        print()
        sleep(1.5)
    else:
        print("Por favor insira um valor entre 2000 e 4000") 
        print()
        sleep(1.5)
    
    while True:
        response = str(input("Deseja verificar novamente? [S/N]"))
        response = response.upper()
        if response == "SIM" or response == "S":
            loop = True
            break
        if response == "NAO" or response == "N":
            loop = False
            break
        else:
            sleep(0.5)
            print("Por favor insira uma resposta válida!")
            