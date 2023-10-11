from tkinter import Tk, filedialog, StringVar
from tkinter import ttk
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
        self.ask_dir('qrc', '')
        self.root.mainloop()

    def setup_widgets(self):

        self.frame = ttk.LabelFrame(self.root, text="Pasta com as Guias de Fabricação", padding=(20, 10))
        self.frame.grid(row=0, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew")
        self.label = ttk.Label(self.frame, textvariable=self.initial_dir)
        self.label.pack(side='left')

        self.frame = ttk.LabelFrame(self.root, text="Pasta com os desenhos da Guia de Fabricação", padding=(20, 10))
        self.frame.grid(row=1, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew")
        self.label = ttk.Label(self.frame, textvariable=self.dwg_path)
        self.label.pack(side='left')

        self.frame = ttk.LabelFrame(self.root, text="Local para os QRCode", padding=(20, 10))
        self.frame.grid(row=3, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew")
        self.label = ttk.Label(self.frame, textvariable=self.qrcode_path)
        self.label.pack(side='left')

        self.frame = ttk.LabelFrame(self.root, text="CONFIGURAÇÕES", padding=(20, 10))
        self.frame.grid(row=4, column=0, padx=20, pady=(10, 10), sticky="nsew", rowspan=3)
        self.btn = ttk.Button(self.frame, text='DEFINIR LOCAL DAS GUIAS DE FABRICAÇÃO', width=40)
        self.btn.grid(row=5, column=0, padx=0, pady=5, sticky='nsew')
        self.btn = ttk.Button(self.frame, text='DEFINIR LOCAS DOS QRCodes', width=40)
        self.btn.grid(row=6, column=0, padx=0, pady=5, sticky='nsew')

        self.frame = ttk.Frame(self.root)
        self.frame.grid(row=7, column=0, padx=20, pady=(10, 10), sticky="nsew", rowspan=3)

        self.btn = ttk.Button(self.frame, text='BUSCAR DESENHOS', width=50)
        self.btn.grid(row=8, column=0, padx=0, pady=10, sticky='nsew')

        self.btn = ttk.Button(self.frame, text='GERAR QRCODE DOS DESENHOS', width=50, style="Accent.TButton")
        self.btn.grid(row=9, column=0, padx=0, pady=10, sticky='nsew')

    def update_config(self):
        print(self.config.data)

        self.dwg_path.set('SELECIONE A PASTA COM OS DWGs DA GUIA DE FABRICAÇÃO')

        if self.config.data['initial_dir'] is '':
            self.initial_dir.set('Definir o local das GFs')
        else:
            self.initial_dir.set(self.config.data['initial_dir'])

        if self.config.data['path_qrcode'] is '':
            self.qrcode_path.set('Defina um local para salvar os QRCodes')
        else:
            self.qrcode_path.set(self.config.data['path_qrcode'])

    def ask_dir(self, option, new_data):
        if option is 'ini':
            self.config.alter_config(option, new_data)
            self.update_config()
        elif option is 'dwg':
            self.config.alter_config(option, new_data)
            self.update_config()
            self.dwg_path.set('new_data')
            pass
        elif option is 'qrc':
            new_data = filedialog.askdirectory(initialdir=f'c:/{os.getenv("USERPROFILE")}/Documents')
            self.config.alter_config(option, new_data)
            self.update_config()
