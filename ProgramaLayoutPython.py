import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        sg.change_look_and_feel('darkblack1')
        #Layout
        layout = [
            [sg.Text('Nome do usuario: ', size=(15, 0)), sg.Input(size=(15, 0), key='nome'),],
            [sg.Text('Idade do usuario: ', size=(15, 0)), sg.Input(size=(15, 0), key='idade')],
            [sg.Text('Data de nascimento: ', size=(15, 0)), sg.Input(size=(15, 0), key='nascimento')],
            [sg.Text('Quais provedores de e-maisl sao aceitos? ')],
            [sg.Checkbox('Gmail', key='gmail'), sg.Checkbox('Outlook', key='outlook'), sg.Checkbox('yahoo', key='yahoo')],
            [sg.Text('Aceita cartao? ')],
            [sg.Radio('sim', 'cartoes', key='aceitaCartao'), sg.Radio('nao', 'cartoes', key='naceitaCartao')],
            [sg.Slider(range=(0, 100),default_value= 0, orientation='h',size= (15,20), key='sliderVel')],
            [sg.Button('Enviar dados')],
            [sg.Output(size=(30, 10))]
        ]
        #Janela
        self.janela = sg.Window('Dados do usuario').layout(layout)


    def Iniciar(self):
        while True:
            # Extrair os dados
            self.button, self.values = self.janela.Read()
            nome = self.values['nome']
            idade = self.values['idade']
            nascimento = self.values['nascimento']
            aceita_gmail = self.values['gmail']
            aceita_outlook = self.values['outlook']
            aceita_yahoo = self.values['yahoo']
            aceitaCartao = self.values['aceitaCartao']
            naceitaCartao = self.values['naceitaCartao']
            velocidadeScript = self.values['sliderVel']
            print(f'Nome: {nome}')
            print(f'Idade: {idade}')
            print(f'Data de nascimento: {nascimento}')
            print(f'Aceita gmail: {aceita_gmail}')
            print(f'Aceita outlook: {aceita_outlook}')
            print(f'Aceita yahoo: {aceita_yahoo}')
            print(f'Aceita cartao? {aceitaCartao}')
            print(f'Nao aceita cartao? {naceitaCartao}')
            print(f'Velocidade do Script: {velocidadeScript}')


tela = TelaPython()
tela.Iniciar()

