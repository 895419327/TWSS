$(document).ready(function () {
    $('.teaching_achievement_content_blur_area').css('filter', 'blur(10px)');
    $('.teaching_achievement_add').show();

    $('.teaching_achievement_add_cross').click(function () {
        $('.teaching_achievement_content_blur_area').css('filter', 'none');
        $('.teaching_achievement_add').hide();
    });

    $('#teaching_achievement_add_cancel').click(function () {
        $('.teaching_achievement_content_blur_area').css('filter', 'none');
        $('.teaching_achievement_add').hide();
    });

    $('#teaching_achievement_add_submit').click(function () {
        $('#location_year_post').val($('#location_year').val());
        $('#location_semester_post').val($('#location_semester').val());

        var form = $('#teaching_achievement_add_form');
        form.ajaxSubmit({
            target: '.content_right',
            error: function () {
                alert('error');
            }
        });
    });


});