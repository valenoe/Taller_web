(function($) {
  $(document).ready(function() {
    var previsionSaludField = $('#id_prevision_salud');
    var tipoIsapreField = $('#id_tipo_isapre');

    function toggleTipoIsapreField() {
      if (previsionSaludField.val() === 'isapre') {
        tipoIsapreField.closest('.form-group').show();
      } else {
        tipoIsapreField.closest('.form-group').hide();
      }
    }

    previsionSaludField.on('change', toggleTipoIsapreField);

    toggleTipoIsapreField();
  });
})(django.jQuery);
