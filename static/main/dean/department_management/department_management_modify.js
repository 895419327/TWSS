$(document).ready(function () {
    $('.department_management_content_blur_area').css('filter', 'blur(10px)');
    $('.department_management_add').show();

    $('.department_management_add_cross').click(function () {
        $('.department_management_content_blur_area').css('filter', 'none');
        $('.department_management_add').hide();
    });

    $('#department_management_add_cancel').click(function () {
        $('.department_management_content_blur_area').css('filter', 'none');
        $('.department_management_add').hide();
    });

    $('#department_management_add_submit').click(function () {
        var form = $('#department_management_add_form');
        form.ajaxSubmit({
            target: '.content_right',
            error: function () {
                alert('error');
            }
        });
    });


});