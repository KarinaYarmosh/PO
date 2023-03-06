#przez okno po nacisnieciu przycisku "Start" zaladowac plik z komputera, zparsowac go i wyswietlic w oknie, zmieniajac liczby na pikseli
from tkinter import *
from tkinter import filedialog

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.line = None
        self.format = None
        self.szerokosc = None
        self.wysokosc = None
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
        # Desaturacja obrazu
        # Negatyw(kolor dopełniający)
        # Kontrast - liniowy, logarytmiczny, potęgowy
        # Jasność(z zachowaniem koloru)
        # Nasycenie
        # Suma, różnica i iloczyn obrazów
        # Ogólne przekształcenie na kanale monochromatycznym
        desaturacjaButton = Button(self, text="Desaturacja", command=self.desaturacja)
        desaturacjaButton.place(x=0, y=60)
        negatywButton = Button(self, text="Negatyw", command=self.negatyw)
        negatywButton.place(x=0, y=90)
        kontrastButton = Button(self, text="Kontrast")
        kontrastButton.place(x=0, y=120)
        jasnoscButton = Button(self, text="Jasność")
        jasnoscButton.place(x=0, y=150)
        nasycenieButton = Button(self, text="Nasycenie")
        nasycenieButton.place(x=0, y=180)
        sumaButton = Button(self, text="Suma")
        sumaButton.place(x=0, y=210)
        roznicaButton = Button(self, text="Różnica")
        roznicaButton.place(x=0, y=240)
        iloczynButton = Button(self, text="Iloczyn")
        iloczynButton.place(x=0, y=270)
        ogolneButton = Button(self, text="Ogólne")
        ogolneButton.place(x=0, y=300)

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
        #wyswietlic obrazki w oknie, zmieniajac liczby na pikseli w formatach PBM, PGM, PPM
        #wyswietlenie obrazka w oknie
        #dziala tylko dla ppm
        self.canvas = Canvas(self, width=self.szerokosc, height=self.wysokosc)
        self.canvas.pack()
        self.img = PhotoImage(file=self.filename)
        self.canvas.create_image(20, 20, anchor=NW, image=self.img)

    def desaturacja(self):
        print("Desaturacja")

    def negatyw(self):
        print("Negatyw")

    def kontrast(self):
        print("Kontrast")
        
    def jasnosc(self):
        print("Jasność")
        
    def nasycenie(self):
        print("Nasycenie")
        
    def suma(self):
        print("Suma")
        
    def roznica(self):
        print("Różnica")
        
    def iloczyn(self):
        print("Iloczyn")
        
    def ogolne(self):
        print("Ogólne")
        
    def client_exit(self):
        exit()

root = Tk()
root.geometry("500x500")
app = Window(root)
root.mainloop()
