import os
import qrcode


BASE_DIR = os.path.dirname(os.path.dirname(__file__))

OUTPUT = os.path.join(BASE_DIR, "generated")

os.makedirs(
    OUTPUT,
    exist_ok=True
)


def generate_qr(data, filename):

    qr = qrcode.QRCode(
        version=2,
        box_size=6,
        border=2
    )

    qr.add_data(data)

    qr.make(fit=True)

    img = qr.make_image(
        fill_color="black",
        back_color="white"
    )

    path = os.path.join(
        OUTPUT,
        filename
    )

    img.save(path)

    return path