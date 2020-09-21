function copy(e) {
    e.preventDefault()
    let copyText = document.querySelector("#link");
    copyText.select();
    document.execCommand("copy");
    document.querySelector("#copy").style.display='none';
    copyText.value = '';
    var dialog = document.querySelector('dialog');
    dialog.show();
    setTimeout(function(){ dialog.close(); }, 2500);


}

document.querySelector("#copy").addEventListener("click", copy);

