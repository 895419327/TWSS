$(document).ready(function () {
    $('.paper_guide_content_blur_area').css('filter', 'blur(10px)');
    $('.paper_guide_add').show();

    $('.paper_guide_add_cross').click(function () {
        $('.paper_guide_content_blur_area').css('filter', 'none');
        $('.paper_guide_add').hide();
    });

    $('#paper_guide_add_cancel').click(function () {
        $('.paper_guide_content_blur_area').css('filter', 'none');
        $('.paper_guide_add').hide();
    });

    $('#paper_guide_add_submit').click(function () {
        var form = $('#paper_guide_add_form');
        form.ajaxSubmit({
            target: '.content_right',
            error: function () {
                alert('error');
            }
        });
    });


});