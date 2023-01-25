function get_int(input){
     num = ""
    for (let i = 0; i < input.length; i++) {
        if (input[i]== "U" / input[i]== "D"){
            break
        } else{
            num += input[i]
        }
    }
    return parseInt(num)
 }
function upvote(word){
    let url = window.location.origin
    let request = new XMLHttpRequest();
    request.open("GET", url + "/upvote/" + word);
    request.send();
    let val = document.getElementById("upvote");
    val.innerHTML = (get_int(val.textContent) + 1) + " Upvotes"
}
function downvote(word){
    let url = window.location.origin
    let request = new XMLHttpRequest();
    request.open("GET", url + "/downvote/" + word);
    request.send();
    let val = document.getElementById("downvote");
    val.innerHTML = (get_int(val.textContent) + 1) + " Downvotes"
}