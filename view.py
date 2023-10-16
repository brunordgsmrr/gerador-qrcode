import tkinter.messagebox
from tkinter import Tk, filedialog, StringVar
from tkinter import ttk

import app
from config import *
import os


class App_View(ttk.Frame):
    def __init__(self, title):

        self.config = Config()

        self.root = Tk()
        self.root.title(title)
        self.root.tk.call("source", "azure.tcl")
        self.root.tk.call("set_theme", "dark")

        ttk.Frame.__init__(self, self.root)

        self.initial_dir = StringVar()
        self.dwg_path = StringVar()
        self.qrcode_path = StringVar()
        self.result = StringVar()
        self.update_config()
        self.setup_widgets()
        self.root.mainloop()

    def setup_widgets(self):

        # Frame principal das configurações
        self.frame_conf = ttk.LabelFrame(self.root, text="Configurações", padding=(10, 10))
        self.frame_conf.grid(row=0, column=0, padx=(10, 10), pady=(20, 10), sticky="nsew")

        # Frame 1: Guias de fabricação
        self.frame = ttk.LabelFrame(self.frame_conf, text="Pasta com as Guias de Fabricação", padding=(20, 10))
        self.frame.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew")
        self.label = ttk.Label(self.frame, textvariable=self.initial_dir)
        self.label.pack(side='left')
        # Botão 1: Guia de fabricação
        self.btn = ttk.Button(self.frame_conf,
                              text='DEFINIR LOCAL DAS GUIAS DE FABRICAÇÃO',
                              width=40,
                              command=lambda: self.ask_dir('ini'))
        self.btn.grid(row=1, column=0, padx=0, pady=5, sticky='nsew')

        # Frame 2: Local QRCode
        self.frame = ttk.LabelFrame(self.frame_conf, text="Local para os QRCode", padding=(20, 10))
        self.frame.grid(row=2, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew")
        self.label = ttk.Label(self.frame, textvariable=self.qrcode_path)
        self.label.pack(side='left')
        # Botão 2: Buscar QRCode
        self.btn = ttk.Button(self.frame_conf,
                              text='DEFINIR LOCAS DOS QRCodes',
                              width=40,
                              command=lambda: self.ask_dir('qrc'))
        self.btn.grid(row=3, column=0, padx=0, pady=5, sticky='nsew')

        # Frame principal do gerador de QRCode
        self.frame_gera = ttk.LabelFrame(self.root, text="Gerador de QRCode", padding=(10, 10))
        self.frame_gera.grid(row=1, column=0, padx=(10, 10), pady=(20, 10), sticky="ns")

        self.frame = ttk.LabelFrame(self.frame_gera, text="Pasta com os desenhos da Guia de Fabricação", padding=(20, 10))
        self.frame.grid(row=2, column=0, padx=(10, 10), pady=(10, 10), sticky="ns")
        self.label = ttk.Label(self.frame, textvariable=self.dwg_path)
        self.label.pack(side='left')

        self.btn = ttk.Button(self.frame_gera,
                              text='BUSCAR DESENHOS',
                              width=40,
                              command=lambda: self.ask_dir('dwg'))
        self.btn.grid(row=8, column=0, padx=0, pady=10, sticky='ns')

        self.btn = ttk.Button(self.frame_gera,
                              text='GERAR QRCODE DOS DESENHOS',
                              width=40,
                              style="Accent.TButton",
                              command=lambda: self.call_generator())
        self.btn.grid(row=9, column=0, padx=0, pady=10, sticky='ns')

    def update_config(self):

        self.dwg_path.set('Selecione os DWGs da Guia de fabricação')

        if self.config.data['initial_dir'] is '':
            self.initial_dir.set('Definir o local das GFs')
        else:
            self.initial_dir.set(self.config.data['initial_dir'])

        if self.config.data['path_qrcode'] is '':
            self.qrcode_path.set('Defina um local para salvar os QRCodes')
        else:
            self.qrcode_path.set(self.config.data['path_qrcode'])

    def ask_dir(self, option, new_data=None):
        if option is 'ini':
            new_data = filedialog.askdirectory(initialdir=self.initial_dir.get())
            self.config.alter_config(option, new_data)
            self.update_config()
        elif option is 'dwg':
            new_data = filedialog.askdirectory(initialdir=self.initial_dir.get())
            self.config.alter_config(option, new_data)
            self.update_config()
            self.dwg_path.set(new_data)
            pass
        elif option is 'qrc':
            new_data = filedialog.askdirectory(initialdir=f'{os.getenv("USERPROFILE")}/Documents')
            self.config.alter_config(option, new_data)
            self.update_config()

    def call_generator(self):

        if app.generate_qrcode(self.dwg_path.get(), self.qrcode_path.get()):
            self.result.set("QRCodes gerados")
            self.confirm_box = tkinter.messagebox.showinfo(title='Confimação', message=self.result.get())
        else:
            self.result.set('Não foi possível gerar os qrcodes')
            self.confirm_box = tkinter.messagebox.showerror(title='Confimação', message=self.result.get())