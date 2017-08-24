$(document).ready(function () {

    $('#workload_input_theory_course').click(function () {
        $('.main_interface').hide();
        $('.theory_course_content').show();
    });

    $('.theory_course_add_button').click(function () {
        $('.theory_course_content_blur_area').css('filter', 'blur(10px)');
        $('.theory_course_add').show();
    });

    $('.theory_course_add_cross').click(function () {
        $('.theory_course_content_blur_area').css('filter', 'none');
        $('.theory_course_add').hide();
    });

    $('#theory_course_add_cancel').click(function () {
        $('.theory_course_content_blur_area').css('filter', 'none');
        $('.theory_course_add').hide();
    });


    $('#theory_course_add_submit').click(function () {
        // 将数据储存为json字符串
        var form = $('.theory_course_add_form_data');
        var datas_jsonstr = '{';
        form.each(function () {
            var title = $(this).attr('title');
            var data = $(this).val();
            datas_jsonstr += '"' + title + '": "' + data + '",';
        });
        datas_jsonstr = datas_jsonstr.substring(0, datas_jsonstr.length - 1);
        datas_jsonstr += '}';

        MyAjax('/upload','theory_course_add',datas_jsonstr);

        // form.each(function () {
        //     $(this).val('');
        // })
    });

    $('.theory_course_modify').click(function () {

    });

    $('.theory_course_delete').click(function () {
        var id = this.id;
        id = id.substring(0, id.length-7);

        MyAjax('/upload', 'theory_course_delete', id);
    });


    //test
    $('#test').click(function () {
        var form = $('#request_form');
        var requestfor = $('#requestfor');
        var requestdata = $('#request_data');

        // 配置目标url
        form.attr('action', '/upload');
        // 配置请求
        requestfor.val('page');
        // 附上数据
        requestdata.val('');

        // 提交
        form.ajaxSubmit({
            target: '.theory_course_content',
            error: function () {
                alert('未知错误');
            }
        });

        // 提交后重置目标url及请求
        form.attr('action', '');
        requestfor.val('');
        requestdata.val('');
    });
});