import json


class Config:
    def __init__(self):
        self.has_config()

    def has_config(self):
        try:
            with open('./config.json', 'r', encoding='utf-8') as f:
                self.data = json.load(f)
                f.close()
        except Exception as err:
            print(f"{err}, arquivo não encontrado")
            dictionary = {
                "initial_dir": "",
                "path_dwg": "",
                "path_qrcode": "",
            }
            self.data = json.dumps(dictionary, indent=4)
            with open("./config.json", "w", encoding="utf-8") as f:
                f.write(self.data)
                f.close()

    def alter_config(self, option, new_data):
        if option == 'ini':
            self.data['initial_dir'] = new_data
        elif option == 'dwg':
            self.data['path_dir'] = new_data
        elif option == 'qrc':
            self.data['path_qrcode'] = new_data
        self.update_config()

    def update_config(self):
        with open("./config.json", "w", encoding="utf-8") as f:
            json.dump(self.data, f)
            f.close()