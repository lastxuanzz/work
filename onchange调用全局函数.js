//新建onload函数，在onLoad中定义全局函数

function onLoad() {
	// top.handleFieldChange 相当于 window.handleFieldChange
	// 而servicenow中不让用window.xxx，所以用top.xxx
	
	// 定义前确保该全局函数没有被定义
	if (typeof top.handleFieldChange === 'undefined') {
		// 定义全局函数handleFieldChange
		top.handleFieldChange = function() {
			// 获取所有字段值
			var test1 = g_form.getValue("test1");
			var test2 = g_form.getValue("test2");
			var test3 = g_form.getValue("test3");

			// 检查所有字段是否都有值
			if (!test1 || !test2 || !test3) {
				return;
			}
			alert("test2");

		};
	}else{
		alert("定义失败")
	}


}

// 在onChange中 引用全局函数 handleFieldChange
// 这样就可以在多个onChange中，使用同种方法了。 避免了onChange中代码冗余的问题
function onChange(control, oldValue, newValue, isLoading) {
    if (isLoading) {
        return;
    }
    }
    // 调用全局函数
    handleFieldChange();

}

/*
	使用场景：
		页面有5个文本框，当5个文本框都有值时，我才进行ajax调用， 查询数据库中的值
		保证每个文本框都有onChange方法，并获取页面中的值，传给ajax
*/