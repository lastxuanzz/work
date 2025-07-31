# Flow

## 1.Flow 的 Trigger：Service Catalog
将Trigger设置为Service Catalog的作用：<br>
- 只有将Trigger设置为Service Catalog，才能在catalog item的flow中，选择该flow<br>
- 添加Action：Ask For Approval（选择将请求发送给谁），作用是将申请发送到sysapproval_approver表中
- if分支中加上Approval的状态是否为Approved（上一步中，承认者是否承认），这个字段来源于sysapproval_approver表，而不是表sc_req_item

## 2.在Flow中自定义Action整型json
```JavaScript
(function execute(inputs, outputs) {
    // script的入力值是action的入力值，是一个reference类型，表request Item
    var sysid = inputs.parameter1.sys_id;
    // 取得本次的申请记录
    var grReq = new GlideRecord('sc_req_item');
    grReq.get(sysid)
    grReq.next();
    // 取得本次的申请记录中item
    var item_sysid = grReq.cat_item.toString();
    var grItem = new GlideRecord('sc_cat_item');
    grItem.get(item_sysid)
    grItem.next();
    // 获取item名
    var item_name = grItem.name.toString();
    // 获取申请id？
    var number = grReq.number.toString();
    allMsgs = ['msg1', 'msg2', 'msg3', 'msg4']
    var obj_msg = {};
    // 这里是msg判断是否为空，为空的text不记录在json中
    allMsgs.forEach(function(item_msg){
        if (grReq.variables[item_msg].toString()){
            obj_msg[item_msg] = grReq.variables[item_msg].toString();
        }
    })
    var obj = {};
    // 做成js对象
    obj["item_name"] = item_name;
    obj["number"] = number;
    // 用户入力的所有msg
    obj["vars"] = obj_msg;
    // 整型成json格式
    outputs.json_payload = JSON.stringify(obj);

})(inputs, outputs);


```
