from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO

from Scripts.geo import window

window = Tk()
window.title('Cats!')
window.geometry('600x420')