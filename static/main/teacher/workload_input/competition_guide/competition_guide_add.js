$(document).ready(function () {

    toCenter();

    $('.blur_area').css('filter', 'blur(10px)');

    $('.add_cross').click(function () {
        $('.blur_area').css('filter', 'none');
        $('.add_popup').hide();
    });

    $('.add_cancel').click(function () {
        $('.blur_area').css('filter', 'none');
        $('.add_popup').hide();
    });

    $('.add_submit').click(function () {

        var isFull = true;
        var empty_item;
        $('.non_empty').each(function () {
            if ($(this).val() == '') {
                isFull = false;
                empty_item = $(this);
            }
        });

        if (isFull) {
            $('#location_year_post').val($('#location_year').val());

            var form = $('#competition_guide_add_form');
            form.ajaxSubmit({
                target: '.content_right',
                error: function () {
                    alert('error');
                }
            });
        } else {
            alert('请完整填写表单');
            empty_item.focus();
        }


    });


});