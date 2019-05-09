(function ($) {
    "use strict";

    /*==================================================================
    [ Focus input ]*/
    // $('.input100').blur(function () {
    //     $(this).addClass('has-val');
    //     $(this).change(function () {
    //         if ($(this).val().trim() == "") {
    //             $(this).removeClass('has-val');
    //         }
    //     })
    // });

    /*==================================================================
    [ Show pass ]*/
    var showPass = 0;
    $('.btn-show-pass').on('click', function () {
        if (showPass == 0) {
            $(this).parents('#box-password').find('.input100').attr('type', 'text');
            $(this).find('i').removeClass('zmdi-eye-off');
            $(this).find('i').addClass('zmdi-eye');
            showPass = 1;
        } else {
            $(this).parents('#box-password').find('.input100').attr('type', 'password');
            $(this).find('i').addClass('zmdi-eye-off');
            $(this).find('i').removeClass('zmdi-eye');
            showPass = 0;
        }

    });

    // $('.input100').focusin(function () {
    //     $(this).addClass('has-val');
    //     var a = $(this);
    //     $('.datepicker-container').click(function () {
    //         alert("ok");
    //         $('.reg').click(function () {
    //             alert("ok");
    //             if (a.val().trim() == "") {
    //                 alert("EEE")
    //             }
    //         })
    //     })
    // })



})(jQuery);