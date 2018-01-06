$(document).ready(function () {

    $('tr:even').addClass('even');

    $('#database_dump_button').click(function () {
        $('#database_dump_form').submit();

        setTimeout(function () {
            MyAjax_Get('/getpage', 'database_management');
        }, 1500);
    });

    $('#database_auto_backup_setting').change(function () {
        $('#changed_mark').show();
    });

    $('.database_download_button').click(function () {
        var id = $(this).attr('id');
        id = id.substring(0, id.length - 9);
        $('#backup_id').val(id);
        $('#backup_operation_form_requestfor').val('backup_download');
        $('#backup_operation_form').submit();
    });

    $('.database_delete_button').click(function () {
        var id = $(this).attr('id');
        id = id.substring(0, id.length - 7);
        if(confirm('确定删除此备份吗？'))
            MyAjax_Get('/database', 'backup_delete', id);
    });
});