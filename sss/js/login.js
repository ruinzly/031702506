var token="";

function disappear(p)
{
    document.getElementById(p).value="";
}
function judge(id,text)
{
    var x=document.getElementById(id).value;
    if(x=="")
        document.getElementById(id).value=text;
}

//读取表单信息
(function ($) {
    $.fn.serializeJson = function () {
        var serializeObj = {};
        var array = this.serializeArray();
        var str = this.serialize();
        $(array).each(function () {
            if (serializeObj[this.name]) {
                if ($.isArray(serializeObj[this.name]) && this.value != "") {
                    serializeObj[this.name].push(this.value);
                } else {
                    if (this.value != "") {
                        serializeObj[this.name] = [serializeObj[this.name], this.value];
                    }
                }
            } else {
                if (this.value != "") {
                    serializeObj[this.name] = this.value;
                }
            }
        });
        return serializeObj;
    };
})(jQuery);

//注册
function register1(){
    //返回json对象
    var register_d=($('#register-form').serializeJson());
    if(register_d.username=="ruin"){
        alert("请输入账号");
        return;
    }else if(register_d.password_1=="ruin014299"){
        alert("请输入密码");
        return;
    }else if(register_d.password_2=="ruin014299"){
        alert("请再次输入密码");
        return;
    }else if(register_d.password_1!=register_d.password_2){
        alert("密码不一致，请重新设置！");
        return;
    }
    var params ={};
     params.username=$("#username").val();
     params.password=$("#password").val();
    // var username=$("#username").val
    $.ajax({
        type:"post",
        url: "http://api.revth.com/register",
        dataType:"json",
        data:JSON.stringify(params),
        contentType: "application/json;charset-UTF-8",
        success:function(返回内容){
            console.log(返回内容);//打印服务端返回的数据
            if(返回内容.status==0){
                alert("注册成功");
                window.location.href="./login.html";
            }
        },
        error:function(返回内容){
            console.log(返回内容);//打印服务端返回的数据

            alert("注册失败！")
        }
    });
}

//绑定
function register2(){
    var register_d=($('#register-form').serializeJson());
    if(register_d.username=="ruin"){
        alert("请输入账号");
        return;
    }else if(register_d.password=="ruin014299"){
        alert("请输入密码");
        return;
    }else if(register_d.student_number=="031702506"){
        alert("请输入学号");
        return;
    }else if(register_d.student_password=="ruin014299"){
        alert("请输入教务处密码");
        return;
    }
    var params ={};
    params.username=$("#username").val();
     params.password=$("#password").val();
    params.student_number=$("#student_number").val();
    params.student_password=$("#student_password").val();

    $.ajax({
        type:"post",
        url: "http://api.revth.com/auth/register2",
        dataType:"json",
        data:JSON.stringify(params),
        contentType: "application/json;charset-UTF-8",
        success:function(返回内容){
           // console.log(返回内容);//打印服务端返回的数据
            if(返回内容.status==0){
                alert("注册并绑定成功");
                window.location.href="./login.html";
            }
        },
        error:function(返回内容){
            alert("注册失败！")
            console.log(返回内容);//打印服务端返回的数据
        }
    });
}

//登录
function login(){
    var login_d=($('#login-form').serializeJson());
    if(login_d.username==""){
        alert("请输入账号");
        return;
    }else if(login_d.password==""){
        alert("请输入密码");
        return;
    }
    $.ajax({
        type:"POST",
        url: "http://api.revth.com/auth/login",
        dataType:"json",
        data:JSON.stringify(login_d),
        contentType: "application/json;charset-UTF-8",
        success:function(返回内容){
            console.log(返回内容);//打印服务端返回的数据
            if(返回内容.status==0){
                token=返回内容.data.token;
                localStorage.setItem('token',返回内容.data.token);//将token的值存入本地缓存中
                localStorage.setItem('user_id',返回内容.data.user_id);//将user_id的值存入本地缓存中
                console.log(window.localStorage);
                alert("登录成功");
                window.location.href="./result.html";
            }
        },
        error:function(返回内容){
            alert("账号/密码错误，请重新登录！");
        }
    });
}

//开始游戏
var dun= new Array();
var game_id="";
var num=0;
function battle(){
    $.ajax({
        type:"POST",
        url:"http://api.revth.com/game/open",
        dataType:"json",
        headers:{
            'X-Auth-Token':localStorage.token
        },
        success:function(result){
            console.log(result.data);
            var pai=new Array();
            pai=changeData(result.data.card);
            game_id=result.data.id;
            dun=changeData1(main(pai));
            //将user_id的值存入本地缓存中
            localStorage.setItem('dun',dun);
            Found();
        },
        error:function(res){
            alert("战局开启失败！");
        }
    });
}


