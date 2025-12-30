## table
通知表：sys_notification<br>
content表：sn_ex_sp_notifs_portal_notification_content_config

## 配置
### sys_notification
1. Category选 Service Catalog
2. When to send<br>
Trigger:Record Change, Updated, Stage change to xxx(Flow中设置，将stage变为error, 更改sc_req_item字段comments)
3. Who will receive<br>
Recipients listed in fields:Opened by
4. 设置Contents<br>
Portals:Employee Center<br>
Content template: item的flow发生error。item：{0}<br>
Content params: ${number}<br>
Action url: /esc?id=ticket&table=sc_req_item&sys_id=${sys_id}&view=sp
