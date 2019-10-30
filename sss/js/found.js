//读取表单
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
//用于判断当前列表是否已经打开
var history_f = {};
for (var i = 1; i < 300; i++) history_f[i] = 0;
//查询战局详情
function found(obj){
    var str = obj.parentNode.id;
    var battleid=$("#battleid").val();
    $("#input1").val=battleid;

    //提取当前的序号
    str = str.substring(7, str.length)
    if (history_f[parseInt(str)] == 0) {
        $.ajax({
            headers: {
                //token
                "X-Auth-Token": localStorage.token
            },
            type: "GET",
            url: "http://api.revth.com/history/"+battleid,
            contentType: "application/json;charset-UTF-8",
            success: function (result) {
                var arr = result.data.detail;
                console.log(arr[0].name);
                for(var i=0;i<4;i++){
                    document.getElementById("td"+i+"1").innerText=arr[i].name;
                    document.getElementById("td"+i+"2").innerText=arr[i].card[0];
                    document.getElementById("td"+i+"3").innerText=arr[i].card[1];
                    document.getElementById("td"+i+"4").innerText=arr[i].card[2];
                    document.getElementById("td"+i+"5").innerText=arr[i].score;
                    document.getElementById("td"+i+"6").innerText=arr[i].player_id;
                }
                if (arr.length > 0) {
                    xxx = '<p>'
                    arr.forEach(element => {
                        xxx += "name:" + element.name + "	card:" + element.card + "	score:" +
                            element
                                .score + "<br>";
                    });
                    xxx += "</p>"
                }

                // document.getElementById("collapse" + str).childNodes[1].innerHTML = xxx;
            },
            error: function (res) {
                console.log(res);
                alert("失败");
            }
        })
        history_f[parseInt(str)] = 1;
    } else {
        history_f[parseInt(str)] = 0;
    }
}

// $(function(){
//     document.getElementById("input1").value=localStorage.id;
//     document.getElementById("input2").value=localStorage.timestamp;
//     for(var i=0;i<4;i++){
//         document.getElementById("td"+i+"1").innerText=localStorage.name[i];
//         document.getElementById("td"+i+"2").innerText=localStorage.card[i][0];
//         document.getElementById("td"+i+"3").innerText=localStorage.card[i][1];
//         document.getElementById("td"+i+"4").innerText=localStorage.card[i][2];
//         document.getElementById("td"+i+"5").innerText=localStorage.score[i];
//         document.getElementById("td"+i+"6").innerText=localStorage.play_id[i];
//     }
// })