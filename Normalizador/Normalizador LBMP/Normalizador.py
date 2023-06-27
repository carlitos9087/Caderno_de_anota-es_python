from tkinter import Tk
from tkinter.filedialog import askdirectory
import PySimpleGUI as sg
import pandas as pd
import backend



window = backend.tela
tela = sg.Window('Normalizador', window, auto_size_text=True)
    

while True:                             # The Event Loop
    event, values = tela.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break      
    # event, values = sg.Window('Normalizador', tela, auto_size_text=True).read()
    # print("\n\nEvento: ",event,"\nvalor: \n", values)


    tabelas_separadas = backend.capta_tabelas(values["-caminho-"])
    # print(tabelas_separadas) #####################

    titulos = backend.ordenandor_titulos3(values["-caminho-"])
    titulos_ordem = titulos.copy()
    titulos_ordem.sort()

    tabelas_juntas = backend.junta_tabelas(tabelas_separadas, titulos )
    tabelas_juntas = tabelas_juntas[titulos_ordem]
    # print(tabelas_juntas)  #####################




    genes = backend.length(values["-caminho_Gene-"])
    # print(genes) #####################

    #tabela com os genes
    Gene_CDS_length = pd.read_excel(values["-caminho_Gene-"])

    hits = tabelas_juntas.loc[genes]
    hits.index = Gene_CDS_length["Nome"]
    # print(hits) #####################



    total_reads = backend.somar_reads(tabelas_juntas)
    # print(total_reads) #####################

    rpm= backend.RPM(hits,total_reads,titulos_ordem)

    rpkm = backend.RPKM(rpm,Gene_CDS_length)

    rpkm2 = backend.RPKM2(rpkm)
   
    if event == "-RPM-":
        root = Tk()
        root.withdraw()  # Oculta a janela principal do tkinter
        folder_path = askdirectory()  # Exibe o diálogo de seleção de pasta
        if folder_path:
            # Faça algo com o local de download selecionado
            print('\n\nLocal de download selecionado:', folder_path)
            rpm.to_excel(f"{folder_path}/{event}.xlsx")
        root.destroy()  # Fecha a janela do tkinter   
            
    if event == "-RPKM-":
        root = Tk()
        root.withdraw()  # Oculta a janela principal do tkinter
        folder_path = askdirectory()  # Exibe o diálogo de seleção de pasta
        if folder_path:
            # Faça algo com o local de download selecionado
            print('\n\nLocal de download selecionado:', folder_path)
            rpm.to_excel(f"{folder_path}/{event}.xlsx")
        root.destroy()  # Fecha a janela do tkinter 

    if event == "-Log2 RPKM-":
        root = Tk()
        root.withdraw()  # Oculta a janela principal do tkinter
        folder_path = askdirectory()  # Exibe o diálogo de seleção de pasta
        if folder_path:
            # Faça algo com o local de download selecionado
            print('\n\nLocal de download selecionado:', folder_path)
            rpm.to_excel(f"{folder_path}/{event}.xlsx")
        root.destroy()  # Fecha a janela do tkinter 

        



tela.close()




