import PySimpleGUI as sg

# Dados de exemplo para login (substitua por seus próprios dados)
usuarios_cadastrados = {
    'usuario1': 'senha1',
    'usuario2': 'senha2',
    'usuario3': 'senha3',
}

def fazer_login(usuario, senha):
    if usuario in usuarios_cadastrados and usuarios_cadastrados[usuario] == senha:
        return True
    else:
        return False

# Layout da janela de login
layout = [
    [sg.Text('Nome de Usuário:'), sg.InputText(key='usuario')],
    [sg.Text('Senha:'), sg.InputText(key='senha', password_char='*')],
    [sg.Button('Login'), sg.Button('Cancelar')]
]

# Criar a janela
janela = sg.Window('Sistema de Login', layout)

while True:
    event, values = janela.read()

    if event == sg.WINDOW_CLOSED or event == 'Cancelar':
        break

    usuario = values['usuario']
    senha = values['senha']

    if fazer_login(usuario, senha):
        sg.popup('Login bem-sucedido!')
        break
    else:
        sg.popup('Login falhou. Tente novamente.')

janela.close()
