(function($) {
    'use strict';
    $(document).ready(function() {
        var $statusRadios = $('input[name="status"]');
        
        function updateStatusOptions() {
            var currentStatus = $statusRadios.filter(':checked').val();
            var $restrictedOptions = $statusRadios.filter('[value="ship"], [value="done"], [value="cancel"]');
            
            if (currentStatus === 'new') {
                $restrictedOptions.each(function() {
                    $(this).prop('disabled', true);
                    $(this).closest('label').css({
                        'opacity': '0.4',
                        'cursor': 'not-allowed',
                        'text-decoration': 'line-through'
                    });
                });
            } else {
                $restrictedOptions.each(function() {
                    $(this).prop('disabled', false);
                    $(this).closest('label').css({
                        'opacity': '1',
                        'cursor': 'pointer',
                        'text-decoration': 'none'
                    });
                });
            }
        }

        // Initial check
        updateStatusOptions();

        // Listen for changes
        $statusRadios.on('change', function() {
            updateStatusOptions();
        });
    });
})(django.jQuery);
