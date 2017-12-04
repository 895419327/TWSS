$(document).ready(function () {

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
        $('.main_content').prepend('<div class="loading">正在加载...</div>');
        MyAjax_Get('/getpage', $(this).attr('id'));
    });

    // 特殊情况下无二级菜单 则点击一级菜单时返回相应页面
    // TODO: 将属于各个身份的功能函数写入相应的身份html里 不要放在公用的main.js里
    // TODO: 服务器需检查权限 防止未登录直接发送表单得到数据
    // Teacher
    $('#workload_count_title').click(function () {
        $('.main_content').prepend('<div class="loading">正在加载...</div>');
        MyAjax_Get('/getpage', 'teacher_workload_count');
    });

    // Head of Department
    $('#teacher_management_title').click(function () {
        $('.main_content').prepend('<div class="loading">正在加载...</div>');
        MyAjax_Get('/getpage', 'teacher_management');
    });

    $('#workload_statistics_title').click(function () {
        $('.main_content').prepend('<div class="loading">正在加载...</div>');
        MyAjax_Get('/getpage', 'workload_statistics');
    });

    // Dean

    $('#global_settings_title').click(function () {
        $('.main_content').prepend('<div class="loading">正在加载...</div>');
        MyAjax_Get('/getpage', 'global_settings');
    });

    $('#class_management_title').click(function () {
        $('.main_content').prepend('<div class="loading">正在加载...</div>');
        MyAjax_Get('/getpage', 'class_management');
    });

    $('#department_management_title').click(function () {
        $('.main_content').prepend('<div class="loading">正在加载...</div>');
        MyAjax_Get('/getpage', 'department_management');
    });

    $('#workload_K_value_title').click(function () {
        $('.main_content').prepend('<div class="loading">正在加载...</div>');
        MyAjax_Get('/getpage', 'workload_K_value');
    });

    // Admin
    $('#database_management_title').click(function () {
        $('.main_content').prepend('<div class="loading">正在加载...</div>');
        MyAjax_Get('/getpage', 'database_management');
    });

    $('#data_import_title').click(function () {
        $('.main_content').prepend('<div class="loading">正在加载...</div>');
        MyAjax_Get('/getpage', 'data_import');
    });
});

function MyAjax_Get(url, forwhat, data, towhere, extra_data) {
    var form = $('#request_form');
    var requestfor = $('#requestfor');
    var requestdata = $('#request_data');
    var extradata = $('#extra_data');


    // 配置目标url
    form.attr('action', url);
    // 配置请求
    requestfor.val(forwhat);
    // 附上数据
    requestdata.val(data);
    var extra_data = arguments[4] ? arguments[4] : '';
    extradata.val(extra_data);

    var towhere = arguments[3] ? arguments[3] : '.content_right';
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
    extradata.val('');
}