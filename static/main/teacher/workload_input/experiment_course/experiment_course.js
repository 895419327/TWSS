$(document).ready(function () {
    
    $('tr:even').addClass('even');

    $('.experiment_course_add_button').click(function () {
        MyAjax_Get('getpage', 'workload_input_experiment_course_add', null, '.experiment_course_add_content')
    });

    $('.experiment_course_modify').click(function () {
        var id = this.id;
        id = id.substring(0, id.length - 7);
        MyAjax_Get('getpage', 'workload_input_experiment_course_modify', id, '.experiment_course_add_content');
    });

    $('.experiment_course_delete').click(function () {
        var id = this.id;
        id = id.substring(0, id.length - 7);
        if (confirm("确认删除？"))
            MyAjax('/upload', 'experiment_course_delete', id);
    });
});