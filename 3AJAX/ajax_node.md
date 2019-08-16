# Day1....AJAX

配置环境：

```setting
#配置存储路径
STATICFILES_DIRS=[
    os.path.join(BASE_DIR,'static'),
]
```

```setting
DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ajax_DB',
        'HOST': '127.0.0.1',
        'PORT': 3306,
        'USER': 'root',
        'PASSWORD': '123456',

    }
}
```

```setting
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        ***'DIRS': [os.path.join(BASE_DIR,'templates'),],***
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

```setting
#注册APP
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    ***'ajax',***
]
```

```主路由
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^ajax/',include('ajax.urls')),

]
```

```分支路由
from django.conf.urls import url
from . import views
urlpatterns = []
```

```分支视图
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
from .models import Users
```

```__init__
#主程序
import pymysql
pymysql.install_as_MySQLdb()
```

## 1.什么是AJAX (阿贾克斯)

```
Asynchronous Javascript And Xml
	异步的       JS         和  Xml (JSON)
```

### 异步访问:

```
当客户端向服务器端发送请求时，服务器在处理的过程中，客户端无需等待，可以做其他操作
```

### AJAX的优点:	

```
	1.异步 的 访问方式
	2.局部 的 刷新方式

#### 
```

使用场合:

```
	1.搜索建议
​	2.表单验证
​	3.前后端完全分离
​		SPA -> Single Page Application

## 
```

## 2.AJAX核心对象-异步对象(XMLHttpRequest)

#### 	1.什么XMLHttpRequest		

```
简称为 "xhr"
		称为 "异步对象",代替浏览器向服务器发送异步的请求并接受响应
```

 **语 法**

	**支持XMLHttpRequest:**
	
			通过 : new XMLHttpRequest()　　　　　　　		  <---------高级版本，使用群体普遍
	
	**不支持XMLHttpRequest:**
	
			 通过 : new ActiveXObject("Microsoft.XMLhttp") 	 <----------低版本，使用群体少
```comm.js
function createXhr(){
    var xhr = null;
    //根据不同浏览器，创建不同的异步对象
    if(window.XMLHttpRequest){
        xhr=new XMLHttpRequest(); 				<---------创建支持XHR的异步对象
    }else{
        xhr=new ActiveXObject('Microsoft.XMLHTTP');			<-----------创建支持AxO的异步对象
    }
    return xhr;
}
```

#### 	2.创建异步对象	

```
xhr的创建是由js来提供的
		主流的异步对象是XMLHttpRequest类型的，并且主流浏览器都支持(IE7+,Chrome,Firefox,Safari,Opera)

​	支持XMLHttpRequest:
​		通过 new XMLHttpRequest()

​	不支持XMLHttpRequet:
​		通过new ActiveXObject("Microsoft.XMLHTTP")

​	判断浏览器的支持性:
​		if(window.XMLHttpRequest){
​			则说明浏览器支持 XMLHttpRequest
​		}else{
​			则说明浏览器支持 ActiveXObject("...")
​		}
示例:
	var xhr=createXhr();
```


​	

```
练习1:创建异步对象并输出
		1.创建一个Django程序 - AjaxDemo01
		2.创建一个应用 - ajax
		3.创建路由/视图
		4.在网页/模板中创建一个JS函数 - createXhr
		5.在函数中，创建异步对象并返回(或输出)
			浏览器到底支持XMLHttpRequest还是ActiveXObject


```

## 3.XHR的成员

#### 	1.方法 - open()	

```
	作用:创建请求
		语法:xhr.open(method,url,async);
			method:请求方式,取值 'get' 或 'post'
			url:请求地址,取值 字符串
			async:是否采用异步的方式发送请求
				true:异步的
				false:同步的
			示例:使用get方式向02-server的地址发送异步请求
				xhr.open('get','/02-server',true);
