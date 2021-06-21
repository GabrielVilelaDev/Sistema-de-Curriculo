$(document).ready(function(){
  $("#Addobjetivos").click(function(){
    $("#objetivos").append(
        "{% for field in objetivos_form.visible_fields %}"+
          "{{field|add_class:'form-control campodinamico'}}"+
          "{% endfor %}"
    )
  });
});