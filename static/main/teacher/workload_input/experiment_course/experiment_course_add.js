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
        var data = grade + ',ExperimentCourse,' + id;
        MyAjax_Get('/getpage', 'get_classes_module', data, '.add_classes');
    });

    $('.help_choose').focus(function () {
        $('.classes_checkboxs').hide();
        $('.courses_selector').show();
    });

    $('.help_choose').blur(function () {
        setTimeout(function () {
            $('.courses_selector').hide();
            $('.classes_checkboxs').show();
        }, 200);
    });

    $('.courses_selector_item').click(function () {
        var str = $(this).text();
        var splits = str.split(' ');
        $('#course_id').val( splits[0]);
        $('#course_name').val(splits[1]);
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

            var form = $('#experiment_course_add_form');
            form.ajaxSubmit({
                target: '.content_right',
                error: function () {
                    alert('error');
                }
            });
        } else {
            alert('请完整填写表单');
            empty_item.focus();
        }

    });


});