```

| 参　 数 | 作　用                     | 取　值                                            |
| ------- | -------------------------- | ------------------------------------------------- |
| method  | 请求方式                   | "get"  或  "post"                                 |
| url     | 请求地址                   | 字符串                                            |
| async   | 是否采用异步的方式发送请求 | true : 异步的发送请求　或　false : 同步的发送请求 |

```
注：async : 当代码中需要执行多次 : 向服务端发送请求时，如果后一次请求需要用前一次请求的结果，需要取值	   为false，请求发送设置为同步，以免造成前一次请求先结束，后一次请求没有得到前一次请求的结果。
```

#### 	2.属性 - readyState		

```
作用:表示请求状态，通过不同的请求状态值来表示xhr与服务器的交互情况
			由0-4共5个值来表示5个不同的状态
			0:请求尚未初始化
			1:已经与服务器建立连接
			2:服务器端已经接收请求信息
			3:服务器端处理中...
			4:响应完成
	示例:
			if(xhr.readyState==4 && xhr.status==200){
​			//可以接收服务器端的响应信息
​		}
```

| 请求状态值 | 由0-4共5个值表示5个不同的状态 |
| ---------- | ----------------------------- |
| 0          | 请求尚未初始化                |
| 1          | 已经与服务器建立联系          |
| 2          | 服务器端已经接受请求信息      |
| 3          | 服务器端处理中                |
| 4          | 服务端响应完成                |

#### 	3.属性 - status		

```
作用:表示服务器端的响应状态码
			200 : 服务器端正确处理请求并给出响应
			404 : Not Found
			500 : Internal Server Error

​	示例:(位置不可变)
​		if(xhr.readyState==4 && xhr.status==200){
​			//可以接收服务器端的响应信息
​		}
```

#### 注　意：先 readyState属性 后 status属性

```
服务器响应请求时先响应readyState ----属性,再响应status ----属性。

所以同时判断属性readyState和status响应时 : 先判断readyState属性再判断status 属性,先后顺序不能改变。
```

#### 4.属性 - responseText	

```
作用:表示服务器端响应回来的数据
	示例:
		if(xhr.readyState==4 && xhr.status==200){
			//可以接收服务器端的响应信息
			console.log(xhr.responseText);
		}
```

#### 5.事件 - onreadystatechange	

1 . 作　用：每当**readyState**值发生改变时要触发的操作。

```
	readyState：表示请求状态，通过不同的**请求状态值**来表示xhr与服务器的交互情况。

​	onreadystatechange -事件: 表示xhr与服务器的交互情况发生变化时要出发的事件。

​	onreadystatechange----------回调函数
```

2 . 操作 ---- 回调函数

3 . 每当服务器响应请求readyState值发生改变时,onreadystatechange回调函数返回重新调用

```
作用:每当xhr的readyState值发生改变时要触发的操作 - 回调函数
	示例:
		xhr.onreadystatechange = function(){
				if(xhr.readyState==4 && xhr.status==200){
				//可以接收服务器端的响应信息
				console.log(xhr.responseText);
			}
		}
```

| 服务器响应状态码 | 例如：                           |
| ---------------- | -------------------------------- |
| 404              | Not Found                        |
| 200              | 响应成功并返回正确的请求处理信息 |

```
例如：
if(xhr.readyState4 && xhr.status==200){
	//满足条件，允许接受服务器端的响应信息
}
#### 
```

#### 6.方法 - send()

```
	作用:通知xhr向服务器端开始发送请求
	语法:xhr.send(body);
		body:请求主体
		get请求:body的值为null
			xhr.send(null);
		post请求:body的置为 具体的请求数据
			xhr.send("请求数据");
```

| body     | 请求主体           | 示例:                |
| -------- | ------------------ | -------------------- |
| get请求  | body的值为null     | xhr.send(null)       |
| post请求 | body的值为请求数据 | xhr.send("请求数据") |

#### 4.AJAX的操作步骤

```
	1.GET请求
​		1.创建 xhr
​		2.创建请求 - open()
​		3.设置回调函数 - onreadystatechange
​			1.判断状态 
​			2.接收响应
​			3.业务处理
​		4.发送请求 - send(null)

示例：
	//1创建xhr
            var xhr=createXhr();
            //2创建请求
            xhr.open('get','/ajax/02-server',true);
            //3设置回调函数
            xhr.onreadystatechange=function(){
                if(xhr.readyState==4 && xhr.status==200){
                    //接收服务器端响应的数据
                    var res= xhr.responseText;
                    document.getElementById('show').innerHTML=res;
                }
            }
            //4发送请求
            xhr.send(null);
