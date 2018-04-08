(function(){
	document.getElementById('login_submit').addEventListener('click', loginUsers);
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
	function loginUsers() {
		var userid = document.getElementById('log_userid').value;
		var password = document.getElementById('log_password').value;
		var url = './register';
		var params = 'user_id=' + userid + '&password='+password;
		ajax('GET', url +'?'+params,'',
				// successful callback
				function(res) {
					if (res === "true"){
						var temp = "http://localhost:8080/Titan/?user_id=" + userid;
						console.log(temp);
						window.location= temp;
					} else {
						alert("Invalid account"); 
					}
				});
	}
	
})();
