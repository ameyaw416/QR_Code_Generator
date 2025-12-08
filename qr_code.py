import segno
qrcode = segno.make_qr("https://bulkclix.com/pay/PgD7DLr")
qrcode.save(
    "KWAME A BOASIAKO.png",
    scale=100,
    border=10,
)