```


/02-server?uname=wangwc&uage=30

回顾：

# day2

## 1.核心对象 - xhr(XMLHttpRequest)

```
	file：static/common.js
	function createXhr(){
    var xhr = null;
    //根据不同浏览器，创建不同的异步对象
    if(window.XMLHttpRequest){
        xhr=new XMLHttpRequest();
    }else{
        xhr=new ActiveXObject('Microsoft.XMLHTTP');
    }
    return xhr;
}
```

## 2.xhr 的成员		

```
1.方法 - open(method,url,async)
		2.属性 - readyState
			4:服务器端响应完毕
		3.属性 - status
			200:服务器端正确响应所有信息
		4.属性 - responseText
		5.事件 - onreadystatechange
		6.方法 - send(body)
			get : null
			post : 发送的数据
```

======================================

## 1.使用AJAX发送POST请求	

```
### token就是令牌，最大的特点就是随机性，不可预测


```

```
可以在http请求中以参数的形式加入一个随机产生的token。并在服务器端建立一个拦截器来验证这个token，并在服务器端建立一个拦截器来验证这个token，如果请求中没有token或者token内容不正确，则认为可能是CSRF攻击而拒绝该请求。
```

```
1.创建xhr
​	2.创建请求
​		1.请求方式改为post
​		2.有请求参数的话不能拼在地址的后面
​		3.设置回调函数
​		4.设置请求消息头 - Content-Type
		示例:
​			xhr.setRequestHeader(
​				"Content-Type",
​				"application/x-www-form-urlencoded"
​			)
​		5.发送请求
​			请求数据放在send()的参数位置处
​			示例:
​				xhr.send("name=wangwc&age=30&gender=男");
```

```&lt;body&gt;
{% csrf_token %}
```

```&lt;script&gt;
//5.发送请求
var uname = $("#uname").val();
var upwd = $("#upwd").val();
//准备获取csrfmiddlewaretoken的值
var **csrf**=$("[name='**csrfmiddlewaretoken**']").val();
var params= "uname="+uname+"&upwd="+upwd+"&**csrfmiddlewaretoken**="+**csrf**;
xhr.send(params);
```

## 1.使用AJAX发送POST请求

​	1.创建xhr

​	2.JSON

### 	1.JSON: JavaScript      Object       Notation

### 											js                 	对象          表现方式

#### 	语法：

```
			对象表示为键值对
			数据由逗号分隔
			花括号保存对象
			方括号保存数组
```

#### json 键/值对

```
JSON键值对是用来保存JS对象的一种方式，和JS对象的写法也大同小异，键/值对组合中的键名写在前面并用双引号“”包裹，使用冒号：分隔，然后是值
```

JSON是JS对象的字符串表示法，它使用文本表示一个JS对象的信息，本质是一个字符串

```
以JS对象的格式来约束前后端交互的字符串数据
```

​	2.JSO - JS 对象

		使用 JS 对象表示一个人的信息，包含如下属性:
			姓名:wangwc
			年龄:30
			身高:180
			体重:180
		var obj = {
			name:"wangwc",
			age:30,
			height:180,
			weight:180
		}
	
		console.log("姓名:"+obj.name);
### 		注:最后一个一定不能加“逗号”

3.JSON规范

1.使用json表示单个对象

​		

```
1.{}表示一个对象

​		2.{}中使用key:value来表示属性(数据)

​		3.key必须使用“ ”引起来

​		4.value是字符串必须用“”引起来

​		5.多对 key:value 之间使用 “，”分隔
```



#### 	示例:

#### 			var obj = '{"name":"wangwc","age":18}';

### 	2.使用json表示多个对象

#### 		使用[] 来表示一组对象

```
	示例：
​	var users='[{"name":"wangwc","age":30},{"name":"qtx","age":29}]';
#### 
```

#### 4.前端中处理JSON

#### 	将得到的JSON串转换成JS对象、数组

```
	JSON.parse(JSON串);
​			var	js对象	=	JSON.parse(JSON串) 
```

实现JSON转换为对象，使用**JSON.parse()**方法

#### JS语言中，一切都是对象

```
对象：使用花括号{}引起来的内容，数据结构为{key：value1，key2：value2，...}的键值对结构（key为对象属性，value为对应的值）。键名可以使用整数和字符串来表示。值得类型可以是任意类型。

