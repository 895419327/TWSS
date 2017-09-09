$(document).ready(function () {
    $('.teaching_project_content_blur_area').css('filter', 'blur(10px)');
    $('.teaching_project_add').show();

    $('.teaching_project_add_cross').click(function () {
        $('.teaching_project_content_blur_area').css('filter', 'none');
        $('.teaching_project_add').hide();
    });

    $('#teaching_project_add_cancel').click(function () {
        $('.teaching_project_content_blur_area').css('filter', 'none');
        $('.teaching_project_add').hide();
    });

    $('#teaching_project_add_submit').click(function () {
        var form = $('#teaching_project_add_form');
        form.ajaxSubmit({
            target: '.content_right',
            error: function () {
                alert('error');
            }
        });
    });


});