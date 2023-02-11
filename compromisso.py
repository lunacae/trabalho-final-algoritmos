class Compromisso:

    def __init__(self, data, hora, duracao, descricao):
        self.data = data
        self.hora = hora
        self.duracao = duracao
        self.descricao = descricao

    def setData(self, data):
        self.data = data

    def setHora(self, hora):
        self.hora = hora

    def setDuracao(self, duracao):
        self.duracao = duracao

    def setDescricao(self, descricao):
        self.descricao = descricao

    def getData(self):
        return self.data

    def getHora(self):
        return self.hora

    def getDuracao(self):
        return self.duracao

    def getDescricao(self):
        return self.descricao

vetor = []
c = 0
while c != 7:
    print('1 - Incluir compromisso')
    print('2 - Consultar compromisso por data')
    print('3 - Consultar compromisso por hora e data')
    print('4 - Alterar compromisso')
    print('5 - Excluir compromisso')
    print('6 - Listar todos os compromissos')
    print('7 - Sair')
    c = int(input('informe qual operação deseja executar: '))

    if(c == 1):
        data = input('informe a data (dd/mm/aaaa): ')
        hora = input('informe a hora (valor inteiro): ')
        duracao = input('informe a duração em horas (valor inteiro): ')
        descricao = input('informe a descrição: ')
        comp = Compromisso(data, hora, duracao, descricao)
        vetor.append(comp)
    elif(c == 2):
        data = input('Informe a data para pesquisa (dd/mm/aaaa): ')
    elif(c == 3):
        data = input('Informe a data para pesquisa (dd/mm/aaaa): ')
        hora = input('Informe a hora para pesquisa (valor inteiro): ')

    elif(c == 4):
        print('Pensar em como buscar o compromisso e alterá-lo')
    elif(c == 5):
        print("Pensar em uma forma de deletar compromisso")
    elif(c == 6):
        for i in range(len(vetor)):
            print('Id do compromisso: ' + i)
            print('Data: ' + vetor[i].data)
            print('Hora: ' + vetor[i].hora)
            print('Duração: ' + vetor[i].duracao)
            print('Descrição: ' + vetor[i].descricao)

print('Programa finalizado')
