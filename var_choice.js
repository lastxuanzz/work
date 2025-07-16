function onChange(control, oldValue, newValue, isLoading) {
    if (isLoading) {
        return;
    }

	// 定义全局数组
    if (typeof top.var1History === 'undefined') {
        top.var1History = [];
    }

	// 每次onchange，newValue都会存到数组中
	// 数组的倒数第二个元素就是onchange前的值
    var1History.push(newValue);

	var allOptions = {
		jcu: [
			{value: 'jcu1',label: 'jcu環境1'},
			{value: 'jcu2',label: 'jcu環境2'},
			{value: 'jcu3',label: 'jcu環境3'},
		],
		svk: [
			{value: 'svk1',label: 'svk環境1'},
			{value: 'svk2',label: 'svk環境2'},
			{value: 'svk3',label: 'svk環境3'},
			{value: 'svk3',label: 'svk環境3'},
		],
		ufa: [
			{value: 'ufa1',label: 'ufa環境1'},
			{value: 'ufa2',label: 'ufa環境2'},
		],
		acg: [
			{value: 'acg1',label: 'acg環境1'},
			{value: 'acg2',label: 'acg環境2'},
			{value: 'acg3',label: 'acg環境3'},
		],

	};

	// 数组长度为1，代表页面onLoad后，第一次onchange，无需对var2的值进行删除
	if (var1History.length == 1){
		allOptions[newValue].forEach(function(opt) {
			g_form.addOption('var2', opt.value, opt.label);
		});
	}

	// 数组长度大于1，代表页面onLoad后，第二次以及后续的onchange，需对var2的值进行删除
	if (var1History.length > 1) {
		// 获取onchange前的值
		var var1OldValue = var1History[var1History.length - 2];
		// 如果旧值不为空，则需删除var2中的值
		if (var1OldValue != ''){
			allOptions[var1OldValue].forEach(function(opt) {
				g_form.removeOption('var2', opt.value);
			});
		}
		// 如果新值不为空，则增加var2中的值
		if(newValue){
			allOptions[newValue].forEach(function(opt) {
				g_form.addOption('var2', opt.value, opt.label);
			});
		}
	}

	// 数组长度超过5后，删除第一个元素
	if (var1History.length > 5) {
		var1History.shift();
	}

}