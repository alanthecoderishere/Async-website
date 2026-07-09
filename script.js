// 1990s style script
function showDate() {
    var d = new Date();
    // Simulate it being 1990 to fit the lore (post-KV31 milestone)
    d.setFullYear(1990);
    
    // Add leading zero if needed
    var hours = d.getHours();
    var minutes = d.getMinutes();
    var seconds = d.getSeconds();
    
    if (hours < 10) hours = "0" + hours;
    if (minutes < 10) minutes = "0" + minutes;
    if (seconds < 10) seconds = "0" + seconds;
    
    var timeString = hours + ":" + minutes + ":" + seconds;
    var dateString = "Current System Time: " + d.toDateString() + " " + timeString;
    
    document.getElementById("dateDisplay").innerHTML = dateString;
    setTimeout(showDate, 1000);
}

function checkLogin() {
    var user = document.getElementsByName("user")[0].value;
    var pass = document.getElementsByName("pass")[0].value;
    
    if (user === "" || pass === "") {
        alert("Please enter both Username and Password.");
    } else {
        alert("FATAL ERROR 0x000000ED: Unmountable Boot Volume.\nConnection to mainframe lost. Please contact the network administrator.");
        // Clear fields
        document.getElementsByName("user")[0].value = "";
        document.getElementsByName("pass")[0].value = "";
    }
}
