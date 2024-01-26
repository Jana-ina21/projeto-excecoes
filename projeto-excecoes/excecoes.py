def calcular_idade():
    while True:
        try:
            nome = input("Digite seu nome completo: ")
            ano_nascimento = int(input("Digite seu ano de nascimento (entre 1922 e 2021): "))
            if 1922 <= ano_nascimento <= 2021:
                idade = 2022 - ano_nascimento
                print(f"Nome: {nome}\nIdade em 2022: {idade} anos")
                break
            else:
                print("Erro: Ano de nascimento deve estar entre 1922 e 2021. Tente novamente.")
        except ValueError:
            print("Erro: Você deve digitar um número para o ano de nascimento. Tente novamente.")

calcular_idade()