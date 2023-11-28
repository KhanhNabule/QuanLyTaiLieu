class TaiLieu:
    def __init__(self, maTaiLieu, tenNSB, soLuongTonKho, soLuongBan, giaBan):
        self.maTaiLieu = maTaiLieu
        self.tenNSB = tenNSB
        self.soLuongTonKho = soLuongTonKho
        self.soLuongBan = soLuongBan
        self.giaBan = giaBan

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

    def get_info(self):
        return (f"Mã tài liệu: {self.maTaiLieu}, Tên nhà xuất bản: {self.tenNSB}, Số lượng tồn kho: {self.soLuongTonKho},"
                f" Số lượng bán (theo ngày): {self.soLuongBan}, Giá bán: {self.giaBan}")