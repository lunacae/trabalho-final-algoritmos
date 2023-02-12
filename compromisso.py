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
    
    def atualizaCompromisso(self, data, hora, duracao, descricao):
        self.setData(data)
        self.setHora(hora)
        self.setDuracao(duracao)
        self.setDescricao(descricao)

def listarCompromisso(compromisso):
    print('Data: ' + compromisso.data)
    print('Hora: ' + compromisso.hora)
    print('Duração: ' + compromisso.duracao)
    print('Descrição: ' + compromisso.descricao)

def listarCompromissos(vetor):
    print('\nLista de compromissos: ')
    for i in range(len(vetor)):
        print('Id do compromisso: ', i)
        print('Data: ' + vetor[i].data)
        print('Hora: ' + vetor[i].hora)
        print('Duração: ' + vetor[i].duracao)
        print('Descrição: ' + vetor[i].descricao)

def listarCompromissosPorData(vetor, data):
    for i in range(len(vetor)):
        if(vetor[i].data == data):
            print('Id do compromisso: ', i)
            listarCompromisso(vetor[i])

def deletarPorId(vetor, id):
    if(len(vetor) >= id+1):
        vetor.pop(id)
        print("Compromisso removido!")
    else:
        print('O id informado não existe')

def listarCompromissosPorDataeHora(vetor, data, hora):
    for i in range(len(vetor)):
        if(vetor[i].data == data and vetor[i].hora == hora):
            print('Id do compromisso: ', i)
            listarCompromisso(vetor[i])

def adicionaCompromisso():
    data = input('informe a data (dd/mm/aaaa): ')
    hora = input('informe a hora (valor inteiro): ')
    duracao = input('informe a duração em horas (valor inteiro): ')
    descricao = input('informe a descrição: ')
    comp = Compromisso(data, hora, duracao, descricao)
    return comp

vetor = []
c = 0
while c != 7:
    print('\n1 - Incluir compromisso')
    print('2 - Consultar compromisso por data')
    print('3 - Consultar compromisso por hora e data')
    print('4 - Alterar compromisso')
    print('5 - Excluir compromisso')
    print('6 - Listar todos os compromissos')
    print('7 - Sair')
    c = int(input('informe qual operação deseja executar: '))

    if(c == 1):
        vetor.append(adicionaCompromisso())
        print('Compromisso adicionado com sucesso!')

    elif(c == 2):
        data = input('Informe a data para pesquisa (dd/mm/aaaa): ')
        listarCompromissosPorData(vetor, data)
        print('Fim da pesquisa')

    elif(c == 3):
        data = input('Informe a data para pesquisa (dd/mm/aaaa): ')
        hora = input('Informe a hora para pesquisa (valor inteiro): ')
        listarCompromissosPorDataeHora(vetor, data, hora)
        print('Fim da pesquisa')

    elif(c == 4):
        
        id = int(input('Informe o ID do compromisso para alterá-lo, para consultar o id selecione \"listar todos\" ou pesquise pelo compromisso por data / hora: '))
        if(len(vetor) >= id+1):
            data = input('informe a nova data (dd/mm/aaaa): ')
            hora = input('informe a nova hora (valor inteiro): ')
            duracao = input('informe a duração em horas (valor inteiro): ')
            descricao = input('informe a descrição: ')
            vetor[id].atualizaCompromisso(data,hora,duracao,descricao)
            print('Compromisso atualizado com sucesso')
        else:
            print('O id informado não existe')

    elif(c == 5):
        id = int(input('Informe o ID do compromisso para deletá-lo, para consultar o id selecione \"listar todos\" ou pesquise pelo compromisso por data / hora: '))
        deletarPorId(vetor,id)
        
    elif(c == 6):
        if(len(vetor) > 0):
            listarCompromissos(vetor)
        else:
            print('Nenhum compromisso foi adicionado ainda \n')

print('Programa finalizado')
