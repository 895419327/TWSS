$(document).ready(function () {
    $('#change_password_button').click(function () {
        var form = $('#change_password_form');

        var original_password = $('#change_password_original_password');

        // 未输入原密码
        if (original_password.val() === '') {
            alert('请输入原密码');
            return;
        }

        var new_password = $('#change_password_new_password');
        var new_password_check = $('#change_password_new_password_check');

        if (new_password.val().length < 8) {
            alert('新密码过短,请至少设置8位以上的密码');
            return;
        }

        if (new_password.val() !== new_password_check.val()) {
            alert('两次输入的新密码不一致');
            MyAjax_Get('/getpage', 'user_info_change_password');
            return;
        }

        original_password.val(original_password.val() + 'zhengzhoudaxueshengmingkexuexueyuanjiaoshigongzuoliangtongjixitong');
        original_password.val(hex_md5(original_password.val()));
        new_password.val(new_password.val() + 'zhengzhoudaxueshengmingkexuexueyuanjiaoshigongzuoliangtongjixitong');
        new_password.val(hex_md5(new_password.val()));

        form.ajaxSubmit({
            target: '.content_right',
            success: function (data) {
                if (data.indexOf('class="unsafe"') > 0)
                    alert('修改失败');
                else if (data.indexOf('class="original_password_error') > 0)
                    alert('原密码错误!');
                else
                    alert('修改成功!')
            },
            error: function () {
                alert('error');
            }
        });
    });
});