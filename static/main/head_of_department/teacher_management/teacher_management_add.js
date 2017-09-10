$(document).ready(function () {
    $('.teacher_management_content_blur_area').css('filter', 'blur(10px)');
    $('.teacher_management_add').show();

    $('.teacher_management_add_cross').click(function () {
        $('.teacher_management_content_blur_area').css('filter', 'none');
        $('.teacher_management_add').hide();
    });

    $('#teacher_management_add_cancel').click(function () {
        $('.teacher_management_content_blur_area').css('filter', 'none');
        $('.teacher_management_add').hide();
    });

    $('#teacher_management_add_submit').click(function () {
        var form = $('#teacher_management_add_form');
        form.ajaxSubmit({
            target: '.content_right',
            error: function () {
                alert('error');
            }
        });
    });


});