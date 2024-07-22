document.addEventListener('DOMContentLoaded', function() {
    var isProDiverField = document.getElementById('id_is_pro_diver');
    var proDiverFields = document.getElementById('pro-diver-fields');
    var nonProDiverFields = document.getElementById('non-pro-diver-fields');

    function toggleFields() {
        if (isProDiverField.checked) {
            proDiverFields.style.display = 'block';
            nonProDiverFields.style.display = 'none';
        } else {
            proDiverFields.style.display = 'none';
            nonProDiverFields.style.display = 'block';
        }
    }

    isProDiverField.addEventListener('change', toggleFields);
    toggleFields();  // Initialize fields on page load
});
