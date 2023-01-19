function timeout(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}       

let GetHomeAwayValues =async function(){
    document.getElementsByClassName("AwayDiv")[0].style = "background-color:transperant;"
    document.getElementsByClassName("HomeDiv")[0].style = "background-color:transperant;"
    document.getElementById("HomeWin").style = "color:white; font-size: x-large;"
    document.getElementById("AwayWin").style = "color:white; font-size: x-large;"
    document.getElementById("HomeWin").innerHTML = "Home Team"
    document.getElementById("AwayWin").innerHTML = "Away Team"
var data = $("#MyForm").serialize();
document.getElementById("AwayFlag").style = "opacity:0.2"
document.getElementById("HomeFlag").style = "opacity:0.2"
var isLoaded = false   
let intervalId = window.setInterval(()=>{
    
    if(isLoaded){
       
    
            document.getElementById("AwayFlag").style = "opacity:1"
            document.getElementById("HomeFlag").style = "opacity:1" 
            window.clearInterval(intervalId);
            
        }
    
} , 50);
    $.ajax(
        {
        contentType: 'application/x-www-form-urlencoded; charset=UTF-8',
        type: "POST",
        url: "http://127.0.0.1:5000/Match/"+document.getElementById("Home").value+"-"+ document.getElementById("Away").value,
        data: data,
        
        success: function(data) {
           isLoaded = true
            document.getElementById("HomeFlag").src = data.homeFlag
            document.getElementById("AwayFlag").src = data.AwayFlag
        },
        error: function(error) {
            console.log(error)
        }
    });
    intervalId()
    
    
   
    
 
    
}



