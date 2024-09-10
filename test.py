import PySimpleGUI as sg
import os
import sqlite3

# diretorio_corrente = os.path.dirname(os.path.abspath(__file__))
db_path = './meudb.db'  #os.path.join(diretorio_corrente, 'database.db')

def initialize_db():
    # db_path = 'path_to_your_database.db'
    # if not os.path.exists(db_path):
    #     print(f"Database file does not exist: {db_path}")
    # else:
    #     print(f"Attempting to connect to database: {db_path}")

    try:
        conexao = sqlite3.connect(db_path)
        print("Database connection successful")
        cur = conexao.cursor()
    
        cur.execute('''CREATE TABLE IF NOT EXISTS CLIENTE (
                            CPF TEXT,
                            NOME TEXT, 
                            SOBRENOME TEXT)''')
        cur.execute('''CREATE TABLE IF NOT EXISTS APARELHO_ELETRONICO (
                            APARELHO TEXT, 
                            DEFEITO TEXT, 
                            MODELO TEXT, 
                            MARCA TEXT)''')
                        # o cursor é o obj responsavel por fazer as ações
        conexao.commit() #sempre precisa commitar pra garantar que tu esta enviadno os dados
    except sqlite3.OperationalError as e:
        print(f"Error connecting to database: {e}")
    finally:
        cur.close()
        conexao.close()

def sqlInsert(query, params):
    try:
        conexao = sqlite3.connect(db_path)
        cur = conexao.cursor()
        cur.execute(query, params)
        conexao.commit()
        return 1
    except sqlite3.Error as e:
        sg.popup(f'Erro no banco de dados: {e}')
        return None
    finally:
        cur.close()
        conexao.close()

initialize_db()

# dados = []
# aparelho_eletronico = ['Marca', 'Defeito', 'Modelo', 'Aparelho']
# cliente = ['CPF', 'Nome', 'Sobrenome']

queryCliente = """INSERT INTO CLIENTE ('CPF', 'NOME', 'SOBRENOME') VALUES (?, ?, ?)"""
queryAparelho = """INSERT INTO APARELHO_ELETRONICO ('MARCA', 'DEFEITO', 'MODELO', 'APARELHO') VALUES (?, ?, ?, ?)"""

print('adicione os valores para incluir um cliente')
cpf = input('cpf: ')
nome = input('nome: ')
sobrenome = input('sobrenome: ')

print('adicione valores pra incluir um aparelho eletronico')
marca = input('marca: ')
defeito = input('defeito: ')
modelo = input('modelo: ')
aparelho = input('aparelho: ')

def insercaoEmLote():
    res1 = sqlInsert(queryCliente, (cpf,nome,sobrenome))
    res2 = sqlInsert(queryAparelho, (marca,defeito,modelo,aparelho))
    if(res1 == None and res2 == None):
        print('deu erro, magrao')
    print('sucesso')
insercaoEmLote()

#tipos no python ---- foreing key

          












# layout = [
#     [sg.Text(aparelho_eletronico[0]), sg.Input(size=20, key=aparelho_eletronico[0])],
#     [sg.Text(aparelho_eletronico[1]), sg.Input(size=20, key=aparelho_eletronico[1])],
#     [sg.Text(aparelho_eletronico[2]), sg.Input(size=20, key=aparelho_eletronico[2])],
#     [sg.Text(aparelho_eletronico[3]), sg.Combo(['Notebook', 'Computador'], key=aparelho_eletronico[3])],
#     [sg.Text(cliente[0]), sg.Input(size=20, key=cliente[0])],
#     [sg.Text(cliente[1]), sg.Input(size=20, key=cliente[1])],
#     [sg.Text(cliente[2]), sg.Input(size=20, key=cliente[2])],
#     [sg.Button('Adicionar Cliente'), sg.Button('Adicionar Aparelho'), sg.Button('Editar'), sg.Button('Salvar', disabled=True), sg.Button('Excluir'), sg.Exit('Sair')],
#     [sg.Table(values=dados, headings=cliente + aparelho_eletronico, key='tabela_aparelhos', display_row_numbers=True, auto_size_columns=True)]
# ]

