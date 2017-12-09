$(document).ready(function () {
    $('tr:even').addClass('even');

    $('.audit_reject').hover(
        function () {
            $(this).children().show();
        },
        function () {
            $(this).children().hide();
        }
    );

    $('.add_button').click(function () {
        var location = $('#location_year').val() + ',' + $('#location_semester').val();
        MyAjax_Get('getpage', 'workload_input_paper_guide_add', null, '.paper_guide_add_content', location)
    });

    $('.paper_guide_modify').click(function () {
        var id = this.id;
        id = id.substring(0, id.length - 7);
        MyAjax_Get('getpage', 'workload_input_paper_guide_add', id, '.paper_guide_add_content');
    });

    $('.paper_guide_delete').click(function () {
        var id = this.id;
        id = id.substring(0, id.length - 7);
        var location = $('#location_year').val() + ',' + $('#location_semester').val();
        if (confirm("确认删除？"))
            MyAjax_Get('/upload', 'paper_guide_delete', id, null, location);
    });

    $('.search_button').click(function () {
        $('#paper_guide_search_form').ajaxSubmit({
            target: '.content_right',
            error: function () {
                alert('连接服务器失败');
            }
        })
    });
});