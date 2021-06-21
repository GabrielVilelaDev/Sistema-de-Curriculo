//objetivos
$(document).on('click', 'button#Addobjetivos', function() {
    $("#objetivos").append(
      '<div class="objetos-div">'+
      '<button class="btn" id="Removeobjetivos"><img src="/static/images/remove.png"></button>'+
      '<input type="text" name="descricao" maxLength="200" class="form-control campodinamico" required=""'+
      'id="id_descricao">'+
      "</div>"
    )
});
$(document).on('click', 'button#Removeobjetivos', function() {
  $(this).closest('div.objetos-div').remove();
});
//objetivos



//habilidades
$(document).on('click', 'button#Addhabilidades', function() {
    $("#habilidades").append(
      '<div class="habilidades-div">'+
      '<button class="btn" id="Removehabilidades"><img src="/static/images/remove.png"></button>'+
      '<input type="text" name="descricao" maxLength="200" class="form-control campodinamico" required=""'+
      'id="id_descricao">'+
      "</div>"
    )
});
$(document).on('click', 'button#Removehabilidades', function() {
  $(this).closest('div.habilidades-div').remove();
});
//habilidades



//formacao
$(document).on('click', 'button#Addformacao', function() {
    $("#formacao").append(
      '<div class="formacao-div">'+
      '<button class="btn" id="Removeformacao"><img src="/static/images/remove.png"></button>'+
      '<input type="text" name="descricao" maxLength="200" class="form-control campodinamico" required=""'+
      'id="id_descricao">'+
      "</div>"
    )
});
$(document).on('click', 'button#Removeformacao', function() {
  $(this).closest('div.formacao-div').remove();
});
//formacao
