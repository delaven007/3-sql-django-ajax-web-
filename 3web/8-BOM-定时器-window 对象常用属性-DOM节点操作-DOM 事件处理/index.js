
function $(tag,index){  //变量声明未赋值默认为undefined
    var elem;
    if(index){
        var elem=document.getElementsByTagName(tag)[index];
    }else{//index=0或index=undefined
        elem=document.getElementsByTagName(tag)[0];
    }
    return elem;
}
$("h1",2)