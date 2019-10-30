$(function(){
    console.log("123");    
    var flag = true;                               
    $.ajax({
        type:"GET",
        url: "http://api.revth.com/rank",
        dataType:"json",
        contentType: "application/json;charset-UTF-8",
        success:function(result){
            for(var i=0;i<91;i++){
                document.getElementById("td"+i+"1").innerText=i+1;
                document.getElementById("td"+i+"2").innerText=result[i].player_id;
                document.getElementById("td"+i+"3").innerText=result[i].name;
                document.getElementById("td"+i+"4").innerText=result[i].score;
            }
        },
        error:function(res){
            alert("获取数据失败！");
        }
    });                   
    }
)