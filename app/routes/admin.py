from flask import Blueprint, render_template, request, redirect, url_for
from app.services import nhanvien_service as nv

bp = Blueprint("admin", __name__)

#=== Danh sách nhân viên ===
@bp.route('/nhanvien')
def danhsach_nhanvien():
    tuKhoa = request.args.get('keyword', '').strip().lower()

    nhanviens = nv.get_nhanviens()
    ketQua = nhanviens

    if tuKhoa:
        ketQua = [
            nhanvien for nhanvien in nhanviens
            if tuKhoa in nhanvien['maNV'].lower()
            or tuKhoa in nhanvien['hoTen'].lower()
            or tuKhoa in nhanvien['sdt'].lower()
        ]

    return render_template(
        'admin/nhanvien/danhsach.html',
        nhanviens=ketQua
    )


#=== Thêm nhân viên ===
@bp.route('/nhanvien/them', methods=['GET', 'POST'])
def them_nhanvien():
    if request.method == 'POST':
        nhanvien = {
            'maNV': request.form.get('maNV', '').strip(),
            'hoTen': request.form.get('hoTen', '').strip(),
            'ngaySinh': request.form.get('ngaySinh', ''),
            'gioiTinh': request.form.get('gioiTinh', ''),
            'sdt': request.form.get('sdt', '').strip(),
            'diaChi': request.form.get('diaChi', '').strip(),
            'chucVu': request.form.get('chucVu', ''),
            'ngayVaoLam': request.form.get('ngayVaoLam', ''),
            'trangThai': request.form.get('trangThai', 'Đang làm')
        }

        if not nhanvien['maNV'] or not nhanvien['hoTen']:
            return render_template(
                'admin/nhanvien/them.html',
                err_msg='Mã nhân viên và họ tên không được để trống!'
            )

        if nv.add_nhanviens(nhanvien):
            return redirect(url_for('admin.danhsach_nhanvien'))

        return render_template(
            'admin/nhanvien/them.html',
            err_msg='Mã nhân viên đã tồn tại!'
        )

    return render_template('admin/nhanvien/them.html')


#=== Cập nhật nhân viên ===
@bp.route('/nhanvien/capnhat/<maNV>', methods=['GET', 'POST'])
def capnhat_nhanvien(maNV):
    nhanvien = nv.get_nhanviens_getID(maNV)

    if nhanvien is None:
        return redirect(url_for('admin.danhsach_nhanvien'))

    if request.method == 'POST':
        data = {
            'hoTen': request.form.get('hoTen', '').strip(),
            'ngaySinh': request.form.get('ngaySinh', ''),
            'gioiTinh': request.form.get('gioiTinh', ''),
            'sdt': request.form.get('sdt', '').strip(),
            'diaChi': request.form.get('diaChi', '').strip(),
            'chucVu': request.form.get('chucVu', ''),
            'ngayVaoLam': request.form.get('ngayVaoLam', ''),
            'trangThai': request.form.get('trangThai', '')
        }

        if not data['hoTen']:
            return render_template(
                'admin/nhanvien/capnhat.html',
                nhanvien=nhanvien,
                err_msg='Họ tên không được để trống!'
            )

        nv.update_nhanviens(maNV, data)

        return redirect(url_for('admin.danhsach_nhanvien'))

    return render_template(
        'admin/nhanvien/capnhat.html',
        nhanvien=nhanvien
    )


#=== Xóa nhân viên ===
@bp.route('/nhanvien/xoa/<maNV>', methods=['POST'])
def xoa_nhanvien(maNV):
    nv.delete_nhanviens(maNV)

    return redirect(url_for('admin.danhsach_nhanvien'))


