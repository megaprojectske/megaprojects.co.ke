(function ($) {

    $(window).load(function () {
        $('.columns-2').each(function (index, object) {
            var col1 = $(object).find('.column-1');
            var col2 = $(object).find('.column-2');

            var maxH = Math.max(col1.height(), col2.height());

            col1.css('min-height', maxH);
            col2.css('min-height', maxH);
        });

        $('.columns-3').each(function (index, object) {
            var col1 = $(object).find('.column-1');
            var col2 = $(object).find('.column-2');
            var col3 = $(object).find('.column-3');

            var maxH = Math.max(col1.height(), col2.height(), col3.height());

            col1.css('min-height', maxH);
            col2.css('min-height', maxH);
            col3.css('min-height', maxH);
        });
    });

})(jQuery);
