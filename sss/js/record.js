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
//历史战绩查询
function Found(){
    var record_d=($('#record-form').serializeJson());
    if(record_d.myid==undefined){
        alert("玩家id不得为空!");
        return;
    }else if(record_d.limit==undefined){
        alert("每页条数不能为空！");
        return;
    }else if(record_d.page==undefined){
        alert("页码不能为空！");
        return;
    }

    //默认每页人数
    let num1 = record_d.limit;
    //定义一个变量保存每页真实应该展示的数量
    let num2;
    //首页展示
    let page = 1;
    var params ={};
    params.player_id=$("#myid").val();
    params.limit=$("#limit").val();
    params.page=$("#page").val();
    console.log(params.player_id);
    console.log(localStorage.token);
    $.ajax({
        type:"GET",
        url: "http://api.revth.com/history",
        dataType:"json",
        data:JSON.stringify(params),
        headers:{
            'X-Auth-Token':localStorage.token
        },
        success:function(result){
            //服务端返回数据
            console.log(data);
            const render = function () {
                //判断当前选择的页码对应的人数
                if (result.length - num1 * (page - 1) >= 10) {
                    num2 = 10;
                } else {
                    num2 = result.length - num1 * (page - 1);
                }
    
    　　　　　　　//该页对应数据
                for (let i = num1 * (page - 1); i < num2 + num1 * (page - 1); i++) {
                    table.innerHTML +=
                        `<tr>
                <th>${result[i].id}</th>
                <th>${result[i].card[0]}</th>
                <th>${result[i].card[1]}</th>
                <th>${result[i].card[2]}</th>
                <th>${result[i].score}</th>
                <th>${result[i].timestamp}</th>
            </tr>`;
                }
            }
            render();    
            const creatPages = function () {
                pages.innerHTML = '';
                for (let i = 0; i < Math.ceil(result.length / num1); i++) {
                    pages.innerHTML += ` <button data-page="${i+1}">${i+1}</button>`
                }
            }
            creatPages();
            //前翻页
            prev.onclick = function () {
                if (page > 1) {
                    page--;
                    render();
                } else {
                   alert('当前为第一页！')
                }
            }

        //后翻页
        next.onclick = function () {
            if (page < Math.ceil(result.length / num1)) {
                page++;
                render();
            } else {
                alert('当前为最后一页！')
            }
        }
        pages.addEventListener('click', function (e) {
            page = e.target.getAttribute('data-page');
            render();
        })
        },
        error:function(){
            alert("输入有误！");
        }
    });
}

