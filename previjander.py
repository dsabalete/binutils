from Tkinter import *
from PIL import Image, ImageTk
import urllib
import os


proxies = {'http': 'http://10.2.201.33:8080'}

url = ["http://www.meteo.cat/servmet/modelitzacio/wamgn00/alturah_1.gif",
        "http://www.meteo.cat/servmet/modelitzacio/wamgn00/alturah_4.gif",
        "http://www.meteo.cat/servmet/modelitzacio/wamgn00/alturah_7.gif",
        "http://www.meteo.cat/servmet/modelitzacio/wamgn00/alturah_10.gif",
        "http://www.meteo.cat/servmet/modelitzacio/wamgn00/alturah_13.gif",
        "http://www.meteo.cat/servmet/modelitzacio/wamgn00/alturah_16.gif",
        "http://www.meteo.cat/servmet/modelitzacio/wamgn00/alturah_19.gif",
        "http://www.meteo.cat/servmet/modelitzacio/wamgn00/alturah_22.gif",
        "http://www.meteo.cat/servmet/modelitzacio/wamgn00/alturah_25.gif",
        "http://www.meteo.cat/servmet/modelitzacio/wamgn00/alturah_28.gif",
        "http://www.meteo.cat/servmet/modelitzacio/wamgn00/alturah_31.gif",
        "http://www.meteo.cat/servmet/modelitzacio/wamgn00/alturah_34.gif",
        "http://www.meteo.cat/servmet/modelitzacio/wamgn00/alturah_37.gif"]

class MyApp(Tk):
        def __init__(self):
                Tk.__init__(self)
                fr = Frame(self)
                fr.pack()
                self.canvas = Canvas(fr, height = 420, width = 565)
                self.canvas.pack()

                self.old_label_image = None
                self.position = 0
#                self.getCommand()
                self.slideshow()

        def slideshow(self):
                file = str(self.position) + '.gif'
                image1 = Image.open(file)
                self.tkpi = ImageTk.PhotoImage(image1)
                label_image = Label(self, image=self.tkpi)
                label_image.place(x=0, y=0, width=image1.size[0], height=image1.size[1])
                #self.title("Title: " + file + " - " + str(self.lastCommand))
                self.title("Title: " + file)

                if self.old_label_image is not None:
                        self.old_label_image.destroy()
                self.old_label_image = label_image

                if self.position is not 12:
                        self.position = self.position + 1
                else:
                        self.position = 0

                huh = self.after(1000, self.slideshow)
                

def grabaFitxer(filename, url):
        file_name = url.split('/')[-1]
        #u = urllib.urlopen(url, proxies=proxies)
        u = urllib.urlopen(url)
        f = open(filename, 'wb')
        meta = u.info()
        file_size = int(meta.getheaders("Content-Length")[0])
        print "Downloading: %s Bytes: %s" % (filename, file_size)

        file_size_dl = 0
        block_sz = 8192
        while True:
                buffer = u.read(block_sz)
                if not buffer:
                        break

                file_size_dl += len(buffer)
                f.write(buffer)
                status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
                status = status + chr(8)*(len(status)+1)
                print status,

        f.close()

def descarregaFitxers(url):
        i = 0
        for x in url:
                filename = "%s.gif" % i
                print filename                
                grabaFitxer(filename, x)
                i = i + 1

def netejaFitxers():
        filelist = [ f for f in os.listdir(".") if f.endswith(".gif")]
        for f in filelist:
                os.remove(f)

descarregaFitxers(url)

if __name__ == "__main__":
        root = MyApp()
        root.mainloop()
        netejaFitxers()
