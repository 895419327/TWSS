$(document).ready(function () {
    $('#workload_input_pratice_course').click(function () {
        $('.main_interface').hide();
        $('.pratice_course_content').show();
    });

    $('.pratice_course_add_button').click(function () {
        $('.pratice_course_content_blur_area').css('filter','blur(10px)');
        $('.pratice_course_add').show();
    });

    $('.pratice_course_add_cross').click(function () {
        $('.pratice_course_content_blur_area').css('filter','none');
        $('.pratice_course_add').hide();
    });

    $('#pratice_course_add_cancel').click(function () {
        $('.pratice_course_content_blur_area').css('filter','none');
        $('.pratice_course_add').hide();
    });
});