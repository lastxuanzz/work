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




