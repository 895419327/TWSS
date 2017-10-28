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

    $('#add_classes_select').change(function () {
        var grade = $('#add_classes_select option:selected').val().substring(0, 4);
        var course_id = $('#course_id').val();
        var data = grade + ',TheoryCourse,' + course_id;
        MyAjax_Get('/getpage', 'get_classes_module', data, '.add_classes');
    });

    $('.add_submit').click(function () {
        $('#location_year_post').val($('#location_year').val());
        $('#location_semester_post').val($('#location_semester').val());

        var form = $('#theory_course_add_form');
        form.ajaxSubmit({
            target: '.content_right',
            error: function () {
                alert('error');
            }
        });
    });


});