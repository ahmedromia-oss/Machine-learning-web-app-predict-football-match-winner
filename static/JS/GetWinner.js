let GetHomeAwayWinner =async function(){
    document.getElementById("AwayWin").innerHTML = "Away Team"
    document.getElementById("HomeWin").innerHTML = "Home Team"
    document.getElementById("HomeWin").style = "color:white; font-size: x-large;"
    document.getElementById("AwayWin").style = "color:white; font-size: x-large;"
    
        var data = $("#MyForm").serialize();
        function timeout(ms) {
            return new Promise(resolve => setTimeout(resolve, ms));
        }
        for(var i = 0; i<11 ; i++ ){
            // await timeout(100)
            document.getElementById("HomeBackGround").style = "background-color:brown"
            
            document.getElementById("AwayBackGround").style = "background-color:transperant"
            await timeout(150)
            document.getElementById("AwayBackGround").style = "background-color:brown"
            document.getElementById("HomeBackGround").style = "background-color:transperant"
            await timeout(150)

        }   
    
            $.ajax({
          
                contentType: 'application/x-www-form-urlencoded; charset=UTF-8',
                type: "POST",
                url: "http://127.0.0.1:5000/predict/"+document.getElementById("Home").value+"-"+ document.getElementById("Away").value,
                data: data,
                success:function(data) {
                    thedata = data
                    if(data == "Home"){
                        document.getElementById("HomeWin").innerHTML = "Winner"
                        document.getElementById("HomeWin").style = "color:#FFD700; font-size: x-large;"
                        document.getElementsByClassName("HomeDiv")[0].style = "background-color:brown;"
                        document.getElementsByClassName("AwayDiv")[0].style = "background-color:transperant;"
    
    
                    }
                    else{
                        document.getElementById("AwayWin").innerHTML = "Winner"
                        document.getElementById("AwayWin").style = "color:#FFD700; font-size: x-large;"
                        document.getElementsByClassName("AwayDiv")[0].style = "background-color:brown;"
                        document.getElementsByClassName("HomeDiv")[0].style = "background-color:transperant;"
    
                    }
                    
                    
                },
                error: function(error) {
                    console.log(error)
                }
        });
}