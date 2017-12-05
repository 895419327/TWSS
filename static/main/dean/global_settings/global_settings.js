$(document).ready(function () {

    var submit_button = $('#global_settings_form_submit');

    var year_text = $('#year');
    var semester_text = $('#semester');

    $('#year_pre').click(function () {
        var year = year_text.text();
        year = year.substring(0,4);
        year = parseInt(year);
        var new_text = (year-1) + '-' + year + '学年';
        year_text.text(new_text);
        submit_button.show();
    });

    $('#year_next').click(function () {
        var year = year_text.text();
        year = year.substring(0,4);
        year = parseInt(year);
        var new_text = (year+1) + '-' + (year+2) + '学年';
        year_text.text(new_text);
        submit_button.show();
    });

    $('.semester_change').click(function () {
        var semester = semester_text.text();
        if(semester === '第一学期')
            semester_text.text('第二学期');
        else if (semester === '第二学期')
            semester_text.text('第一学期');
        submit_button.show();
    });

    submit_button.click(function () {
        $('#year_upload').attr('value', year_text.text());
        $('#semester_upload').attr('value', semester_text.text());

        $('#global_settings_form').ajaxSubmit({
            target: '.content_right',
                success: function () {
                    alert('设置成功！');
                },
                error: function () {
                    alert('error!')
                }
        });
    });
});