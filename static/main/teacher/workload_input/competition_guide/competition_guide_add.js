$(document).ready(function () {
    $('.competition_guide_content_blur_area').css('filter', 'blur(10px)');
    $('.competition_guide_add').show();

    $('.competition_guide_add_cross').click(function () {
        $('.competition_guide_content_blur_area').css('filter', 'none');
        $('.competition_guide_add').hide();
    });

    $('#competition_guide_add_cancel').click(function () {
        $('.competition_guide_content_blur_area').css('filter', 'none');
        $('.competition_guide_add').hide();
    });

    $('#competition_guide_add_submit').click(function () {
        $('#location_year_post').val($('#location_year').val());
        $('#location_semester_post').val($('#location_semester').val());

        var form = $('#competition_guide_add_form');
        form.ajaxSubmit({
            target: '.content_right',
            error: function () {
                alert('error');
            }
        });
    });


});