function copy(e) {
    e.preventDefault()
    let copyText = document.querySelector("#link");
    copyText.select();
    document.execCommand("copy");
}

document.querySelector("#copy").addEventListener("click", copy);