var submit = document.getElementById('username')
window.onsubmit = function() {

    var r = new RegExp(/^(ftp|http|https):\/\/open.spotify[^ "]+$/);
    if ((submit.value == '') || r.test(submit.value) == false){
        alert('You must enter a valid profile link')
        return false
    }
    else return true
};