import os
from amzqr import amzqr


# create a qr code
version, level, qr_name = amzqr.run(
    words="https://u.wechat.com/EIL6skVzHJtHA5ZRGTCRM60",
    version=1,
    level='H',
    picture="girl.gif",
    colorized=True,
    contrast=1.0,
    brightness=1.0,
    save_name="wechat.gif",
    save_dir=os.getcwd()
)
