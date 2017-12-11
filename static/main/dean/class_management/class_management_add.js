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

    $('.add_submit').click(function () {
        var isFull = true;
        var empty_item = null;
        $('.non_empty').each(function () {
            if ($(this).val() == '') {
                isFull = false;
                empty_item = $(this);
            }
        });

        // 规范班级id
        var class_id = $('#class_id').val();
        var grade = $('#grade').val();

        var check_class_id = class_id.substring(0, 4);
        var check_grade = grade.substring(0, 4);

        if (check_class_id !== check_grade) {
            alert('班级编号请以所在年级开头');
            $('#class_id').focus();
            return;
        }

        if (isFull) {
            var form = $('#class_management_add_form');
            form.ajaxSubmit({
                target: '.content_right',
                success: function (data) {
                    if (data.indexOf('class="unsafe"') > 0)
                        alert('修改失败');
                    else
                        alert('修改成功!')
                },
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