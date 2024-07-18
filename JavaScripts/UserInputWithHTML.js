let userName;
document.getElementById("btn1").onclick=function event(){
    userName=document.getElementById("lol").value;
    document.getElementById("h1").textContent=`Hello , ${userName}`
}