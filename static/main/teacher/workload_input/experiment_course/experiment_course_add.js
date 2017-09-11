$(document).ready(function () {
    $('.experiment_course_content_blur_area').css('filter', 'blur(10px)');
    $('.experiment_course_add').show();

    $('.experiment_course_add_cross').click(function () {
        $('.experiment_course_content_blur_area').css('filter', 'none');
        $('.experiment_course_add').hide();
    });

    $('#experiment_course_add_cancel').click(function () {
        $('.experiment_course_content_blur_area').css('filter', 'none');
        $('.experiment_course_add').hide();
    });

    $('#experiment_course_add_submit').click(function () {
        $('#location_year_post').val($('#location_year').val());
        $('#location_semester_post').val($('#location_semester').val());

        var form = $('#experiment_course_add_form');
        form.ajaxSubmit({
            target: '.content_right',
            error: function () {
                alert('error');
            }
        });
    });


});