from flask import Blueprint, render_template, request, redirect, url_for

bp = Blueprint("auth", __name__)

#=== Trang chủ ===
@bp.route('/')
def index():
    return redirect(url_for('auth.login'))


#=== Đăng nhập ===
@bp.route('/login', methods=['GET', 'POST'])
def login():
    err_msg = None

    if request.method == 'POST':
        user = request.form.get('username')
        password = request.form.get('password')

        if user == 'admin' and password == '123456':
            return redirect(url_for('admin.danhsach_nhanvien'))
        else:
            err_msg = "Tài khoản hoặc mật khẩu không chính xác!"

    return render_template('auth/login.html', err_msg=err_msg)


