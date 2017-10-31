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
        var extra_data = $(this).attr('id');
        MyAjax_Get('getpage', 'workload_input_competition_guide_add', null, '.competition_guide_add_content', extra_data);
    });

    $('.competition_guide_modify').click(function () {
        var id = this.id;
        id = id.substring(0, id.length - 7);
        MyAjax_Get('getpage', 'workload_input_competition_guide_add', id, '.competition_guide_add_content');
    });

    $('.competition_guide_delete').click(function () {
        var id = this.id;
        id = id.substring(0, id.length - 7);
        var location = $('#location_year').val() + ',' + $('#location_semester').val();
        if (confirm("确认删除？"))
            MyAjax_Get('/upload', 'competition_guide_delete', id, null, location);
    });

    $('.search_button').click(function () {
        $('#competition_guide_search_form').ajaxSubmit({
            target: '.content_right',
            error: function () {
                alert('error!');
            }
        })
    });
});