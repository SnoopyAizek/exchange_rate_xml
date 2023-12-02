from datetime import datetime

from lxml import etree
from zeep import Client
from zeep.plugins import HistoryPlugin

history = HistoryPlugin()
dt = datetime.now()
client = Client(
    "http://www.cbr.ru/DailyInfoWebServ/DailyInfo.asmx?WSDL", plugins=[history])
xml = client.service.GetCursOnDateXML(dt)
for elt in xml.getiterator():
    if elt.tag == 'Vname':
        elt.text = elt.text.rstrip()
with open("exchange_rates.xml", "w", encoding="utf-8") as file_save:
    file_save.write(etree.tostring(xml, encoding='unicode', pretty_print=True))
