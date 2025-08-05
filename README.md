## 创建schedule（日历）
1. 在cmn_schedule中创建Schedule记录
2. 创建Schedule entry fields记录 工作日和节假日<br>
https://www.servicenow.com/docs/bundle/yokohama-platform-administration/page/administer/time/reference/r_ScheduleEntryFields.html
3. 使用下方script可以判断是否为工作日了
```javascript
var glide = new GlideRecord('cmn_schedule');
glide.addQuery('type', 'work_days');
glide.query();
if (glide.next()) {
   var sched = new GlideSchedule(glide.sys_id);
   var date = new GlideDateTime();
   date.setDisplayValue("2025-08-08 12:00:00");
   if (sched.isInSchedule(date)) 
      gs.info("Is in the schedule");
   else
      gs.info("Is NOT in the schedule");
}
```