# window = sg.Window('Sistema de Aparelhos Eletrônicos', layout)

# while True:
#     event,values=window.read()
#     print(window)

#     editarLinha = None

   

#     while True:
#         event, values = window.read()

#         if event == sg.WIN_CLOSED or event == 'Sair':
#             break

#         if event == 'Adicionar':
        
#             dados.append([values[cliente[0]], values[cliente[1]], values[cliente[2]]])
#             window['tabela_aparelhos'].update(values=dados)
#             for i in range(3):
#                 window[cliente[i]].update(value='')
            
#             dados.append([values[aparelho_eletronico[0]], values[aparelho_eletronico[1]], values[aparelho_eletronico[2]], values[aparelho_eletronico[3]]])
#             window['tabela_aparelhos'].update(values=dados)
#             for i in range(3):
#                 window[aparelho_eletronico[i]].update(value='')

#             conexao = sqlite3.connect(db_path)
#             conexao.execute("INSERT INTO CLIENTE (CPF, NOME, SOBRENOME) VALUES (?, ?, ?)", (values[cliente[0]], values[cliente[1]], values[cliente[2]]))
#             conexao.execute("INSERT INTO APARELHO_ELETRONICO (APARELHO, DEFEITO, MODELO, MARCA) VALUES (?, ?, ?, ?)", (values[aparelho_eletronico[0]], values[aparelho_eletronico[1]], values[aparelho_eletronico[2]], values[aparelho_eletronico[3]]))
#             conexao.commit()
#             conexao.close()

#         elif event == 'Editar':
#             if not values['tabela_aparelhos']:
#                 sg.popup('Nenhuma linha selecionada')
#             else:
#                 editarLinha = values['tabela_aparelhos'][0]
#                 sg.popup('Editar linha selecionada')
#                 for i, campo in enumerate(cliente + aparelho_eletronico):
#                     window[campo].update(value=dados[editarLinha][i])
#                 window['Salvar'].update(disabled=False)

#         elif event == 'Salvar':
#             if editarLinha is not None:
#                 dados[editarLinha] = [values[cliente[i]] for i in range(len(cliente))] + [values[aparelho_eletronico[i]] for i in range(len(aparelho_eletronico))]
#                 window['tabela_aparelhos'].update(values=dados)

#                 for campo in cliente + aparelho_eletronico:
#                     window[campo].update(value='')
#                 window['Salvar'].update(disabled=True)

#                 try:
#                     conexao = sqlite3.connect(db_path)
#                     conexao.execute("UPDATE CLIENTE SET NOME = ?, SOBRENOME = ? WHERE CPF = ?", 
#                                     (values[cliente[1]], values[cliente[2]], values[cliente[0]]))
#                     conexao.execute("UPDATE APARELHO_ELETRONICO SET APARELHO = ?, DEFEITO = ?, MODELO = ? WHERE MARCA = ? ", 
#                                     (values[aparelho_eletronico[1]], values[aparelho_eletronico[2]], values[aparelho_eletronico[3]], values[aparelho_eletronico[0]]))
#                     conexao.commit()
#                 except sqlite3.Error as e:
#                     sg.popup(f'Erro no banco de dados: {e}')
#                 finally:
#                     conexao.close()

#         elif event == 'Excluir':
#             if not values['tabela_aparelhos']:
#                 sg.popup('Nenhuma linha selecionada')
#             else:
#                 if sg.popup_ok_cancel('Essa operação não pode ser desfeita. Confirma?') == 'OK':
#                     try:
#                         conexao = sqlite3.connect(db_path)
#                         cpf_cliente = dados[values['tabela_aparelhos'][0]][0]
#                         conexao.execute("DELETE FROM APARELHO_ELETRONICO WHERE CPF_CLIENTE = ?", (cpf_cliente,))
#                         conexao.execute("DELETE FROM CLIENTE WHERE CPF = ?", (cpf_cliente,))
#                         conexao.commit()
#                     except sqlite3.Error as e:
#                         sg.popup(f'Erro no banco de dados: {e}')
#                     finally:
#                         conexao.close()

#                     del dados[values['tabela_aparelhos'][0]]
#                     window['tabela_aparelhos'].update(values=dados)

#     window.close()
