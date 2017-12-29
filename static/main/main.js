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

    // 点击二级菜单返回相应页面
    $('.unit_detail').click(function () {
        $('.main_content').prepend('<div class="loading">正在加载...</div>');
        MyAjax_Get('/getpage', $(this).attr('id'));
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
            alert('连接服务器失败');
        }
    });

    // 提交后重置目标url及请求
    form.attr('action', '');
    requestfor.val('');
    requestdata.val('');
    extradata.val('');
}

function toCenter() {
    var add_popup = $('.add_popup');
    var height = add_popup.css('height');
    height = height.replace('px', '');
    add_popup.css('margin-top', '-' + height / 2 + 'px');
}