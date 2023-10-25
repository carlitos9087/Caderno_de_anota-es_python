import PySimpleGUI as sg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import statistics as stat
import pandas as pd



sg.theme('DarkTeal9')
# sg.theme('DarkTeal12')
# sg.theme('DarkAmber')
# theme_name_list = sg.theme_list()
# print(theme_name_list)

frameInsert = sg.Frame("Inserir", [ #frame inserir
    [sg.Text('Inserir dados estatísticos')],
    [sg.Text('Insira o valor de X'), sg.Text('Insira o valor de Y')],
    [sg.Input(key='X', do_not_clear=False, size=(10, 1)), sg.Input(key='Y', do_not_clear=False, size=(10, 1))],
    [sg.Text('Insira o número de repetições')],
    [sg.Input(default_text="1", key='N', size=(10, 1))],
    # [sg.Button('Enter'), sg.Exit("Sair")]
    [sg.Button('Enter'), sg.Exit("Apagar")]
],expand_y=False, expand_x=False,size=(280,200))

frameConjuntos = sg.Frame("Conjuntos", [ # frame conjuntos
    [sg.Text('X:'), sg.Text('', key='X_value', background_color = '#446878', border_width=3) ],
    [sg.Text('Y:'), sg.Text('', key='Y_value', background_color = '#446878', border_width=3)]
],
element_justification='left',size=(230,200),
expand_y=False, expand_x=False)

  

frameAvisos = sg.Frame("Avisos", [ #frame avisos
    [sg.Text("Sem avisos", key='error_message')]
],
                background_color='#B22222', 
#size=(500, 50),
element_justification='center',expand_x=True)

frameGrafico = sg.Frame("Graph", [ #frame grafico
    [sg.Canvas(key='graph_canvas', size=(400,300))]
], size=(400, 450), element_justification='center',expand_x=True,expand_y=True)

frameEstatisticas = sg.Frame("Correlação", [ #frame estatisticas
    [sg.Text('Soma de X: '), sg.Text('', key='sum_x')],
    [sg.Text('Soma de Y: '), sg.Text('', key='sum_y')],
    [sg.Text('Média de X: '), sg.Text('', key='mean_x')],
    [sg.Text('Média de Y: '), sg.Text('', key='mean_y')],
    [sg.Text('Correlação Linear: '), sg.Text('', key='Correlacao')],
    [sg.Text('', key='Conclusao',size=(None,1))]
],
    size=(230,250),
    element_justification='left')


#frameCoeficiente é um nome antigo, não traduzido pra função atual dele, que é a regressão
frameCoeficiente = sg.Frame("Regressão Linear", [
[sg.Text('Insira os dados com base na formula:')],
[sg.Text('Y = X * B + A')],
[sg.Text('----------------------------------------')],
[sg.Text('A =', size=(None, None)),sg.Text(0, key="-A-")],
[sg.Text('B =', size=(None, None)),sg.Text(0, key="-B-")],
[sg.Text('Y =',size=(None, None), key='-Y-'),sg.Input(default_text=0, key='Y_', do_not_clear=True, size=(7, 1))],
[sg.Text('X =',size=(None, None), key='-X-'),sg.Input(default_text=0, key='X_', do_not_clear=True, size=(7, 1))],
[sg.Button(button_text="Calcular Regressão", key="Regressao")] ], element_justification='left', size=(280,250))



# Definindo o layout
tela = [
    [sg.Text('Calculadora Correlação Linear e Regressão')],
    [sg.Column([[frameInsert]
                #,[sg.Text('z', size=(1, 1))]
    ,[frameCoeficiente]], expand_y=True, expand_x=True,),
     sg.Column([[frameConjuntos],#[sg.Text('z', size=(1, 1))],
    [frameEstatisticas]], expand_y=True, expand_x=True,),frameGrafico],
     [frameAvisos]]



#FIM FRONT END
#######
#COMEÇO "BACK END"

layout = tela
window = sg.Window("   Calculador", layout)
x, y = [], []
global ultimoX_
ultimoX_ = 0.0
global ultimoY_
ultimoY_ = 0.0

def entrada(x,y,n):
  print("x = ",x, "x type = ", type(x))
  print("y = ",y, "y type = ", type(y))
  print("n = ",n, "n type = ", type(n))

  # Tratando casos de erro de x e y
  
  if x == "": x = "0"
  if y == "": y = "0"
  if n == "":
    window['error_message'].update('Número de repetições não pode ser vazio.')
    XY={"X":x ,"Y":y, "N":0.0}
    return XY
    
  if n.isalpha() or int(n) <= 0:
    window['error_message'].update('Número de repetições inválido. Insira um valor inteiro positivo.')
    XY={"X":x ,"Y":y, "N":n}
    return XY
  if x.isalpha() or y.isalpha():
    window['error_message'].update('X ou Y inválidos. Insira um valor númerico.')
    XY={"X":x ,"Y":y, "N":n}
    return XY
  if x.isalnum() and y.isalnum() and n.isalnum(): 
    a= float(x)
    b= float(y)
    c= float(n)
    window['error_message'].update('Sem avisos!')
    XY={"X":a ,"Y":b, "N":c}
    
    return  XY
  a= float(x)
  b= float(y)
  c= float(n)

  XY={"X":a ,"Y":b, "N":c}
  return XY
  
