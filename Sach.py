from TaiLieu import TaiLieu
class Sach(TaiLieu):
    def __init__(self, maTaiLieu, tenNSB, soLuongTonKho, soLuongBan, giaBan, tenTacGia, soTrang):
        super().__init__(maTaiLieu, tenNSB, soLuongTonKho, soLuongBan, giaBan)
        self.tenTacGia = tenTacGia
        self.soTrang = soTrang

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
    def set_tenTacGia(self, tenTacGia):
        self.tenTacGia = tenTacGia
    def set_soTrang(self, soTrang):
        self.soTrang = soTrang

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
    def get_tenTacGia(self):
        return self.tenTacGia
    def get_soTrang(self):
        return self.soTrang

    def get_info(self):
        return super().get_info() + f", Tên tác giả: {self.tenTacGia}, Số trang: {self.soTrang}"