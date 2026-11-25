import json
from pathlib import Path
from flask import current_app

def data_path():
    return Path(current_app.config["EMPLOYEE_DATA_PATH"])


# Đọc danh sách nhân viên
def load_nhanviens():
    with open(data_path(), encoding="utf_8") as f:
        return json.load(f)

# Lưu danh sách nhân viên
def save_nhanviens(nhanviens):
    with open(data_path(), "w", encoding="utf-8") as f:
        json.dump(nhanviens, f, ensure_ascii=False, indent=4)

# Lấy danh sách nhân viên
def get_nhanviens():
    return load_nhanviens()

# Tìm nhân viên theo mã
def get_nhanviens_getID(maNV):
    nhanviens = load_nhanviens()

    for nv in nhanviens:
        if nv['maNV'] == maNV:
            return nv

    return None

# Thêm nhân viên
def add_nhanviens(nhanvien):
    nhanviens = load_nhanviens()
    for nv in nhanviens:
        if nv['maNV'] == nhanvien['maNV']:
            return False
    nhanviens.append(nhanvien)
    save_nhanviens(nhanviens)

    return True

# Cập nhật nhân viên
def update_nhanviens(maNV, data):
    nhanviens = load_nhanviens()
    for nv in nhanviens:
        if nv['maNV'] == maNV:
            nv.update(data)
            save_nhanviens(nhanviens)
            return True

    return False

# Xóa nhân viên
def delete_nhanviens(maNV):
    nhanviens = load_nhanviens()
    for nv in nhanviens:
        if nv['maNV'] == maNV:
            nhanviens.remove(nv)
            save_nhanviens(nhanviens)
            return True

    return False