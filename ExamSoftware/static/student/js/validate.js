var loginController = {
    init: function () {
        loginController.registerEvent();
    },

    registerEvent: function () {
        $('#btnCreate').off('click').on('click', function () {
            var flg = true;

            var txtAddress = $('#txtAddress').val();
            if (txtAddress === "") {
                $('#lblAddress').html('Địa chỉ không được bỏ trống');
                flg = false;
            } else {
                $('#lblAddress').html('');
            }

            var txtFullName = $('#txtFullName').val();
            if (txtFullName === "") {
                $('#lblFullName').html('Họ tên không được bỏ trống');
                flg = false;
            } else {
                $('#lblFullName').html('');
            }

            // email validate
            var txtEmail = $('#txtEmail').val();
            if (txtEmail === "") {
                $('#lblEmail').html('Email không được bỏ trống');
                flg = false;
            } else {
                if (!regexEmail.test(txtEmail)) {
                    $('#lblEmail').html('Email không hợp lệ');
                    flg = false;
                } else {
                    $('#lblEmail').html('');
                }
            }

            //role validate
            var txtRole = $('#txtRole').val();
            if (txtRole === "") {
                $('#lblRole').html('Vai trò không được bỏ trống');
                flg = false;
            } else {
                $('#lblRole').html('');
            }

            //active validate
            var txtActive = $('#txtActive').val();
            if (txtActive === "") {
                $('#lblActive').html('Kích hoạt tài khoản không được bỏ trống');
                flg = false;
            } else {
                $('#lblActive').html('');
            }

            // phonnumber validate
            var txtPhone = $('#txtPhone').val();
            if (txtPhone === "") {
                $('#lblPhone').html('Số điện thoại không được bỏ trống');
                flg = false;
            } else if (!regexPhone.test(txtPhone)) {
                $('#lblPhone').html('Số điện thoại không hợp lệ');
                flg = false;
            } else {
                $('#lblPhone').html('');
            }

            // account validate
            var txtUserName = $('#txtUserName').val();
            if (txtUserName === '') {
                $('#lblUserName').html('Tên tài khoản không được bỏ trống');
                flg = false;
            } else if (!regexUser.test(txtUserName)) {
                $('#lblUserName').html('Tên tài khoản không hợp lệ');
                flg = false;
            } else if (txtUserName.length < 5 || txtUserName.length > 30) {
                $('#lblUserName').html('Tên tài khoản ít nhất 5-30 ký tự');
                flg = false;
            } else {
                $('#lblUserName').html('');
            }

            // valid password
            var txtPassword = $('#txtPassword').val();
            if (txtPassword === "") {
                $('#lblPassword').html('Mật khẩu không được bỏ trống');
                $('#txtRePassword').val('');
                flg = false;
            } else if (txtPassword.length < 6 || txtPassword.length > 30) {
                $('#lblPassword').html('Mật khẩu ít nhất 6-30 ký tự');
                $('#txtRePassword').val('');
                flg = false;
            } else if (!regexPass.test(txtPassword)) {
                $('#lblPassword').html('Yêu cầu mật khẩu phức tạp hơn. VD: Abc123');
                $('#txtRePassword').val('');
                flg = false;
            } else {
                $('#lblPassword').html('');
            }

            // Re-password
            var txtRePassword = $('#txtRePassword').val();
            if (txtRePassword === "") {
                $('#lblRePassword').html("Vui lòng xác nhận mật khẩu");
                flg = false;
            } else if (txtRePassword !== txtPassword) {
                $('#lblRePassword').html('Xác nhận mật khẩu không đúng');
                flg = false;
            } else {
                $('#lblRePassword').html('');
            }

            if (flg) {
                userController.Create();
            } else {
                swal("Thêm tài khoản mới", "Dữ liệu không hợp lệ", "error");
            }
        });
    }
}
loginController.init();

$(document).on("keyup", "#txtFullName", function () {
    var txtFullName = $(this).val();
    if (txtFullName === '') {
        $('#lblFullName').html('Họ tên không được bỏ trống');
    } else {
        $('#lblFullName').html('');
    }
});

$(document).on("keyup", "#txtAddress", function () {
    var txtAddress = $(this).val();
    if (txtAddress === "") {
        $('#lblAddress').html('Địa chỉ không được bỏ trống');
    } else {
        $('#lblAddress').html('');
    }
});

$(document).on("keyup", "#txtEmail", function () {
    var txtEmail = $(this).val();
    if (txtEmail === "") {
        $('#lblEmail').html('Email không được bỏ trống');
    } else {
        if (!regexEmail.test(txtEmail)) {
            $('#lblEmail').html('Email không hợp lệ');
        } else {
            $('#lblEmail').html('');
        }
    }
});

$(document).on("keyup", "#txtPhone", function () {
    var txtPhone = $(this).val();
    if (txtPhone === "") {
        $('#lblPhone').html('Số điện thoại không được bỏ trống');
    } else if (!regexPhone.test(txtPhone)) {
        $('#lblPhone').html('Số điện thoại không hợp lệ');
    } else {
        $('#lblPhone').html('');
    }

});

$(document).on("keyup", "#txtUserName", function () {
    var txtUserName = $(this).val();
    if (txtUserName === '') {
        $('#lblUserName').html('Tên đăng nhập không được bỏ trống');
    } else if (!regexUser.test(txtUserName)) {
        $('#lblUserName').html('Tên tài khoản không hợp lệ');
    } else if (txtUserName.length < 5 || txtUserName.length > 30) {
        $('#lblUserName').html('Tên tài khoản ít nhất 5-30 ký tự');
    } else {

        $('#lblUserName').html('');
    }
});

$(document).on("keyup", "#txtPassword", function () {
    var txtPassword = $(this).val();
    if (txtPassword === "") {
        $('#lblPassword').html('Mật khẩu không được bỏ trống');
        $('#txtRePassID').val('');
        $('#lblRePassID').html("");

    } else if (txtPassword.length < 6 || txtPassword.length > 30) {
        $('#lblPassword').html('Mật khẩu ít nhất 6-30 ký tự');
        $('#txtRePassID').val('');
        $('#lblRePassID').html("");

    } else if (!regexPass.test(txtPassword)) {
        $('#lblPassword').html('Yêu cầu mật khẩu phức tạp hơn. VD: Abc123');
        $('#txtRePassID').val('');
        $('#lblRePassID').html("");

    } else {
        $('#lblPassword').html('');
    }
});

$(document).on("keyup", "#txtRePassword", function () {
    let txtRePassID = $(this).val();
    let txtPassword = $("#txtPassword").val();
    if (txtRePassword === "") {
        $('#lblRePassword').html("Yêu cầu xác nhận mật khẩu");
    } else if (txtRePassID !== txtPassword) {
        $('#lblRePassword').html('Xác nhận mật khẩu không đúng');
    } else {
        $('#lblRePassword').html('');
    }
});