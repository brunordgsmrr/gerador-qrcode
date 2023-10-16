"""
    Programa para gerar Qrcode da lista de desenhoswrite_config_path
"""
import qrcode
import os

def gerar_qrcode(desenho:str, path:str):
    """ Metodo para gerar um Arquivo QRcode """
    if '.dwg' in desenho:
        qr = qrcode.QRCode(version=1, box_size=60, border=1)
        qr.add_data(desenho[0:14])
        qr.make(fit=True)
        image = qr.make_image(fill_color='black', back_color='white')
        image.save(f'{path}/QR{desenho[0:14]}.png')

def main(path_dwg, path_qr):
    """
    Metodo principal, chamando o gerador de qrcode passando o caminho
    para a lista de desenhos e o caminho para salvar os QRCodes
    """
    lista_desenhos = os.listdir(path_dwg)

    for i in lista_desenhos:
        gerar_qrcode(i, path_qr)

    return 'Qrcodes gerados'
