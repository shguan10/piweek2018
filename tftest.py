import classify_image as ci
from classify_image import identify
from pprint import pprint as pp
from time import sleep
ci.create_graph()
pp(identify("tmp.jpg"))
pp(identify("tmp.jpg"))
sleep(20000)
