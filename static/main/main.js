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
        // 点击标题后 显示本模块子菜单但不隐藏其他模块的
        $(this).next().slideToggle('fast');
    });

    // 一般情况下点击二级菜单返回相应页面
    $('.unit_detail').click(function () {
        MyAjax_Get('/getpage', $(this).attr('id'));
    });

    // 特殊情况下无二级菜单 则点击一级菜单时返回相应页面
    // TODO: 可优化
    // TODO: 服务器需检查权限 防止未登录直接发送表单得到数据
    // Teacher
    $('#workload_count_title').click(function () {
        MyAjax_Get('/getpage', 'workload_count');
    });

    // Head of Department
    $('#teacher_management_title').click(function () {
        MyAjax_Get('/getpage', 'teacher_management');
    });

    $('#class_management_title').click(function () {
        MyAjax_Get('/getpage', 'class_management');
    });

    $('#workload_statistics_title').click(function () {
        MyAjax_Get('/getpage', 'workload_statistics');
    });

    $('#department_management_title').click(function () {
        MyAjax_Get('/getpage', 'department_management');
    })


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