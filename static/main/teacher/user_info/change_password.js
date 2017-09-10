$(document).ready(function () {
    $('#theory_course_add_submit').click(function () {
        var form = $('#theory_course_add_form');
        form.ajaxSubmit({
            target: '.content_right',
            error: function () {
                alert('error');
            }
        });
    });
});