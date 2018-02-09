#Sessão de importação

import _thread
from threading import Thread
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
import os

#Sessão de importação espec[ifica do calculo Simplex
import playsound
from numpy import multiply
from scipy.optimize import linprog

##########################################################################################################
#                                                                                                        #
# Desenvolvedores: Thales da Silva Neves, Verônica Sakai, José Antônio Gonçalves                         #
# Turma: 5ºADS Vespertino                                                                                #
#                                                                                                        #
##########################################################################################################

class FrameTkinter(object):

    def inicilizarFrame(self, args, parent):

        def clear():
            lblResultadoX1["text"] = ""
            lblResultadoX2["text"] = ""
            lblResultadoX3["text"] = ""
            lblResultadoX4["text"] = ""
            lblResultadoX5["text"] = ""
            lblResultadoX6["text"] = ""
            lblResultadoX7["text"] = ""
            lblResultadoZ["text"] = ""

        def on_closing():
            if messagebox.askokcancel("Sair", "Deseja realmente sair?"):
                sys.exit(0)

        def btnCalcularClick():

            try:

                # Função objetiva
                c = [float(str(funcaoObjetivaX1.get()).replace(',', '.')),
                     float(str(funcaoObjetivaX2.get()).replace(',', '.')),
                     float(str(funcaoObjetivaX3.get()).replace(',', '.')),
                     float(str(funcaoObjetivaX4.get()).replace(',', '.'))]

                # Restrições técnicas
                A = [[float(restricoesTecnicasX11.get()),
                      float(restricoesTecnicasX12.get()),
                      float(restricoesTecnicasX13.get()),
                      float(restricoesTecnicasX14.get())],
                     [float(restricoesTecnicasX21.get()),
                      float(restricoesTecnicasX22.get()),
                      float(restricoesTecnicasX23.get()),
                      float(restricoesTecnicasX24.get())],
                     [float(restricoesTecnicasX31.get()),
                      float(restricoesTecnicasX32.get()),
                      float(restricoesTecnicasX33.get()),
                      float(restricoesTecnicasX34.get())]]

                # Restrições técnicas maior, igual, menor num depois
                B = [float(restricoesTecnicasMMI1.get()),
                     float(restricoesTecnicasMMI2.get()),
                     float(restricoesTecnicasMMI3.get())]

                if cbObjetivo.get().__eq__("Maximizar"):
                    c = multiply(c, -1)
                if cbSinaisRestricoesTecnicas1.get().__eq__(">="):
                    A[0] = multiply(A[0], -1)
                    B[0] = multiply(B[0], -1)
                if cbSinaisRestricoesTecnicas2.get().__eq__(">="):
                    A[1] = multiply(A[1], -1)
                    B[1] = multiply(B[1], -1)
                if cbSinaisRestricoesTecnicas3.get().__eq__(">="):
                    A[2] = multiply(A[2], -1)
                    B[2] = multiply(B[2], -1)

                x = (0, None)

                resultado = linprog(c, A, B, bounds=(x), options={"disp": False})

                if resultado.status == 0:
                    lblStatus["text"] = "Resolução efetuada com sucesso !!!"
                    if cbObjetivo.get().__eq__("Maximizar"):
                        lblResultadoZ["text"] = (resultado.fun * -1)
                    else:
                        lblResultadoZ["text"] = resultado.fun

                    lblResultadoX1["text"] = resultado.x[0]
                    lblResultadoX2["text"] = resultado.x[1]
                    lblResultadoX3["text"] = resultado.x[2]
                    lblResultadoX4["text"] = resultado.x[3]
                    lblResultadoX5["text"] = resultado.slack[0]
                    lblResultadoX6["text"] = resultado.slack[1]
                    lblResultadoX7["text"] = resultado.slack[2]

                elif resultado.status == 1:
                    lblStatus["text"] = "Falha ao solucionar. Limite de iteração alcançado."
                    clear()
                elif resultado.status == 2:
                    lblStatus["text"] = "Falha ao solucionar. O problema parece ser inviável."
                    clear()
                else:
                    lblStatus["text"] = "Falha ao solucionar. O problema parece ser ilimitado."
                    clear()

            except Exception as e2:
                lblResultadoX1["text"] = "Valores não numéricos"
                lblResultadoX2["text"] = "Valores não numéricos"
                lblResultadoX3["text"] = "Valores não numéricos"
                lblResultadoX4["text"] = "Valores não numéricos"
                lblResultadoX5["text"] = "Valores não numéricos"
                lblResultadoX6["text"] = "Valores não numéricos"
                lblResultadoX7["text"] = "Valores não numéricos"
                lblResultadoZ["text"] = "Valores não numéricos"

        janela = Tk()

        Label(janela, text="").pack()
        janela.title("Método Simplex")

        canvas = Canvas(janela, width=1500, height=1500)
        canvas.pack()
        my_image = PhotoImage(file="ic_python.png")
        canvas.create_image(740, 400, anchor=NW, image=my_image)

        # largura, x, altura, +, Esquerda do vídeo e o Topo
        janela.geometry("1000x600+180+35")

        lblObjetivo = Label(janela, text="Qual o objetivo da função: ")
        lblObjetivo.place(x=430, y=30)

        cbObjetivo = StringVar()
        cbObjetivo = Combobox(parent, textvariable=cbObjetivo, state="readonly")
        cbObjetivo['values'] = ("Maximizar", "Minimizar")
        cbObjetivo.place(x=430, y=50)
        cbObjetivo.current(0)

        ############################################
        #        Bloco da Função Objetiva          #
        ###########################################
        lblFuncaoObjetiva = Label(janela, text="Função: ")
        lblFuncaoObjetiva.place(x=90, y=100)

        funcaoObjetivaX1 = Entry(janela)
        funcaoObjetivaX1.place(x=160, y=100)

        lblFuncaoObjetivaX1 = Label(janela, text="X1 +")
        lblFuncaoObjetivaX1.place(x=300, y=100)

        funcaoObjetivaX2 = Entry(janela)
        funcaoObjetivaX2.place(x=340, y=100)

        lblFuncaoObjetivaX2 = Label(janela, text="X2 +")
        lblFuncaoObjetivaX2.place(x=480, y=100)

        funcaoObjetivaX3 = Entry(janela)
        funcaoObjetivaX3.place(x=530, y=100)

        lblFuncaoObjetivaX3 = Label(janela, text="X3 +")
        lblFuncaoObjetivaX3.place(x=670, y=100)

        funcaoObjetivaX4 = Entry(janela)
        funcaoObjetivaX4.place(x=720, y=100)

        lblFuncaoObjetivaX4 = Label(janela, text="X4")
        lblFuncaoObjetivaX4.place(x=860, y=100)

        ############################################
        #   Bloco das Restrições Técnicas 1       #
        ###########################################
        lblRestricoesTecnicas = Label(janela, text="Restrições Técnicas: ")
        lblRestricoesTecnicas.place(x=430, y=170)

        restricoesTecnicasX11 = Entry(janela)
        restricoesTecnicasX11.place(x=60, y=220)

        lblRestricoesTecnicasX11 = Label(janela, text="X1 +")
        lblRestricoesTecnicasX11.place(x=190, y=220)

        restricoesTecnicasX12 = Entry(janela)
        restricoesTecnicasX12.place(x=230, y=220)

        lblRestricoesTecnicasX12 = Label(janela, text="X2 +")
        lblRestricoesTecnicasX12.place(x=360, y=220)

        restricoesTecnicasX13 = Entry(janela)
        restricoesTecnicasX13.place(x=400, y=220)

        lblRestricoesTecnicasX13 = Label(janela, text="X3 +")
        lblRestricoesTecnicasX13.place(x=530, y=220)

        restricoesTecnicasX14 = Entry(janela)
        restricoesTecnicasX14.place(x=570, y=220)

        lblRestricoesTecnicasX14 = Label(janela, text="X4")
        lblRestricoesTecnicasX14.place(x=700, y=220)

        cbSinaisRestricoesTecnicas1 = StringVar()
        cbSinaisRestricoesTecnicas1 = Combobox(parent, textvariable=cbSinaisRestricoesTecnicas1, width=2, state="readonly")
        cbSinaisRestricoesTecnicas1['values'] = ('<=', '>=', '=')
        cbSinaisRestricoesTecnicas1.place(x=740, y=220)
        cbSinaisRestricoesTecnicas1.current(0)

        restricoesTecnicasMMI1 = Entry(janela)
        restricoesTecnicasMMI1.place(x=800, y=220)

        ############################################
        #   Bloco das Restrições Técnicas 2       #
        ###########################################
        restricoesTecnicasX21 = Entry(janela)
        restricoesTecnicasX21.place(x=60, y=280)

        lblRestricoesTecnicasX21 = Label(janela, text="X1 +")
        lblRestricoesTecnicasX21.place(x=190, y=280)

        restricoesTecnicasX22 = Entry(janela)
        restricoesTecnicasX22.place(x=230, y=280)

        lblRestricoesTecnicasX22 = Label(janela, text="X2 +")
        lblRestricoesTecnicasX22.place(x=360, y=280)

        restricoesTecnicasX23 = Entry(janela)
        restricoesTecnicasX23.place(x=400, y=280)

        lblRestricoesTecnicasX23 = Label(janela, text="X3 +")
        lblRestricoesTecnicasX23.place(x=530, y=280)

        restricoesTecnicasX24 = Entry(janela)
        restricoesTecnicasX24.place(x=570, y=280)

        lblRestricoesTecnicasX24 = Label(janela, text="X4")
        lblRestricoesTecnicasX24.place(x=700, y=280)

        cbSinaisRestricoesTecnicas2 = StringVar()
        cbSinaisRestricoesTecnicas2 = Combobox(parent, textvariable=cbSinaisRestricoesTecnicas2, width=2, state="readonly")
        cbSinaisRestricoesTecnicas2['values'] = ('<=', '>=', '=')
        cbSinaisRestricoesTecnicas2.place(x=740, y=280)
        cbSinaisRestricoesTecnicas2.current(0)

        restricoesTecnicasMMI2 = Entry(janela)
        restricoesTecnicasMMI2.place(x=800, y=280)

        ############################################
        #   Bloco das Restrições Técnicas 3       #
        ###########################################
        restricoesTecnicasX31 = Entry(janela)
        restricoesTecnicasX31.place(x=60, y=340)

        lblRestricoesTecnicasX31 = Label(janela, text="X1 +")
        lblRestricoesTecnicasX31.place(x=190, y=340)

        restricoesTecnicasX32 = Entry(janela)
        restricoesTecnicasX32.place(x=230, y=340)

        lblRestricoesTecnicasX32 = Label(janela, text="X2 +")
        lblRestricoesTecnicasX32.place(x=360, y=340)

        restricoesTecnicasX33 = Entry(janela)
        restricoesTecnicasX33.place(x=400, y=340)

        lblRestricoesTecnicasX33 = Label(janela, text="X3 +")
        lblRestricoesTecnicasX33.place(x=530, y=340)

        restricoesTecnicasX34 = Entry(janela)
        restricoesTecnicasX34.place(x=570, y=340)

        lblRestricoesTecnicasX34 = Label(janela, text="X4")
        lblRestricoesTecnicasX34.place(x=700, y=340)

        cbSinaisRestricoesTecnicas3 = StringVar()
        cbSinaisRestricoesTecnicas3 = Combobox(parent, textvariable=cbSinaisRestricoesTecnicas3, width=2, state="readonly")
        cbSinaisRestricoesTecnicas3['values'] = ('<=', '>=', '=')
        cbSinaisRestricoesTecnicas3.place(x=740, y=340)
        cbSinaisRestricoesTecnicas3.current(0)

        restricoesTecnicasMMI3 = Entry(janela)
        restricoesTecnicasMMI3.place(x=800, y=340)

        lblRestricoesDeNaoNegatividade = Label(janela, text="X1, X2, X3, X4 ≥ 0")
        lblRestricoesDeNaoNegatividade.place(x=450, y=420)

        ############################################
        #   Bloco dos resultados das variáveis     #
        ###########################################
        lblR = Label(janela, text="Resultados: ")
        lblR.place(x=60, y=380)

        lblX1 = Label(janela, text="X1: ")
        lblX1.place(x=70, y=400)

        lblResultadoX1 = Label(janela, text="0")
        lblResultadoX1.place(x=100, y=400)

        lblX2 = Label(janela, text="X2: ")
        lblX2.place(x=70, y=420)

        lblResultadoX2 = Label(janela, text="0")
        lblResultadoX2.place(x=100, y=420)

        lblX3 = Label(janela, text="X3: ")
        lblX3.place(x=70, y=440)

        lblResultadoX3 = Label(janela, text="0")
        lblResultadoX3.place(x=100, y=440)

        lblX4 = Label(janela, text="X4: ")
        lblX4.place(x=70, y=460)

        lblResultadoX4 = Label(janela, text="0")
        lblResultadoX4.place(x=100, y=460)

        lblX5 = Label(janela, text="X5: ")
        lblX5.place(x=70, y=480)

        lblResultadoX5 = Label(janela, text="0")
        lblResultadoX5.place(x=100, y=480)

        lblX6 = Label(janela, text="X6: ")
        lblX6.place(x=70, y=500)

        lblResultadoX6 = Label(janela, text="0")
        lblResultadoX6.place(x=100, y=500)

        lblX7 = Label(janela, text="X7: ")
        lblX7.place(x=70, y=520)

        lblResultadoX7 = Label(janela, text="0")
        lblResultadoX7.place(x=100, y=520)

        lblZ = Label(janela, text="Z: ")
        lblZ.place(x=70, y=540)

        lblResultadoZ = Label(janela, text="0")
        lblResultadoZ.place(x=100, y=540)

        lblStatus = Label(janela, text="Status: ")
        lblStatus.place(x=70, y=560)

        lblStatus = Label(janela, text=" ")
        lblStatus.place(x=110, y=560)

        # self.box.grid(column=0, row=0)

        btnCalcular = Button(janela, width=20, height=2, text="Calcular", font="bold", command=btnCalcularClick,
                             bg="#E0FFFF")
        btnCalcular.place(x=410, y=500)

        janela.protocol("WM_DELETE_WINDOW", on_closing)

        # tmp = Thread(target=lambda:musica("mp3"))
        # tmp.setDaemon(True)
        # tmp.start()
        # tmp.run()

        # tmp = Thread(target=lambda : playsound.playsound("Kygo - ID - Ultra Music Festival Anthem.mp3"))
        # tmp.start()

        janela.mainloop()

#def musica(args):
#    playsound.playsound("Kygo - ID - Ultra Music Festival Anthem.mp3")


if __name__ == '__main__':

    # ft = _thread.start_new_thread(lambda : FrameTkinter().inicilizarFrame("inicializando", parent=""), ())
    # _thread.start_new_thread(musica("mp3"), ())
    # playsound.playsound("Kygo - ID - Ultra Music Festival Anthem.mp3")
    p = FrameTkinter().inicilizarFrame("in", parent="")

    # tmp = Thread(target=lambda : FrameTkinter().inicilizarFrame("s", parent=""))
    # tmp = Thread(target=musica("mp3"))
    # tmp.setDaemon(False)
    # tmp.start()

    # fT = FrameTkinter().inicilizarFrame("inicializando", parent="")
