# Aplicação para gerar qrcode para inserir nos desenhos do Autocad
from tkinter import Tk, filedialog,StringVar,Label, Button
import os
import read_config as config
import gerar_qrcode as gerador

def dist_btn(y_atual):
    """Somar a dist no eixo Y"""
    return y_atual + 40

def dist_lbl(y_atual):
    """Somar a dist no eixo Y"""
    return y_atual + 35

def ask_dir_gf():
    """ Metodo para buscar o diretorio da GF"""
    path = filedialog.askdirectory(initialdir=f'c:/{os.getenv("USERPROFILE")}/Documents')
    config.write('initial_dir', path)
    return path

def ask_dir_dwg(initial_dir):
    """ Metodo para buscar o diretorio da DWGs"""
    path = filedialog.askdirectory(initialdir=initial_dir)
    config.write('path_dwg', path)
    return path

def ask_dir_qrcode():
    """ Metodo para retornar o caminho do qrcode """
    path = filedialog.askdirectory(initialdir=f'c:/{os.getenv("USERPROFILE")}/Documents')
    config.write('path_qrcode', path)
    return path

def main_tk(configs):
    window = Tk()
    window.geometry("700x600")
    window.configure(bg='lightblue')

    dist_y = 250
    y_lbl = 20
    resultado = StringVar(value='')

    initial_dir = StringVar()
    if configs['initial_dir'] == '':
        initial_dir.set('Definir o local das GFs')
    else:
        initial_dir.set(configs['initial_dir'])

    dwg_path = StringVar(value='Selecione uma pasta com desenhos da GF')

    qrcode_path = StringVar()
    if configs['path_qrcode'] == '':
        qrcode_path.set('Defina um local para salvar os QRCodes')
    else:
        qrcode_path.set(configs['path_qrcode'])

    # Etiqueta: Pasta das GFs
    label = Label(window, font='Arial 14', text='Pasta com as GFs:')
    label.place(x=15, y=y_lbl)
    y_lbl = dist_lbl(y_lbl)
    label = Label(window, font='Arial 12', textvariable=initial_dir)
    label.place(x=15, y=y_lbl)
    y_lbl = dist_lbl(y_lbl)

    # Etiqueta: Pasta dos DWG para QRCode
    label = Label(window, font='Arial 14', text='Pasta da GF com os desenhos para gerar QRCode:')
    label.place(x=15, y=y_lbl)
    y_lbl = dist_lbl(y_lbl)
    label = Label(window, font='Arial 12', textvariable=dwg_path)
    label.place(x=15, y=y_lbl)
    y_lbl = dist_lbl(y_lbl)

    # Etiqueta: Local dos QRCodes gerados
    label = Label(window, font='Arial 14', text='Local onde sera salvo os QRCode')
    label.place(x=15, y=y_lbl)
    y_lbl = dist_lbl(y_lbl)
    label = Label(window, font='Arial 12', textvariable=qrcode_path)
    label.place(x=15, y=y_lbl)
    y_lbl = dist_lbl(y_lbl)

    # Button: Definir pasta de GFs
    btn_browse = Button(window, text='Definir pasta de GFs',
                        command=lambda: initial_dir.set(ask_dir_gf()))
    btn_browse.place(x=15, y=dist_y)
    dist_y = dist_btn(dist_y)

    # Button: Buscar pasta com os desenhos da GF
    btn_browse = Button(window, text='Buscar pasta com os desenhos da GF',
                        command=lambda: dwg_path.set(ask_dir_dwg(initial_dir.get())))
    btn_browse.place(x=15, y=dist_y)
    dist_y = dist_btn(dist_y)

    # Button: Definir pasta para salvar os QRCodes
    btn_browse = Button(window, text='Definir pasta para salvar os QRCodes',
                        command=lambda: qrcode_path.set(ask_dir_qrcode()))
    btn_browse.place(x=15, y=dist_y)
    dist_y = dist_btn(dist_y)

    # Button: Gerar QRCode
    btn_generate = Button(window, text='Gerar QRCode', bg='lightgreen',
                          command=lambda: resultado.set(gerador.main(dwg_path.get(), qrcode_path.get())))
    btn_generate.place(x=15, y=dist_y)
    dist_y = dist_btn(dist_y)

    # Label: Resultado
    lbl_resulta = Label(window, font='Arial 16', textvariable=resultado)
    lbl_resulta.place(x=50, y=450)

    window.mainloop()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    data_config = config.read_config()
    main_tk(data_config)
