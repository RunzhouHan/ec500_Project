(function(){
	document.getElementById('register_submit').addEventListener('click', addUsers);
	function $(tag, options) {
		if (!options) {
			return document.getElementById(tag);
		}

		var element = document.createElement(tag);

		for ( var option in options) {
			if (options.hasOwnProperty(option)) {
				element[option] = options[option];
			}
		}

		return element;
	}
	function ajax(method, url, data, callback, errorHandler) {
		  var xhr = new XMLHttpRequest();

		  xhr.open(method, url, true);

		  xhr.onload = function () {
		    switch (xhr.status) {
		      case 200:
		        callback(xhr.responseText);
		        break;
		      case 403:
		        onSessionInvalid();
		        break;
		      case 401:
		        errorHandler();
		        break;
		    }
		  };

		  xhr.onerror = function () {
		    console.error("The request couldn't be completed.");
		    errorHandler();
		  };

		  if (data === null) {
		    xhr.send();
		  } else {
		    xhr.setRequestHeader("Content-Type", "application/json;charset=utf-8");
		    xhr.send(data);
		  }
	}
	function addUsers() {
		var userid = document.getElementById('reg_userid').value;
		var first_name = document.getElementById('reg_firstname').value;
		var last_name = document.getElementById('reg_lastname').value;
		var password = document.getElementById('reg_password').value;
		var nation = document.getElementById('reg_nation').value;
		var age = document.getElementById('reg_age').value;
		var gender = document.getElementById('reg_gender').value;
		var url = './login';
		var params = 'user_id=' + userid + '&first_name=' + first_name + '&last_name=' + last_name + '&password='+password
		+'&nation='+nation + '&age=' + age + '&gender=' + gender;
		console.log(params);
		ajax('POST', url +'?'+params,'',
				// successful callback
				function(res) {
					alert(res);
				});
	}
})();