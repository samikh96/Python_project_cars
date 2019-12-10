import json
import os
from Write_to_db import Table
def open_file():
    with open('\\Users\Mohammad Khwaja\.PyCharmCE2019.2\config\scratches\json_destination\watchdog_file.json','r') as cardata:
        data = json.load(cardata)
        cartable = Table()
        print(data)
        cartable.create_operation(data)
    os.remove('\\Users\Mohammad Khwaja\.PyCharmCE2019.2\config\scratches\json_destination\watchdog_file.json')




