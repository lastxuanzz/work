## 在Catalog Item中设置全局属性方法

### 方法1
1. 创建一个onLoad方法
```javascript
function onLoad() {
    // 在新建top的属性xxx前，还应检查top.xxx的类型是否为undefined
    // servicenow中吐过有这个全局属性，就会被覆盖了，影响到了servicenow原来的功能
    if (typeof top.top的属性1 === 'undefined') {
        top.top的属性1 = 'xxxxxxxxx';
    }
}
```
2. 在其他方法中引用
```javascript
function onChange(control, oldValue, newValue, isLoading) {
    if (isLoading) {
        return;
    }
    alert(top的属性1);
}
```

### 方法2
1. 创建一个onLoad方法
```javascript
function onLoad() {
    // 注意： 这个 test用属性 不能用var声明，如果用var声明之后，他就成了onLoad中的局部变量啦。
    // 也应事前检查test用属性的类型是否为undefined
    test用属性 = 'xxxxxxxxxxxxx';
}
```
2. 在其他方法中引用
```javascript
function onChange(control, oldValue, newValue, isLoading) {
    if (isLoading) {
        return;
    }
    alert(test用属性);
}
```

## 在Catalog Item中设置全局属性的缺点
- 用户在浏览器的控制台中，可以直接修改这个全局变量，会导致原有的数据失效。

***

## 获取旧数据的方法（不使用全局变量）

**场景：**<br>
有一个下拉框select1，select1中的可选值为：空, a, b, c...<br>
现在我想将选取值的历史记录放在一个数组中，以便于我可以获取上一次选取的值（因为onChange中的oldValue是onLoad时的值）<br>

1. 创建一个text类型的var_text，并将其设置为readOnly和Hidden，默认值设置为`[]`， 注意：这个`[]`在text的变量中是一个字符串`'[]'`
2. 创建一个select类型的var_select，可选值设置为空, a, b, c...
3. 为var_select创建一个onChange方法
```javascript
function onChange(control, oldValue, newValue, isLoading) {
    if (isLoading) {
        return;
    }
    // 获取var_text的数据，即字符串： '[xx, xx, xx]'
    arr = g_form.getValue('var_text');
    // 将字符串转成数组 '[xx, xx, xx]' 👉 [xx, xx, xx]
    arr = JSON.parse(arr);
    // push新元素 [xx, xx, xx] 👉 [xx, xx, xx, XXX]
    arr.push(newValue);
    // 数组转成字符串 [xx, xx, xx, XXX] 👉 '[xx, xx, xx, XXX]'
    arr = JSON.stringify(arr);
    // 将字符串赋值为var_text
    g_form.setValue('var_text', arr);
}
```
4. 这样，var_text中存放的就是var_select的选择历史记录啦

***

### 附全局变量的使用例子

```javascript
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
```
