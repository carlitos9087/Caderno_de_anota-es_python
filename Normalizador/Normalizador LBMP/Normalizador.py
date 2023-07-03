import PySimpleGUI as sg
import pandas as pd
import backend
import os

window = backend.tela
tela = sg.Window('Normalizador', window, auto_size_text=True)
    
caminho_teste = "/home/carlitos/Documentos/Caderno_de_anotacoes_python/Normalizador/Dados/GSE162760"

while True:                             # The Event Loop
    event, values = tela.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break      
    # event, values = sg.Window('Normalizador', tela, auto_size_text=True).read()
    # print("\n\nEvento: ",event,"\nvalor: \n", values)

    # print(values)
    try:
        tabelas_separadas = backend.capta_tabelas(values["-caminho-"])
        print(tabelas_separadas[0] )#####################

        titulos = backend.ordenandor_titulos3(values["-caminho-"])
        # print(titulos)#################

        titulos_ordem = titulos.copy()
        titulos_ordem.sort()
    
        tabelas_juntas = backend.junta_tabelas(tabelas_separadas, titulos )
        # print(tabelas_juntas,"dsafdsafdsgfdagf")
        tabelas_juntas = tabelas_juntas[titulos_ordem]
        # print(tabelas_juntas)  #####################

    except:
        sg.popup("Ocorreu um erro ao ler as srr files\nTente novamente.", title="Erro srr files")
        continue




    try:
        genes = backend.length(values["-caminho_Gene-"])
        # print(genes) #####################

        #tabela com os genes
        Gene_CDS_length = pd.read_excel(values["-caminho_Gene-"])

        hits = tabelas_juntas.loc[genes]
        hits.index = Gene_CDS_length["Nome"]
        # print(hits) #####################

        total_reads = backend.somar_reads(tabelas_juntas)
        # print(total_reads) #####################
    except:
        sg.popup("Ocorreu um erro ao ler as informações do gene\nTente novamente.", title="Erro gene info")
        continue
    try:
        rpm= backend.RPM(hits,total_reads,titulos_ordem)
    except:
        sg.popup("Ocorreu um erro ao normalizar\nTente novamente.", title="Erro ")
        continue
    try:
        rpkm = backend.RPKM(rpm,Gene_CDS_length)
    except:
        sg.popup("Ocorreu um erro ao normalizar\nTente novamente.", title="Erro ")
        continue
    try:
        rpkm2 = backend.RPKM2(rpkm)
    except:
        sg.popup("Ocorreu um erro ao normalizar\nTente novamente.", title="Erro ")
        continue

    if event == "-RPM-":
        folder_path = sg.popup_get_file("Salvar", save_as=True, file_types=('Excel Files', '*.xlsx'))
        rpm.to_excel(f"{folder_path}{event}.xlsx")
            
    if event == "-RPKM-":
        folder_path = sg.popup_get_file("Salvar", save_as=True, file_types=('Excel Files', '*.xlsx'))
        rpkm.to_excel(f"{folder_path}{event}.xlsx")

    if event == "-Log2 RPKM-":
        folder_path = sg.popup_get_file("Salvar", save_as=True, file_types=('Excel Files', '*.xlsx'))
        rpkm2.to_excel(f"{folder_path}{event}.xlsx")

tela.close()