################################
## Parte Regressão Linear

b = 0 
a = 0 #valores iniciais


def calcular_x(y, a, b):
    return (y - a) / b

def calcular_y(x, a, b):
    return a + b * x

def calcularReg(X_, Y_,a,b):
  global ultimoX_
  global ultimoY_  
  if X_ == "": X_ = 0
  if Y_ == "": Y_ = 0
  
  if a == 0 or b == 0: 
     window['error_message'].update('a e b == 0, por algum motivo')
     resultadoX_ = 0
     resultadoY_ = 0
     return 0;
  if X_.isalpha() or Y_.isalpha():
    window['error_message'].update('X_ ou Y_ inválidos. Insira um valor numerico.')
    #Saindo mais cedo
    return 0
   
  X = float(X_)
    
  Y = float(Y_)
    
  #Calculando X_
  resultadoX_ = round(calcular_x(Y, a, b), 2)
  
  #Calculando Y_
  resultadoY_ = round(calcular_y(X, a, b), 2)
  
  
   
   
  #Atualiza valores x_ e y_
  tempX = ultimoX_
  tempY = ultimoY_
  
    
  if round(X,4) != round(tempX,4) :  
    window['Y_'].update(resultadoY_)
    ultimoX_ = round(X,4)
    ultimoY_ = round(float(resultadoY_),4)
    print("Y_ atualizado");
    
  if round(Y,4) != round(tempY,4) :
    window['X_'].update(resultadoX_) 
    ultimoX_ = round(float(resultadoX_), 4)
    ultimoY_ = round(Y,4)

    
    print("X_ atualizado");
  if round(Y,4) != round(tempY,4) and round(X,4) != round(tempX,4): 
    window['error_message'].update("É impossível calcular X e Y ao mesmo tempo. Retornando a valores padrão")
    window['X_'].update(0)
    window['Y_'].update(0); 
    ultimoX_ = 0
    ultimoY_ = 0

  ################################
  #Função correlação linear

def calcular_correlacao(x, y):
    #Converter as listas em arrays numpy
    x_mean = stat.mean(x)
    y_mean = stat.mean(y)

    x_deviation = [xi - x_mean for xi in x]
    y_deviation = [yi - y_mean for yi in y]

    #Calcular a correlação
    numerator = sum(xi * yi for xi, yi in zip(x_deviation, y_deviation))
    denominator = (sum(xi ** 2 for xi in x_deviation) * sum(yi ** 2 for yi in y_deviation)) ** 0.5

    if denominator == 0:
        return 0

    correlacao = numerator / denominator

    return correlacao


def identificar_forca_correlacao(correlacao):
    if -0.3 <= correlacao <= 0.3:
        return 'Fraca (Positivo)'
    elif 0.3 < correlacao <= 0.6:
        return 'Relativamente Fraca (Positivo)'
    elif 0.6 < correlacao <= 0.9:
        return 'Forte (Positivo)'
    elif 0.9 < correlacao <= 1:
        return 'Muito Forte (Positivo)'
    elif -0.6 <= correlacao < -0.3:
        return 'Relativamente Fraca (Negativa)'
    elif -0.9 <= correlacao < -0.6:
        return 'Forte (Negativa)'
    elif -1 <= correlacao < -0.9:
        return 'Muito Forte (Negativa)'
    else:
        return 'Valor de correlação inválido'


###############################
fig, ax = plt.subplots(figsize=(4, 4))

canvas = None

def update_graph():
    ax.clear()
    ax.scatter(x, y)
    verix=all(elemento == 0 for elemento in x)
    veriy=all(elemento == 0 for elemento in y)
    if verix == False and veriy == False and len(x)>2:
      coefficients = np.polyfit(x, y, 1)
      x_regression = np.linspace(min(x), max(x), 100)
      y_regression = np.polyval(coefficients, x_regression)
      ax.plot(x_regression, y_regression, color='red')
    ax.set_xlabel('Eixo x')
    ax.set_ylabel('Eixo y')
    ax.set_title('Gráfico de Correlação Linear')
    ax.grid(True)
    canvas.draw()

#########################

