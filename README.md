### 1.设置某个字段值唯一
```javascript
(function executeRule(current, previous /*null when async*/ ) {
    // current和previous都是一个GlideRecord对象，当前和过去
    // 获取当前的system_code值
    var syscode = current.getValue('system_code');
    // 实例化表对象，x_1359700_apply_system是表名
    var gr = new GlideRecord('x_1359700_apply_system');
    // 添加查询的filter
    gr.addQuery('system_code', syscode);
    // 查询
    gr.query();
    // 判断是否为空
    if (gr.hasNext()) {
        gs.addErrorMessage('system code重复:' + syscode);
        // 阻止本次更新（前提是：此Business Rule的when条件选before）
        current.setAbortAction(true);
    }
})(current, previous);
```
