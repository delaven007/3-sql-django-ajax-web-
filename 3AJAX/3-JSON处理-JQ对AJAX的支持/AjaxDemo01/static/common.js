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