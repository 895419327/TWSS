$(document).ready(function () {
    var notice = $('.notice');
    notice.each(function () {
        var str = $(this).html();
        str = str.replace(/\n/g, '<br>');
        $(this).html(str);
    });

    $('#notice_edit_button').click(function () {
        var text = notice.html();
        text = text.replace(/<br>/g, '\n');
        notice.hide();
        $('#notice_editor').text(text);
        $('.notice_editor_area').show();
        $(this).text('保存');
        $(this).attr('id', 'notice_edit_save_button');

        $('#notice_edit_save_button').click(function () {
            $('#notice_edit_form').ajaxSubmit({
                target: '.content_right',
                success: function () {
                    alert('设置成功！');
                },
                error: function () {
                    alert('error!')
                }
            })
        });
    });


});