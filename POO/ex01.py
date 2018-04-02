class Televisao:
    def __init__(self, min = 2, max = 20):
        self.canal = 2
        self.ligada = True
        self.__cmin = min
        self.__cmax = max

    def aumenta_canal(self):
        self.canal = self.canal + 1
        if (self.canal > self.__cmax):
            self.canal = self.__cmin


    def diminui_canal(self):
        self.canal = self.canal - 1
        if (self.canal < self.__cmin):
            self.canal = self.__cmax


tv = Televisao(2, 5)

for i in range(10):
    tv.aumenta_canal()
    print(tv.canal)


