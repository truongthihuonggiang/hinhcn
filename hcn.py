class Hcn:
    x1= 0
    y1 = 0
    x2 = 0
    y2 = 0
    maunen = "white"
    duongvien = "black"
    def __init__(self, x1 = 0, y1 = 0, x2 = 0, y2= 0, maunen = "white", duongvien = "black"):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.duongvien = duongvien
        self.maunen = maunen
    def vehinh (self, cas):
        self.hinh = cas.create_rectangle(self.x1,self.y1,self.x2,self.y2,outline = self.duongvien,fill = self.maunen)
    def xoahinh(self,cas):
        if self.hinh:
            cas.delete(self.hinh)

    def dichlen(self):
        self.y1 = self.y1 - 10
        self.y2 = self.y2 - 10 

    def dichxuong(self):
        self.y1 = self.y1 + 10
        self.y2 = self.y2 + 10
    
    def dichphai(self):
        self.x1 = self.x1 + 10
        self.x2 = self.x2 + 10
    def dichtrai (self):
        self.x1 = self.x1 - 10
        self.x2 = self.x2 - 10