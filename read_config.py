import json

def read_config():
    """
    Metodo para retornar as config do usuario
    """
    try:
        with open("./config.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            f.close()
    except Exception as err:
        print(f"{err}, arquivo não encontrado")
        dictionary = {
            "path_config": "",
            "path_dwg": "",
            "path_qrcode": "",
        }
        json_object = json.dumps(dictionary, indent=4)
        with open("./config.json", "w", encoding="utf-8") as f:
            f.write(json_object)
            f.close()

    with open("./config.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        f.close()

    return data


def write(config, path):
    """
    Metodo para escrver as config do usuario
    """
    if config == 'initial_dir':
        with open("config.json", "r", encoding="utf-8") as json_file:
            data = json.load(json_file)
            json_file.close()

        data[config] = path
        with open("config.json", "w", encoding="utf-8") as json_file:
            json.dump(data, json_file)

    if config == 'path_dwg':
        with open("config.json", "r", encoding="utf-8") as json_file:
            data = json.load(json_file)
            json_file.close()

        data[config] = path
        with open("config.json", "w", encoding="utf-8") as json_file:
            json.dump(data, json_file)

    if config == 'path_qrcode':
        with open("config.json", "r", encoding="utf-8") as json_file:
            data = json.load(json_file)
            json_file.close()

        data[config] = path
        with open("config.json", "w", encoding="utf-8") as json_file:
            json.dump(data, json_file)
