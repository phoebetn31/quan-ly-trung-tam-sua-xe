from app.dao import nhanvien_dao as dao

def get_nhanviens():
    return dao.get_nhanviens()

def get_nhanviens_getID(maNV):
    return dao.get_nhanviens_getID(maNV)

def add_nhanviens(nhanvien):
    return dao.add_nhanviens(nhanvien)

def update_nhanviens(maNV, data):
    return dao.update_nhanviens(maNV, data)

def delete_nhanviens(maNV):
    return dao.delete_nhanviens(maNV)
