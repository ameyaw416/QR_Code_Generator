import segno
qrcode = segno.make_qr("https://bulkclix.com/pay/w9wlAHh")
qrcode.save(
    "HAJIA KANDEs DELIGHT.png",
    scale=100,
    border=10,
)