#przez okno po nacisnieciu przycisku "Start" zaladowac plik z komputera, zparsowac go i wyswietlic w konsole
from tkinter import *
from tkinter import filedialog

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.line = None
        self.format = None
        self.szerokosc = None
        self.wysokosc = None
        self.sprawdzenie = 0
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("GUI")
        self.pack(fill=BOTH, expand=1)
        quitButton = Button(self, text="Quit", command=self.client_exit)
        quitButton.place(x=0, y=0)
        #przycisk start, po nacisnieciu otwiera okno z wyborem pliku
        startButton = Button(self, text="Start", command=self.client_start)
        startButton.place(x=0, y=30)

    def client_start(self):
        #otwiera okno z wyborem pliku
        self.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("pbm files","*.pbm"),
                                                                                                        ("pgm files","*.pgm"),
                                                                                                        ("ppm files","*.ppm"),
                                                                                                        ("all files","*.*")))
        #parsowanie pliku
        self.f = open(self.filename, 'r')
        self.lines = self.f.readlines()
        self.f.close()
        #wyswietlenie w konsoli
        for self.line in self.lines:
            if self.line.startswith('P1') or self.line.startswith('P4'):
                self.format = self.line
                print("PBM: " + self.line)
            elif self.line.startswith('P2') or self.line.startswith('P5'):
                self.format = self.line
                print("PGM: " + self.line)
            elif self.line.startswith('P3') or self.line.startswith('P6'):
                self.format = self.line
                print("PPM: " + self.line)
            #jezeli linia ma tylko 2 elementy to jest to rozmiar obrazu, to pierwszy to szerokosc, drugi to wysokosc
            elif len(self.line.split()) == 2:
                #szerokosc
                self.szerokosc = self.line.split()[0]
                self.wysokosc = self.line.split()[1]
                print("Szerokosc: " + self.szerokosc)
                #wysokosc
                print("Wysokosc: " + self.wysokosc)
            else:
                print(self.line)

    def client_exit(self):
        exit()

root = Tk()
root.geometry("400x300")
app = Window(root)
root.mainloop()