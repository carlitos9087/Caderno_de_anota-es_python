# !pip install --upgrade seaborn
import numpy as np
import re
import os
import pandas as pd
import PySimpleGUI as sg


def capta_tabelas(caminho:str):
  df=[]
  for num, pasta in enumerate(os.listdir(caminho)):
    if not pasta.endswith(".tabular"): continue
    df.append(pd.read_table(os.path.join(caminho, pasta)))   #lendo tabelas tabelas
    if df[num].index.name != 'Geneid':
      df[num].set_index('Geneid', inplace=True)  #tornando a colula Geneid o id das tabelas
  return df

def ordenandor_titulos3(caminho: str):
    lista_nomes = os.listdir(caminho)

    lista_nomes_corretos  = []
    lista_nomes_corretos2 = []
    lista_nomes_corretos3 = []
    resultado = []
    for titulo in lista_nomes:
        # pattern = '_[a-zA-Z]+[0-9]*.tabular'
        pattern = '_[a-zA-Z]+[0-9 ]*.tabular'
        string = titulo
        repl = ''
        lista_nomes_corretos.append(re.sub(pattern, repl, string))

    for i in lista_nomes_corretos:

      i = i.split("_")

      if len(i[-1]) == 1:
        i.insert(-1, "_0")
      else:
        i.insert(-1, "_")
      lista_nomes_corretos2.append(i)

    for nomes_partidos in lista_nomes_corretos2:
      if len(nomes_partidos) == 3:
        aux1 = "".join(nomes_partidos)
        resultado.append(aux1)
      else:
        for num in range(1,len(nomes_partidos)):
          if num % 2 == 0: continue
          nomes_partidos.insert(num, "_")
        aux2 = "".join(nomes_partidos)
        resultado.append(aux2)

    return resultado

def junta_tabelas(lista_tabelas:list, lista_titulos:list):
    df_todos = pd.merge(lista_tabelas[0], lista_tabelas[1], on="Geneid")

    for itens in lista_tabelas[2:]:
        df_todos = pd.merge(df_todos, itens, on="Geneid")

    df_todos.columns = lista_titulos
    return df_todos

def somar_reads(tabelas_brutas):
  Soma_reads = pd.DataFrame(tabelas_brutas.sum()/1000000).T
  return Soma_reads

def length(id_genes):
  caminho_Gene = pd.read_excel(id_genes)
  lista_genes = caminho_Gene["Geneid"].to_list()
  return lista_genes

def RPM(Gene_hits, soma_reads, ordem):
  df, rpm = [], []
  for i in range(0,len(ordem)):
    df.append(Gene_hits[ordem[i]]/ soma_reads[ordem[i]].values)

  rpm = pd.merge(df[0], df[1], on="Nome")

  for a in df[2:]:
    rpm = pd.merge(rpm, a, on="Nome")

  return rpm

def RPKM(Rpm, Gene_CDS):
  rpkm = Rpm.copy()
  for i in range(0,rpkm.shape[0]):
    rpkm.iloc[[i],:]=(rpkm.iloc[[i],:]/Gene_CDS["Gene_CDS length"].to_list()[i])
  return rpkm*1000

def RPKM2(RPKM):
  a = RPKM.apply(lambda x: np.log2(x))
  b = a.replace([np.inf, -np.inf], 0)
  return b

# caminho="./Microsoft-Excel-logo-1.png"
# image = Image.open(caminho)
# resized_image = image.resize((50, 50))
caminho = './imagem_redimensionada.png'
# resized_image.save(resized_image_path)

form_rows =   sg.Frame('Dados',[
             [sg.Text('SRR files', size=(15, 1))],
             [sg.InputText('',), sg.FolderBrowse(key="-caminho-")],
             [sg.Text('Genes Info', size=(15, 1))], 
             [sg.InputText(''), sg.FileBrowse(key="-caminho_Gene-")],
             ], element_justification = 'left', expand_y=True, title_location=sg.TITLE_LOCATION_TOP)

download =   sg.Frame('Download',[[sg.Image(caminho, p=[20,20])],[sg.Button("RPM", key="-RPM-"),sg.Button("RPKM", key="-RPKM-"),sg.Button("Log2 RPKM", key="-Log2 RPKM-")]],
            element_justification = 'center', expand_x=True, title_location=sg.TITLE_LOCATION_TOP, pad=[0,20])

tela = [[sg.Column([[form_rows],[download]])]]