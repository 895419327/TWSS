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

        var rank_select_area = $('#project_rank_area');
        switch (type) {
            case '教研论文':
                rank_select_area.hide();
                level_select.html(
                    "<option>核心期刊</option>" +
                    "<option>一般期刊</option>"
                ); break;
            case '教改项目结项':
                rank_select_area.hide();
                level_select.html(
                    "<option>国家级</option>" +
                    "<option>省部级</option>" +
                    "<option>校级</option>"
                ); break;
            case '教学成果':
                rank_select_area.show();
                level_select.html(
                    "<option>国家级</option>" +
                    "<option>省部级</option>" +
                    "<option>校级</option>"
                ); break;
            case '教材':
                rank_select_area.hide();
                level_select.html(
                    "<option>全国统编教材、国家级规划教材、全国教学专业指导委员会指定教材、全国优秀教材</option>" +
                    "<option>其他正式出版教材</option>"
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

            var form = $('#teaching_achievement_add_form');
            form.ajaxSubmit({
                target: '.content_right',
                error: function () {
                    alert('连接服务器失败');
                }
            });
        } else {
            alert('请完整填写表单');
            empty_item.focus();
        }

    });


});