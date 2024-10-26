(function($) {
    $(document).ready(function() {
        $('#id_section').change(function() {
            const section = $(this).val();
            const itemField = $('#id_item_name');
            itemField.empty();

            if (section) {
                $.ajax({
                    url: `/get_items/${section}/`,
                    success: function(data) {
                        itemField.append(new Option("Select Item", ""));
                        data.items.forEach(item => {
                            itemField.append(new Option(item.name, item.id));
                        });
                    }
                });
            }
        });
    });
})(django.jQuery);