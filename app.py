# This is a sample Python script.
from view import *
import os
import qrcode

def generate_qrcode(path_dwg, path_qrcode):

    try:
        dwg_list = os.listdir(path_dwg)

        for i in dwg_list:
            if '.dwg' in i:
                qr = qrcode.QRCode(version=1, box_size=60, border=1)
                qr.add_data(i[0:14])
                qr.make(fit=True)
                image = qr.make_image(fill_color='black', back_color='white')
                image.save(f'{path_qrcode}/QR{i[0:14]}.png')
        return True
    except FileNotFoundError:
        return False


def main():

    App_View('Gerador de QRCode')



if __name__ == '__main__':
    main()
