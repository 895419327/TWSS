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
        var data = grade + ',TheoryCourse,' + id;
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



        if (isFull) {
            $('#location_year_post').val($('#location_year').val());
            $('#location_semester_post').val($('#location_semester').val());

            var form = $('#theory_course_add_form');
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