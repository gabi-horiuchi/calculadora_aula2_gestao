while True:
    count = 0
    count_bi_years = 0
    print("Descubra quantos anos bissextos existem de 2000 até x (Limite 4000)")
    basis_year = int(input("Insira o ano referência para o cálculo de anos bissextos:"))

    for year in range(2000, basis_year):
        if count == 4:
            count_bi_years += 1
            count = 0
        count += 1 
    
    print(f"Até o ano de {basis_year} existe(m) {count_bi_years} ano(s) bissexto(s)")