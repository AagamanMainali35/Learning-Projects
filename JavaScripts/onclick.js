let a;
document.getElementById("btn1").onclick=function(){
    a= document.getElementById("lol").value;
    document.getElementById("h1").textContent=`Welcome , ${a}`
}