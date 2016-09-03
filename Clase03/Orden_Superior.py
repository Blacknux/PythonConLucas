def saludar(lang):
    def saludar_es():
        print("Hola")
    def saludar_en():
        print("Hi")
    def saludar_fr():
        print("salut")
    lang_func={"es":saludar_es,"en":saludar_en,"fr":saludar_fr}
    
    return lang_func[lang]

def calcular(operacion,n1,n2):
    def suma(n1,n2):
        return n1+n2
    def resta(n1,n2):
        return n1-n2
    oper={"+":suma,"-":resta}

    return oper[operacion]

calcular("+",4,5)()
