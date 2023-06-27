import PySimpleGUI as sg
from PIL import Image

caminho="/home/carlitos/Downloads/Microsoft-Excel-logo-1.png"
image = Image.open(caminho)
resized_image = image.resize((50, 50))
resized_image_path = 'imagem_redimensionada.png'
resized_image.save(resized_image_path)


form_rows =   sg.Frame('Dados',[
             [sg.Text('SRR files', size=(15, 1))],
             [sg.InputText(''), sg.FolderBrowse()],
             [sg.Text('Genes Info', size=(15, 1))], 
             [sg.InputText(''), sg.FolderBrowse()],
             ], element_justification = 'left', expand_y=True, title_location=sg.TITLE_LOCATION_TOP)

download =   sg.Frame('Download',[[sg.Image(resized_image_path, p=[20,20])],[sg.Button("RPM"),sg.Button("RPKM"),sg.Button("Log2 RPKM")]],
            element_justification = 'center', expand_x=True, title_location=sg.TITLE_LOCATION_TOP, pad=[0,20])

tela = [[sg.Column([[form_rows],[download]])]]


event, values = sg.Window('Normalizador', tela, auto_size_text=True).read()
print(event, values)
#######################################################################################3

# import PySimpleGUI as sg

# def blank_frame():
#     return sg.Frame("", [[]], pad=(5, 3), expand_x=True, expand_y=True, background_color='#404040', border_width=0)

# sg.theme('DarkGrey4')

# layout_frame1 = [
#     [blank_frame(), blank_frame()],
#     [sg.Frame("Frame 3", [[blank_frame()]], pad=(5, 3), expand_x=True, expand_y=True, title_location=sg.TITLE_LOCATION_TOP)],
# ]

# layout_frame2 = [[blank_frame()]]

# layout = [
#     [sg.Frame("Frame 1", layout_frame1, size=(280, 250)),
#      sg.Frame("Frame 2", layout_frame2, size=(200, 250), title_location=sg.TITLE_LOCATION_TOP)],]

# window = sg.Window("Title", layout, margins=(2, 2), finalize=True)

# while True:

#     event, values = window.read()
#     if event == sg.WINDOW_CLOSED:
#         break

# window.close()