数组：数组在JS中是方括号[] 包裹起来的内容，数据结构为[“java”，“javascript”，“vb”，...]的索引结构。在JS中，数组是一种比较特殊的数据类型，可以用键值对，可以索引。值得类型任意。
```

# **day3**

$obj.load(url,data,callback)

url:请求地址,data表示参数,callback 回调函数

1.data

​	2.



$.get()

dataType:响应回来的数据的格式[可选]

取值:

html:响应文本当html处理

text:响应文本当普通文本处理

script:响应文本当js脚本执行

json:响应文本是json格式文本(直接转换成js对象/数组)

$.post()

4.$.ajax()

$.ajax({ajax参数对象})   ***(只能是一个参数)***   或者(键值对)

​	5.async:是否采用异步方式发送请求

​	6.success:响应成功后的回调函数

​	7.error

# Day3

## 1.JSON

```
Json后端发送前段接收
```









### 	1.服务器端的JSON处理

​		

```
1.在Python中的处理
			1.允许将 元组，列表，字典 转换成JSON串
			2.元组，字典，列表中的内容必须是
				字符串，数字
				元组，列表，字典

​		python中提供了json模块，json模块中提供dumps方法实现json串的转换
```

​	

```
2.在Django中的处理
		使用Django中提供的序列化模块来完成QuerySet到JSON串的转换

​		from django.core import serializers
​		jsonStr = serializers.serialize('json',QuerySet)
```

### 2.前端中将JS对象转换成JSON串

​	

```
方法:JSON.stringify(jsObj)
	作用:将jsObj转换成JSON串
```

### 3.服务器端中将JSON串转换为字典/列表

```
	方法:json.loads(jsonStr)
```

### 2.JQ对AJAX的支持

​	

#### 1.$obj.load()

​		语法:
​			

```
$obj.load(url,data,callback)
				url:请求地址
				data:请求参数  (JS传参   键引号加与不加一样)
				callback:响应成功后的回调
```

​	

```
	作用:加载远程地址的内容到$obj中
```

​		

用法:
			1.data
			 请求参数[可选],如果没有参数则使用get方式
			 1.通过字符串传参
				"key1=value1&key2=value2"

​			注:此种传参会使用get方式发送请求

|         .通过字符串传参          |          通过JS对象传参           |
| :------------------------------: | :-------------------------------: |
|    "key1=value1&key2=value2"     |    key1:"value1",key2:"value2"    |
| 注:此种传参会使用get方式发送请求 | 注:此种传参会使用post方式发送请求 |


​			 2.通过JS对象传参
​				{
​					key1:"value1",
​					key2:"value2"
​				}
​				注:此种传参会使用post方式发送请求
​		

```
	2.callback
				响应成功后的回调函数[可选]
				function(resText){
					resText:表示响应回来的数据
				}
```




### 	2.$.get()

​		

```
		作用:通过get方式异步的向远程地址发送请求
		语法:$.get(url,data,callback,type)
```

​			

```
			1.url:请求地址
			2.data:请求参数[可选]
				1.使用字符串
				2.使用JS对象
			3.callback:响应成功后的回调函数[可选]
				function(resText){
					

​			}
​			4.type:响应回来的数据的格式[可选]
​				取值如下:
​				1.html:响应回来的文本当成html文本处理
​				2.text:响应回来的文本当成普通文本处理
​				3.script:响应回来的文本当JS脚本执行
​				4.json:响应回来的文本是JSON格式,会直接转换成JS对象/数组

			dataType:响应回来的数据的格式[可选]
			取值:

            html:响应文本当html处理

            text:响应文本当普通文本处理

            script:响应文本当js脚本执行

            json:响应文本是json格式文本(直接转换成js对象/数组)


```

### 3.$.post()

```
	语法:$.post(url,data,callback,type)
	各个参数同$.get()
```

### 4.$.ajax()

​	

```
$.ajax({ajax参数对象})   ***(只能是一个参数)***   或者(键值对)
```

```
作用:自定义所有的ajax参数
	语法: $.ajax({AJAX的参数对象})
```

​	AJAX的参数对象:

2. ```
   1.url : 请求的地址
   
   2. data : 请求到服务器端的参数
      1.字符串 : "key1=value1&key2=value2"
         	2.JS对象: {key1:"value1",key2:"value2"}
      3.type : 请求方式 'get' 或 'post'
      4.dataType : 响应回来的数据的格式
      	json,html,text,script
   ```

```
5.async : 是否采用异步的方式发送请求
	true:异步(默认值)
	false:同步
```

```
6.success:响应成功后的回调函数
	function(resText){
		resText表示的是响应回来的数据
	}
```

```
7.error:请求或响应失败时的回调函数
	function(){
	}
```



