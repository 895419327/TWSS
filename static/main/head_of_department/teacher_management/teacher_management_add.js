$(document).ready(function () {
    $('.blur_area').css('filter', 'blur(10px)');

    $('.add_cross').click(function () {
        $('.blur_area').css('filter', 'none');
        $('.add_popup').hide();
    });

    $('.add_cancel').click(function () {
        $('.blur_area').css('filter', 'none');
        $('.add_popup').hide();
    });

    $('.reset_password_button').click(function () {
        var teacher_id = $('#original_teacher_id').val();
        var teacher_name = $('#teacher_name').val();

        if (confirm('确定重置 ' + teacher_name + '老师(' + teacher_id + ') 的密码吗？\n' +
                '(重置后的密码为教职工号)')) {
            $('#reset_teacher_id').val(teacher_id);
            $('#reset_password_form').ajaxSubmit({
                target: '.content_right',
                success: function (data) {
                    if (data.indexOf('class="unsafe"') > 0)
                        alert('修改失败!');
                    else
                        alert('修改成功！\n' +
                            '已将 ' + teacher_name + '老师' + '的密码重置为 ' + teacher_id +
                            '\n请及时通知' + teacher_name + '老师');
                },
                error: function () {
                    alert('连接服务器失败');
                }
            })
        }
    });

    $('.add_submit').click(function () {
        var isFull = true;
        var empty_item = null;
        $('.non_empty').each(function () {
            if ($(this).val() == '') {
                isFull = false;
                empty_item = $(this);
            }
        });

        if (isFull) {
            var form = $('#teacher_management_add_form');
            form.ajaxSubmit({
                target: '.content_right',
                error: function () {
                    alert('连接服务器失败');
                }
            });
        } else {
            alert('请完整填写表单');
            empty_item.focus();
        }
    });


});