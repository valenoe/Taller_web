    const selection = document.getElementById('selection');
    
    const disabledField = document.getElementById('disabledField');
    
    selection.addEventListener('change', function() {
      const selectedValue = selection.value;
      
      if (selectedValue === '2') {
        disabledField.disabled = false;
      } else {
        disabledField.disabled = true;
      }
    });