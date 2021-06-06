var count = 0;
function adicionar(campo){
    count++;
    document.getElementById(campo).innerHTML += "<input class='form-control'"
    + "type='text' placeholder='"+campo+"' style='margin-bottom: 10px; margin-top: 10px' id='"+ campo + count + "' name='"+ campo+"'>";
}

function removercampo(campo){
    if (count == 0 || count == null){
        return 0
    }
    var id = campo+count
    document.getElementById(id).remove()
    count--
}