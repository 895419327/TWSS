$(document).ready(function () {
    $('#change_password_button').click(function () {
        var form = $('#change_password_form');

        var original_password =  $('#change_password_original_password');
        original_password.val(hex_md5(original_password.val()));

        var new_password =  $('#change_password_new_password');
        new_password.val(hex_md5(new_password.val()));

        form.ajaxSubmit({
            // target: '#message',
            success: function () {
                alert('修改成功！');
                $('.change_password_item input').val('');
            },
            error: function () {
                alert('原密码错误！');
                $('.change_password_item input').val('');
            }
        });
    });
});