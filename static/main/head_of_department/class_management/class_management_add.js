$(document).ready(function () {
    $('.class_management_content_blur_area').css('filter', 'blur(10px)');
    $('.class_management_add').show();

    $('.class_management_add_cross').click(function () {
        $('.class_management_content_blur_area').css('filter', 'none');
        $('.class_management_add').hide();
    });

    $('#class_management_add_cancel').click(function () {
        $('.class_management_content_blur_area').css('filter', 'none');
        $('.class_management_add').hide();
    });

    $('#class_management_add_submit').click(function () {
        var form = $('#class_management_add_form');
        form.ajaxSubmit({
            target: '.content_right',
            error: function () {
                alert('error');
            }
        });
    });


});