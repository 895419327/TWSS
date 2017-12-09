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

    $('#add_classes_select').change(function () {
        var grade = $('#add_classes_select option:selected').val().substring(0, 4);
        var id = $('#id').val();
        var data = grade + ',PraticeCourse,' + id;
        MyAjax_Get('/getpage', 'get_classes_module', data, '.add_classes');
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

        var isChooseClass = false;
        $('.class_checkbox').each(function () {
            if ($(this).is(':checked'))
                isChooseClass = true;
        });
        if(!isChooseClass) {
            alert('请选择班级');
            return;
        }

        if (isFull) {
            $('#location_year_post').val($('#location_year').val());
            $('#location_semester_post').val($('#location_semester').val());

            var form = $('#pratice_course_add_form');
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