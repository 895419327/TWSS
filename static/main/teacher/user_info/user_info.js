$(document).ready(function () {

    var modify_button = $('#user_info_modify');

    // 修改功能
    var modifying = false;

    modify_button.click(function () {
            // 判断修改状态
            // 未修改状态时为'修改'按钮
            if (!modifying) {
                modifying = true;
                modify_button.text('保存');
                modify_button.css('color', 'red');
                $('.single_line_item_can_modify').each(function () {
                    var data = $(this).text();
                    var name = $(this).attr('name');
                    var width = $(this).css('width');
                    $(this).html("<input class='single_line_item_modify_area' " + "value=" + data + " name=" + name + ">");

                    // 这里要手动设置width避免td自动调整宽度
                    // $(this).css('width', width);
                    $(this).children().css('width', width);
                });


                var department_selector = $('#user_info_department_selector');
                var departments = ["生物工程", "生物技术", "生物信息"];
                var current_department = department_selector.text();
                for (var d = 0; d < 3; d++) {
                    if (current_department === departments[d])
                        departments.splice(d, 1);
                }
                department_selector.html("<select name='department'>" +
                    "<option>" + current_department + "</option>" +
                    "<option>" + departments[0] + "</option>" +
                    "<option>" + departments[1] + "</option>" +
                    "</select>");

                var gender_selector = $('#user_info_gender_selector');
                var current_gender = gender_selector.text();

                switch (current_gender) {
                    case '未记录':
                    case '男':
                        gender_selector.html("<select name='gender'>" +
                            "<option>" + "男" + "</option>" +
                            "<option>" + "女" + "</option>" +
                            "</select>");
                        break;
                    case '女':
                        gender_selector.html("<select name='gender'>" +
                            "<option>" + "女" + "</option>" +
                            "<option>" + "男" + "</option>" +
                            "</select>");
                        break;
                }

                // 点击'修改'时模拟点击选择第一个可修改的文本框
                $('.single_line_item_modify_area:first').trigger('select');
                return;
            }

            // 修改状态时为'保存'按钮

            if (modifying) {
                modifying = false;
                modify_button.text('修改');
                modify_button.css('color', 'black');

                var form = $('#user_info_form');
                form.ajaxSubmit({
                    target: '.content_right',
                    success: function (data) {
                        if(data.indexOf('class="unsafe"') > 0)
                            alert('修改失败');
                        else
                            alert('修改成功!')
                    },
                    error: function () {
                        alert('连接服务器失败');
                    }
                });
            }
        }
    );
});