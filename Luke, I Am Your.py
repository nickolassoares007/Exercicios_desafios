def relation_to_luke(nome):
    relacoes = {                 
        "Darth Vader": "father",
        "Leia": "sister",
        "Han": "brother in law",
        "R2D2": "droid",
        "C3PO": "droid",
        "Yoda": "master",
        "ObiWan": "master",
    }
    return f"Luke, I am your {relacoes[nome]}." #f-string (ou formatted string), uma maneira elegante e poderosa de criar textos com valores variáveis dentro deles.


# Aqui começa a parte interativa
nome = input("Digite o nome de alguém da galáxia de Star Wars: ")
print(relation_to_luke(nome))

# comentarios sobre meus erros

# Prestar atenção na identação, pois o python é sensível a isso.
# a função print() deve ser com o p minusculo.
# def é a palavra reservada para definir uma função.
# não esquecer de colocar o return no final da função.
# o nome da função deve ser o mesmo na hora de chamar a função.
# Não esquecer de colocar dois pontos no final da função.