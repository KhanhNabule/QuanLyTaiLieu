from TaiLieu import TaiLieu
class TapChi(TaiLieu):
    def __init__(self, maTaiLieu, tenNSB, soLuongTonKho, soLuongBan, giaBan, soPhatHanh, thangPhatHanh):
        super().__init__(maTaiLieu, tenNSB, soLuongTonKho, soLuongBan, giaBan)
        self.soPhatHanh = soPhatHanh
        self.thangPhatHanh = thangPhatHanh

    def set_info(self, maTaiLieu, tenNSB, soLuongTonKho, soLuongBan, giaBan, soPhatHanh, thangPhatHanh):
        super().set_info(maTaiLieu, tenNSB, soLuongTonKho, soLuongBan, giaBan)
        self.soPhatHanh = soPhatHanh
        self.thangPhatHanh = thangPhatHanh

    def set_maTaiLieu(self, maTaiLieu):
        self.maTaiLieu = maTaiLieu
    def set_tenNSB(self, tenNSB):
        self.tenNSB = tenNSB
    def set_soLuongTonKho(self, soLuongTonKho):
        self.soLuongTonKho = soLuongTonKho
    def set_soLuongBan(self, soLuongBan):
        self.soLuongBan = soLuongBan
    def set_giaBan(self, giaBan):
        self.giaBan = giaBan
    def set_soPhatHanh(self, soPhatHanh):
        self.soPhatHanh = soPhatHanh
    def set_thangPhatHanh(self, thangPhatHanh):
        self.thangPhatHanh = thangPhatHanh

    def get_maTaiLieu(self):
        return self.maTaiLieu
    def get_tenNSB(self):
        return self.tenNSB
    def get_soLuongTonKho(self):
        return self.soLuongTonKho
    def get_soLuongBan(self):
        return self.soLuongBan
    def get_giaBan(self):
        return self.giaBan
    def get_soPhatHanh(self):
        return self.soPhatHanh
    def get_thangPhatHanh(self):
        return self.thangPhatHanh

    def get_info(self):
        return super().get_info() + f", Số phát hành: {self.soPhatHanh}, Tháng phát hành: {self.thangPhatHanh}"