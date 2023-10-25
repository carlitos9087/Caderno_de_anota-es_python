import PySimpleGUI as sg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Função para criar um gráfico com base nos valores de X e Y
def criar_grafico(x_values, y_values, tipo_grafico):
    try:
        x = [float(x.strip()) for x in x_values.split(",")]
        y = [float(y.strip()) for y in y_values.split(",")]

        fig, ax = plt.subplots()
        if tipo_grafico == "Gráfico de Linhas":
            ax.plot(x, y, label="Dados de Linha")
        elif tipo_grafico == "Gráfico de Barras":
            ax.bar(x, y, label="Dados de Barra")

        ax.set_xlabel("Eixo X")
        ax.set_ylabel("Eixo Y")
        ax.legend()

        return fig, ax
    except ValueError:
        print("deu ruim")
        return None, None

# Layout da interface
layout = [
    [sg.Text("Escolha o tipo de gráfico:"), sg.Combo(["Gráfico de Linhas", "Gráfico de Barras"], key="-TIPO-", default_value="Gráfico de Linhas")],
    [sg.Text("Valores para o eixo X:"), sg.InputText(key="-X-")],
    [sg.Text("Valores para o eixo Y:"), sg.InputText(key="-Y-")],
    [sg.Button("Criar Gráfico"), sg.Button("Sair")],
    [sg.Canvas(key="-CANVAS-")],
]

# Janela
window = sg.Window("Criador de Gráficos", layout, finalize=True)

# Crie uma figura e um eixo iniciais
fig, ax = plt.subplots()
ax.set_xlabel("Eixo X")
ax.set_ylabel("Eixo Y")
canvas_elem = window["-CANVAS-"]
canvas = FigureCanvasTkAgg(fig, master=canvas_elem.Widget)
canvas.get_tk_widget().pack()
canvas.draw()

# Loop de eventos
while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == "Sair":
        break
    elif event == "Criar Gráfico":
        # Limpe o eixo
        ax.clear()

        # Obtenha os valores inseridos pelo usuário
        x_values = values["-X-"]
        y_values = values["-Y-"]
        tipo_grafico = values["-TIPO-"]

        # Crie um gráfico com tratamento de erro para valores inválidos
        fig, ax = criar_grafico(x_values, y_values, tipo_grafico)

        if fig and ax:
            ax.set_xlabel("Eixo X")
            ax.set_ylabel("Eixo Y")
            ax.legend()

            # Atualize o gráfico no elemento Canvas do PySimpleGUI
            canvas.draw()

            # Force a atualização da janela PySimpleGUI
            window.Refresh()
        else:
            sg.popup_error("Valores inválidos. Certifique-se de que os valores estão corretos.")

# Feche a janela
window.close()
