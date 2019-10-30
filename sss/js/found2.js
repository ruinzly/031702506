$(function(){
    document.getElementById("input1").value=localStorage.id;
    document.getElementById("input2").value=localStorage.timestamp;
    for(var i=0;i<4;i++){
        document.getElementById("td"+i+"1").innerText=localStorage.name[i];
        document.getElementById("td"+i+"2").innerText=localStorage.card[i][0];
        document.getElementById("td"+i+"3").innerText=localStorage.card[i][1];
        document.getElementById("td"+i+"4").innerText=localStorage.card[i][2];
        document.getElementById("td"+i+"5").innerText=localStorage.score[i];
        document.getElementById("td"+i+"6").innerText=localStorage.play_id[i];
    }
})