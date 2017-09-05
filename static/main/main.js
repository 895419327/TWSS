$(document).ready(function () {

    // 退出按钮动画
    // $('#logout').click(function () {
    //     var body = $('body');
    //     body.css('filter','blur(5px)');
    //     setTimeout(function () {
    //         var confirm_logout = confirm('确定退出吗?');
    //         if(confirm_logout == true){
    //             window.close();
    //         }
    //         else {
    //             body.css('filter','none');
    //         }
    //     },100);
    //
    // });

    // 禁用左侧菜单的双击选择文字，影响使用体验
    $('.left_unit').addClass('no_select');
    // 禁用全局按钮的双击选择文字
    $('.content_button').addClass('no_select');


    //左侧菜单动画
    $('.unit_title').click(function () {
        // 点击标题后 隐藏其他模块的子菜单 显示本模块的子菜单
        // $('.unit_options').slideUp('fast');
        // if($(this).next().css('display') === 'none'){
        //     $(this).next().slideDown('fast');
        // }

        // 点击标题后 显示本模块子菜单但不隐藏其他模块的
        $(this).next().slideToggle('fast');
    });

    $('#user_info_user_info').click(function () {
        MyAjax_Get('/getpage', 'user_info', '');
    });

    $('#user_info_change_password').click(function () {
        MyAjax_Get('/getpage', 'change_password', '');
    });

    $('#workload_input_theory_course').click(function () {
        MyAjax_Get('/getpage', 'theory_course', '');
    });

    $('#workload_input_pratice_course').click(function () {
        MyAjax_Get('/getpage', 'pratice_course', '');
    });

    $('#workload_input_teaching_achievement').click(function () {
        MyAjax_Get('/getpage', 'teaching_achievement', '');
    });

    $('#workload_input_teaching_project').click(function () {
        MyAjax_Get('/getpage', 'teaching_project', '');
    });

    $('#workload_input_competition_guide').click(function () {
        MyAjax_Get('/getpage', 'competition_guide', '');
    });

    $('#workload_input_paper_guide').click(function () {
        MyAjax_Get('/getpage', 'paper_guide', '');
    });

    $('#workload_count_title').click(function () {
        MyAjax_Get('/getpage', 'workload_count', '');
    });
});

function MyAjax(action, forwhat, data) {
    var form = $('#request_form');
    var requestfor = $('#requestfor');
    var requestdata = $('#request_data');

    // 配置目标url
    form.attr('action', action);
    // 配置请求
    requestfor.val(forwhat);
    // 附上数据
    requestdata.val(data);

    // 提交
    form.ajaxSubmit({
        target: '.content_right',
        error: function () {
            alert('未知错误');
        }
    });

    // 提交后重置目标url及请求
    form.attr('action', '');
    requestfor.val('');
    requestdata.val('');
}

function MyAjax_Get(action, forwhat, data, towhere) {
    var form = $('#request_form');
    var requestfor = $('#requestfor');
    var requestdata = $('#request_data');

    // 配置目标url
    form.attr('action', action);
    // 配置请求
    requestfor.val(forwhat);
    // 附上数据
    requestdata.val(data);

    var towhere = arguments[3]?arguments[3]:'.content_right';
    // 提交
    form.ajaxSubmit({
        target: towhere,
        error: function () {
            alert('未知错误');
        }
    });

    // 提交后重置目标url及请求
    form.attr('action', '');
    requestfor.val('');
    requestdata.val('');
}