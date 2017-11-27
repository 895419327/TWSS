$(document).ready(function () {
    $('.blur_area').css('filter', 'blur(10px)');

    $('.add_cross').click(function () {
        $('.blur_area').css('filter', 'none');
        $('.add_popup').hide();
    });

    $('.add_cancel').click(function () {
        $('.blur_area').css('filter', 'none');
        $('.add_popup').hide();
    });

     $('#project_type').change(function () {
        var type = $(this).val();
        var level_select = $('#project_level');
        switch (type) {
            case '工程实践教育类':
                level_select.html(
                    "<option>国家级</option>"
                ); break;
            default:
                level_select.html(
                    "<option>国家级</option>" +
                    "<option>省部级</option>" +
                    "<option>校级</option>"
                ); break;

        }
    });

    $('.add_submit').click(function () {

        var isFull = true;
        var empty_item = null;
        $('.non_empty').each(function () {
            if ($(this).val() == '') {
                isFull = false;
                empty_item = $(this);
            }
        });

        if (isFull) {
            $('#location_year_post').val($('#location_year').val());

            var form = $('#teaching_project_add_form');
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