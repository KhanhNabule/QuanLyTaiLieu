from ManageDocument import ManageDocument
import TaiLieu
from Bao import Bao
from TapChi import TapChi
from Sach import Sach
import datetime

# khởi tạo một đối tượng QuanLySinhVien để quản lý sinh viên
manager = ManageDocument()
while True:
    try:
        print("\nCHUONG TRINH QUAN LY TAI LIEU PYTHON")
        print("********************************MENU******************************")
        print("**  1. Thêm mới tài liệu.                                       **")
        print("**  2. Tìm kiếm tài liệu                  .                     **")
        print("**  3. Sửa thông tin tài liệu.                                  **")
        print("**  4. Sắp xếp tài liệu dựa vào doanh thu theo ngày.            **")
        print("**  5. Sắp xếp tài liệu theo tên.                               **")
        print("**  6. Hiển thị danh sách tạp chí, báo có cùng tháng phát hành. **")
        print("**  7. Hiển thị tài liệu bán chạy cần nhập thêm.                **")
        print("**  8. Xóa tài liệu.                                            **")
        print("**  9. Hiển thị danh sách tài liệu.                             **")
        print("**  0. Thoat                                                    **")
        print("******************************************************************")

        key = int(input("Nhap tuy chon: "))
        if (key == 1):
            print("\n1. Thêm mới tài liệu.")
            theLoai = input("Chọn thể loại muốn thêm: ")
            if (theLoai == "Sách"):
                maTaiLieu = input("Nhập mã tài liệu: ")
                tenNSB = input("Nhập tên nhà xuất bản: ")
                soLuongTonKho = int(input("Nhập số lượng tồn kho: "))
                soLuongBan = int(input("Nhập số lượng bán: "))
                giaBan = float(input("Nhập giá bán: "))
                tenTacGia = input("Nhập tên tác giả: ")
                soTrang = int(input("Nhập số trang: "))
                sach = Sach(maTaiLieu, tenNSB, soLuongTonKho, soLuongBan, giaBan, tenTacGia, soTrang)
                manager.themTaiLieu(sach)
            elif (theLoai == "Tạp Chí"):
                maTaiLieu = input("Nhập mã tài liệu: ")
                tenNSB = input("Nhập tên nhà xuất bản: ")
                soLuongTonKho = int(input("Nhập số lượng tồn kho: "))
                soLuongBan = int(input("Nhập số lượng bán: "))
                giaBan = float(input("Nhập giá bán: "))
                soPhatHanh = int(input("Nhập số phát hành: "))
                thangPhatHanh = int(input("Nhập tháng phát hành: "))
                tapChi = TapChi(maTaiLieu, tenNSB, soLuongTonKho, soLuongBan, giaBan, soPhatHanh, thangPhatHanh)
                manager.themTaiLieu(tapChi)
            elif (theLoai == "Báo"):
                maTaiLieu = input("Nhập mã tài liệu: ")
                tenNSB = input("Nhập tên nhà xuất bản: ")
                soLuongTonKho = int(input("Nhập số lượng tồn kho: "))
                soLuongBan = int(input("Nhập số lượng bán: "))
                giaBan = float(input("Nhập giá bán: "))

                while True:
                    date_str = input("Ngày phát hành (định dạng yyyy-mm-dd): ")
                    try:
                        ngayPhatHanh = datetime.datetime.strptime(date_str, "%Y-%m-%d")
                        break
                    except ValueError:
                        print("Định dạng không đúng. Vui lòng nhập lại.")

                bao = Bao(maTaiLieu, tenNSB, soLuongTonKho, soLuongBan, giaBan, ngayPhatHanh)
                manager.themTaiLieu(bao)
            else:
                print("Không tìm thấy tài liệu cần thêm")
            print("\nThêm tài liệu thành công!")
        elif (key == 2):
            if (manager.soLuongDocument() > 0):
                print("\n2. Tìm kiếm theo tên nhà xuất bản.")
                print("\nNhập tên để tìm kiếm: ")
                name = input()
                search_result = manager.searchTaiLieu(name)
                for tai_lieu in search_result:
                    print(tai_lieu.get_info())
            else:
                print("\nDanh sách rỗng")
        elif (key == 3):
            if (manager.soLuongDocument() > 0):
                print("\n3. Cập nhật tài liệu. ")
                print("\nNhập mã tài liệu: ")
                maTaiLieu = input()
                manager.updateTaiLieu(maTaiLieu)
        elif (key == 4):
            if (manager.soLuongDocument() > 0):
                print("\n4. Sắp xếp tài liệu dựa vào doanh thu theo ngày.")
                lua_chon = input("Sap xep (tang hoac giam) ? ")
                manager.sapxeptheodoanhthu(lua_chon)
            else:
                print("\nSanh sach sinh vien trong!")
        elif (key == 5):
            if (manager.soLuongDocument() > 0):
                print("\n5. Sắp xếp tài liệu theo tên.")
                luaChon = input("Vui long lựa chọn sắp xếp từ a->z hay từ z->a: ")
                manager.sapXepTaiLieu(luaChon)
                manager.showDocument()
            else:
                print("\nDanh sách rỗng")
        elif (key == 6):
            if (manager.soLuongDocument() > 0):
                print("\n6. Hiển thị danh sách tạp chí, báo có cùng tháng phát hành.")
                thang = input("Thang phat hanh ? ")
                manager.hienthicungthang(thang)
            else:
                print("\nSanh sach sinh vien trong!")
        elif (key == 7):
            if (manager.soLuongDocument() > 0):
                print("\n7. Hiển thị danh sách bán chạy cần nhập thêm.")
                manager.displayTaiLieuBanChay()
            else:
                print("\nDanh sách rỗng")
        elif (key == 8):
            if (manager.soLuongDocument() > 0):
                print("\n8.Xóa tài liệu: ")
                maTaiLieu = input()
                if (manager.deleteTaiLieu(maTaiLieu)):
                    print("\nTài liệu co ma tai lieu = ", maTaiLieu, " da bi xoa.")
                    break
                else:
                    print("\nSinh vien co id = ", maTaiLieu, " khong ton tai.")
            else:
                print("\nDanh sách rỗng!")
        elif (key == 9):
            if (manager.soLuongDocument() > 0):
                print("\n9. Hien thi danh sach tai lieu.")
                manager.showDocument()
            else:
                print("\nDanh sách rỗng")
        elif (key == 0):
            print("\nBan da chon thoat chuong trinh!")
            break
        else:
            print("\nKhong co chuc nang nay!")
            print("\nHay chon chuc nang trong hop menu.")
    except ValueError as ve:
        print(f"\nLỗi: {ve}. Vui lòng nhập một số thực.")
    except Exception as e:
        print(f"\nLỗi không xác định: {e}")
