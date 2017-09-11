$(document).ready(function () {
    $('.theory_course_content_blur_area').css('filter', 'blur(10px)');
    $('.theory_course_add').show();

    $('.theory_course_add_cross').click(function () {
        $('.theory_course_content_blur_area').css('filter', 'none');
        $('.theory_course_add').hide();
    });

    $('#theory_course_add_cancel').click(function () {
        $('.theory_course_content_blur_area').css('filter', 'none');
        $('.theory_course_add').hide();
    });

    $('#theory_course_add_submit').click(function () {
        $('#location_year_post').val($('#location_year').val());
        $('#location_semester_post').val($('#location_semester').val());

        var form = $('#theory_course_add_form');
        form.ajaxSubmit({
            target: '.content_right',
            error: function () {
                alert('error');
            }
        });
    });


});