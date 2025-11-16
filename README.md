## 查表中的值
html:
```html
<div>
  <!-- your widget template -->
  <button type="button"
          class="btn btn-primary"
          ng-click="onButtonClick()">
    <span>参照</span>
  </button>
</div>
```

client:
```javascript
api.controller = function ($scope) {
	/* widget controller */
	var c = this;
	var g_form = $scope.page.g_form;

	var aws_info_arr = [
		'vpc',
		'public_subnet',
		'private_subnet',
		'security_group',
		'ec2',
		'subnet'
	];

	$scope.onButtonClick = function () {
		var system_code = g_form.getValue('system_code');
		var env = g_form.getValue('env');
		if (!system_code || !env) {
			g_form.addInfoMessage('syscode和env不能为空');
			return;
		}

		var aws_info = {
			system_code: system_code,
			env: env
		};

		c.server.get({
			action: 'get_aws_rescore',
			aws_info: aws_info
		}).then(function (res) {
			if (res && res.data.awsInfoObj) {
				if(res.data.getAWSResourceFlag){
					setValueInItem(res.data.awsInfoObj);
				}else{
					g_form.addErrorMessage('获取AWS资源配置失败: ' + res.data.message);
				}
			} else {
				g_form.addErrorMessage('服务器返回数据异常');
			}
		}).catch(function (err) {
			g_form.addErrorMessage('获取AWS资源配置失败: ' + err.message);
		})

		function setValueInItem(arr) {
			aws_info_arr.forEach(function(item){
				g_form.setValue(item, arr[item]);
			})
		}

	};
};
```

server:
```javascript
(function () {
	if (input && input.action === 'get_aws_rescore') {
		try {
			var gr = new GlideRecord('x_1360191_test_app_system');
			gr.addQuery('system_code', input.aws_info.system_code);
			gr.addQuery('env', input.aws_info.env);
			gr.query();
			var awsInfoObj = {
				vpc: '',
				public_subnet: '',
				private_subnet: '',
				security_group: '',
				ec2: '',
				subnet: ''
			};
			if (gr.next()) {
				awsInfoObj.vpc = gr.getValue('vpc') || '';
				awsInfoObj.public_subnet = gr.getValue('public_subnet') || '';
				awsInfoObj.private_subnet = gr.getValue('private_subnet') || '';
				awsInfoObj.security_group = gr.getValue('security_group') || '';
				awsInfoObj.ec2 = gr.getValue('ec2') || '';
				var subnet_arr = [{
					"public_subnet_1": gr.getValue('public_subnet') || '',
					"private_subnet_1": gr.getValue('private_subnet') || ''
				}];
				awsInfoObj.subnet = JSON.stringify(subnet_arr);
			}
			data.getAWSResourceFlag = true;
			data.awsInfoObj = awsInfoObj;
		} catch (err) {
			data.getAWSResourceFlag = false;
			data.message = err.message;
		}

	}
})();
```

## API
html:
```html
<div>
<!-- your widget template -->
  <button type="button"
          class="btn btn-primary"
          ng-click="onButtonClick()">
    <span>api Request</span>
  </button>
</div>
```

client:
```javascript
api.controller=function($scope) {
  /* widget controller */
  var c = this;
	var ipAddress = '8.8.8.8';
	$scope.onButtonClick = function () {
		c.server.get({
			action: 'checkIp',
			ip: ipAddress
		}).then(function(res){
			console.log('IP信息查询成功:', res.data.city);
		})
		
	}
};
```

server:
```javascript
(function() {
	if(input && input.action === 'checkIp'){
		try{
			var request  = new sn_ws.RESTMessageV2();        
			request.setHttpMethod('get');

			//endpoint - ServiceNow REST Attachment API        
			request.setEndpoint('https://ipinfo.io/' + input.ip + '/json');        
			var response = request.execute();    
			var httpResponseStatus = response.getStatusCode();  
			var responseBody = response.getBody();
			if (httpResponseStatus === 200) {
				var ipInfo = JSON.parse(responseBody);
				data.city = ipInfo.country;
			}
		}
		catch(ex){
			var message  = ex.getMessage();        
			gs.info(message);    
		}
	}

})();


/*
POST:
var r = new sn_ws.RESTMessageV2();
r.setEndpoint("https://abc.com"); 
r.setRequestHeader("Accept", "application/json");
r.setRequestHeader("Content-Type", "application/x-www-form-urlencoded"); ******important*****
r.setRequestBody(body);
r.setHttpMethod('POST');
var response = r.execute();
var responseBody = response.getBody();
var httpStatus = response.getStatusCode();
*/
```
