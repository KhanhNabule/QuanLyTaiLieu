import TaiLieu
from Bao import Bao
from TapChi import TapChi
from Sach import Sach

class ManageDocument:
    listDocument = []
    def soLuongDocument(self):
        return self.listDocument.__len__()
        
    def themTaiLieu(self, tailieu):
        self.listDocument.append(tailieu)
        
    def updateTaiLieu(self, maTaiLieu):
        theLoai = input("Nhập thể loại muốn chỉnh sửa: ")
        if (theLoai == "Sách"):
            sach: Sach = self.timTheoMaTaiLieu(maTaiLieu)
            maTaiLieu = input("Nhập mã tài liệu: ")
            tenNSB = input("Nhập tên nhà xuất bản: ")
            soLuongTonKho = int(input("Nhập số lượng tồn kho: "))
            soLuongBan = int(input("Nhập số lượng bán: "))
            giaBan = float(input("Nhập giá bán: "))
            tenTacGia = input("Nhập tên tác giả: ")
            soTrang = int(input("Nhập số trang: "))
            sach.maTaiLieu = maTaiLieu
            sach.tenNSB = tenNSB
            sach.soLuongTonKho = soLuongTonKho
            sach.soLuongBan = soLuongBan
            sach.giaBan = giaBan
            sach.tenTacGia = tenTacGia
            sach.soTrang = soTrang
        elif (theLoai == "Tạp Chí"):
            tapChi: TapChi = self.timTheoMaTaiLieu(maTaiLieu)
            maTaiLieu = input("Nhập mã tài liệu: ")
            tenNSB = input("Nhập tên nhà xuất bản: ")
            soLuongTonKho = int(input("Nhập số lượng tồn kho: "))
            soLuongBan = int(input("Nhập số lượng bán: "))
            giaBan = float(input("Nhập giá bán: "))
            soPhatHanh = int(input("Nhập số phát hành: "))
            thangPhatHanh = int(input("Nhập tháng phát hành: "))
            tapChi.maTaiLieu = maTaiLieu
            tapChi.tenNSB = tenNSB
            tapChi.soLuongTonKho = soLuongTonKho
            tapChi.soLuongBan = soLuongBan
            tapChi.giaBan = giaBan
            tapChi.soPhatHanh = soPhatHanh
            tapChi.thangPhatHanh = thangPhatHanh
        elif (theLoai == "Báo"):
            bao: Bao = self.timTheoMaTaiLieu(maTaiLieu)
            maTaiLieu = input("Nhập mã tài liệu: ")
            tenNSB = input("Nhập tên nhà xuất bản: ")
            soLuongTonKho = int(input("Nhập số lượng tồn kho: "))
            soLuongBan = int(input("Nhập số lượng bán: "))
            giaBan = float(input("Nhập giá bán: "))
            ngayPhatHanh = int(input("Ngày phát hành: "))
            bao.maTaiLieu = maTaiLieu
            bao.tenNSB = tenNSB
            bao.soLuongTonKho = soLuongTonKho
            bao.soLuongBan = soLuongBan
            bao.giaBan = giaBan
            bao.ngayPhatHanh = ngayPhatHanh
        else:
            print("Không tìm thấy tài liệu")

    def timTheoMaTaiLieu(self, maTaiLieu):
        searchResult = None
        if (self.soLuongDocument() > 0):
            for doc in self.listDocument:
                if (doc.maTaiLieu == maTaiLieu):
                    searchResult = doc
        return searchResult

    # sort list theo số lượng
    def sapxepTaiLieu(self, sap_xep):
        if sap_xep == 'tang':
            self.listDocument.sort(key=lambda x: x.get_soLuongTonKho())
        elif sap_xep == 'giam':
            self.listDocument.sort(key=lambda x: x.get_soLuongTonKho(), reverse=True)
        else:
            print("Invalid !!")


    # Hiển thị danh sách tạp chí và báo trong cùng tháng xuất bản
    def hienthicungthang(self, thang):
        for tai_lieu in self.listDocument:
            if isinstance(tai_lieu, TapChi):
                if tai_lieu.get_thangPhatHanh() == int(thang):   # định dạng 'dd'
                    print(tai_lieu.get_info())
            elif isinstance(tai_lieu, Bao):
                date = tai_lieu.get_ngayPhatHanh().strftime('%Y-%m-%d')
                if date.split('-')[1] == thang:   # định dạng 'yyyy-mm-dd'
                    print(tai_lieu.get_info())

    # Doanh thu theo ngày
    def tinhdoanhthumoingay(self,tailieu):
        soluongban = tailieu.get_soLuongBan()
        giaban = tailieu.get_giaBan()
        return soluongban * giaban

    # Sắp xếp tài liệu theo doanh thu theo ngày
    def sapxeptheodoanhthu(self, lua_chon):
        for tai_lieu in self.listDocument:
            if lua_chon == "tang":
                self.listDocument.sort(key=lambda x: self.tinhdoanhthumoingay(x))
            elif lua_chon == "giam":
                self.listDocument.sort(key=lambda x: self.tinhdoanhthumoingay(x), reverse=True)
            else:
                print("Lựa chọn không hợp lệ")


    def sapXepTaiLieu(self, lua_chon):
        if lua_chon == "tang":
            self.listDocument.sort(key=lambda x: x.tenNSB)
        elif lua_chon == "giam":
            self.listDocument.sort(key=lambda x: x.tenNSB, reverse=True)
    def searchTaiLieu(self, tenNSB):
        ket_qua = []
        for doc in self.listDocument:
            if doc.tenNSB == tenNSB:
                ket_qua.append(doc)
        return ket_qua


    def displayTaiLieuBanChay(self):
        TaiLieu_BanChay = sorted(self.listDocument, key=lambda x: (x.soLuongBan, x.soLuongTonKho), reverse=True)
        top5_tonkho_itnhat = TaiLieu_BanChay[:5]
        top5_banchaynhat = TaiLieu_BanChay[:5]
        for TaiLieu in top5_tonkho_itnhat:
            if TaiLieu in top5_banchaynhat:
                print(TaiLieu.get_info())

    def deleteTaiLieu(self, maTaiLieu):
        isDeleted = False
        for doc in self.listDocument:
            if doc.maTaiLieu == maTaiLieu:
                print(f"Xoa tai lieu co ma tai lieu: {maTaiLieu}")
                self.listDocument.remove(doc)
                isDeleted = True
        return isDeleted
    # Hàm hiển thị danh sách sinh viên ra màn hình console
    def showDocument(self):
        for doc in self.listDocument:
            print(doc.get_info())


