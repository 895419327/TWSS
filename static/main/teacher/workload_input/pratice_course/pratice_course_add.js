$(document).ready(function () {
    $('.pratice_course_content_blur_area').css('filter', 'blur(10px)');
    $('.pratice_course_add').show();

    $('.pratice_course_add_cross').click(function () {
        $('.pratice_course_content_blur_area').css('filter', 'none');
        $('.pratice_course_add').hide();
    });

    $('#pratice_course_add_cancel').click(function () {
        $('.pratice_course_content_blur_area').css('filter', 'none');
        $('.pratice_course_add').hide();
    });

    $('#pratice_course_add_submit').click(function () {
        var form = $('#pratice_course_add_form');
        form.ajaxSubmit({
            target: '.content_right',
            error: function () {
                alert('error');
            }
        });
    });


});