while True:
    event, values = window.read()
    # Encerra o programa se o usuário fecha a janela
    
    # if event == sg.WIN_CLOSED or event == 'Sair':break
    coisas = entrada(values["X"],values["Y"],values["N"])
    varX = coisas["X"]
    varY = coisas["Y"]
    varN = coisas["N"]
    print(event)
   

    if type(varX) != float or type(varY) != float or type(varN)!= float: continue
    if event == 'Enter':
        for i in range(0,int(varN)):
            x.append(varX)
            y.append(varY)
        print(x,y)
      # Exibe os valores de X e Y no frame "Conjuntos"
        X_value_str = [str(i) for i in x[-5:]]
        Y_value_str = [str(i) for i in y[-5:]]
        if len(x) > 5:
          X_value_str = '...'+", ".join([str(i) for i in x[-5:]])
          Y_value_str = '...'+", ".join([str(i) for i in y[-5:]])
      
        window['X_value'].update(X_value_str)
        window['Y_value'].update(Y_value_str)
      # Cria o gráfico de correlação linear 
        if canvas is None:
            canvas = FigureCanvasTkAgg(fig,master=window['graph_canvas'].TKCanvas)
            canvas.get_tk_widget().pack(side='top', fill='both', expand=1)
      #Atualiza o grafico com novos valores de X e YX_
        update_graph()
      # Calcula a autosomma e media de dados X e Y 
        sum_x = np.sum(x)
        sum_y = np.sum(y)
        mean_x = np.mean(x)
        mean_y = np.mean(y)
      #Correlacao Conclusao
        correlacao = calcular_correlacao(x,y)
        conclusao = identificar_forca_correlacao(calcular_correlacao(x,y))
        window["Correlacao"].update(round(correlacao,4))
        window["Conclusao"].update(conclusao)
      # Exibe a soma e a média de X e Y no frame "Stats"
        window['sum_x'].update(str(sum_x))
        window['sum_y'].update(str(sum_y))
        window['mean_x'].update(f'{mean_x:.2f}')
        window['mean_y'].update(f'{mean_y:.2f}')
      # Exibe a e b depois de 2 elementos na tabela, se elementos forem distintos um dos outros
        
        if (len(x) >= 2 or len(y) >= 2) and (len(set(x)) >= 2 or len(set(y)) >= 2):  
              
              b, a = stat.linear_regression(x,y);
              window['-A-'].update(round(a, 2))
              window['-B-'].update(round(b, 2))
      
  
###############################################################
    if event == 'Apagar':   
        if len(x)==0 or len(y)==0:
          window['error_message'].update('Não há o que apagar')
          print(x,y)
          continue
        if len(x)==1 or len(y)==1:
          window['error_message'].update('Não há o que apagar')
          x.pop()
          y.pop()
          print(x,y)
          update_graph()
          window['X_value'].update("")
          window['Y_value'].update("")
          
          window["Correlacao"].update("")
          window["Conclusao"].update("")
      # Exibe a soma e a média de X e Y no frame "Stats"
          window['sum_x'].update("")
          window['sum_y'].update("")
          window['mean_x'].update("")
          window['mean_y'].update("")
          continue
        x.pop()
        y.pop()
        print(x,y)
      # Exibe os valores de X e Y no frame "Conjuntos"
        X_value_str = [str(i) for i in x[-5:]]
        Y_value_str = [str(i) for i in y[-5:]]
        if len(x) > 5:
          X_value_str = '...'+", ".join([str(i) for i in x[-5:]])
          Y_value_str = '...'+", ".join([str(i) for i in y[-5:]])
      
        window['X_value'].update(X_value_str)
        window['Y_value'].update(Y_value_str)
      # Cria o gráfico de correlação linear 
        if canvas is None:
            canvas = FigureCanvasTkAgg(fig,master=window['graph_canvas'].TKCanvas)
            canvas.get_tk_widget().pack(side='top', fill='both', expand=1)
      #Atualiza o grafico com novos valores de X e YX_
        update_graph()
      # Calcula a autosomma e media de dados X e Y 
        sum_x = np.sum(x)
        sum_y = np.sum(y)
        mean_x = np.mean(x)
        mean_y = np.mean(y)
        # if len(x)==0 or len(y)==0:
        #   window['error_message'].update('Não há o que apagar')
        #   continue
        # if len(x)==1 or len(y)==1:
        #   window['error_message'].update('Não há o que apagar')
        #   x.pop()
        #   y.pop()
        #   continue
      #Correlacao Conclusao
        correlacao = calcular_correlacao(x,y)
        conclusao = identificar_forca_correlacao(calcular_correlacao(x,y))
        window["Correlacao"].update(round(correlacao,4))
        window["Conclusao"].update(conclusao)
      # Exibe a soma e a média de X e Y no frame "Stats"
        window['sum_x'].update(str(sum_x))
        window['sum_y'].update(str(sum_y))
        window['mean_x'].update(f'{mean_x:.2f}')
        window['mean_y'].update(f'{mean_y:.2f}')
      # Exibe a e b depois de 2 elementos na tabela, se elementos forem distintos um dos outros
        
        if (len(x) >= 2 or len(y) >= 2) and (len(set(x)) >= 2 or len(set(y)) >= 2):  
              
              b, a = stat.linear_regression(x,y);
              window['-A-'].update(round(a, 2))
              window['-B-'].update(round(b, 2))
    if event == 'Regressao': 
      
      if(len(x) >= 2 or len(y) >= 2) and (len(set(x)) >= 2 or len(set(y)) >=   2):
        calcularReg(values["X_"], values["Y_"],a , b) 
      else: window['error_message'].update("Não há elementos distintos em X e Y suficientes para calcular A e B")
         
   

window.close()

