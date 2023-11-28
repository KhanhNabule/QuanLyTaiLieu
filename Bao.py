from TaiLieu import TaiLieu
class Bao(TaiLieu):
    def __init__(self, maTaiLieu, tenNSB, soLuongTonKho, soLuongBan, giaBan, ngayPhatHanh):
        super().__init__(maTaiLieu, tenNSB, soLuongTonKho, soLuongBan, giaBan)
        self.ngayPhatHanh = ngayPhatHanh

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
    def set_ngayPhatHanh(self, ngayPhatHanh):
        self.ngayPhatHanh = ngayPhatHanh

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
    def get_ngayPhatHanh(self):
        return self.ngayPhatHanh

    def get_info(self):
        return super().get_info() + f", Ngày phát hành: {self.ngayPhatHanh}"