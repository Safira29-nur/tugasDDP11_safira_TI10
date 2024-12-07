class Gempa:
    #konstraktor inisialisasi dan skala
    def __init__(self, lokasi, skala):
        #atribut
        self.lokasi = lokasi
        self.skala = skala
        
#method menentukakn skala gempa
    def dampak(self):
    #statement/logika
        if self.skala <2:
           print('dampak tidak terasa')
        elif self.skala >=2 and self.skala <=4:
            print('dampak gempa retak-retak')
        elif self.skala >4 and self.skala <6:
            print('dampak gempa bangunan roboh')
        elif self.skala >6:
            print('dampak gempa tsunami')
        
#menampilkan lokasi dan skala
        print(f'lokasi gempa: {self.lokasi}')
        print(f'skala gempa: {self.skala}')

 