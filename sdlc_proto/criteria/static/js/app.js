$(function () {
    $('.cell-container')
        .popup({
            on: 'click',
            inline: false
        })
    ;

    $('.save-criteria').click(function () {
        var form = $(this).closest('form.update-criteria');
        var formData = form.serialize();
        var elementId = form.attr('id');

        $.ajax({
            url: '/criteria/update',
            data: formData,
            type: 'post',
            cache: false,
            success: function (data) {
                console.log('success ', elementId, 'change');

                $('#criteriaCell' + elementId.split('criteriaForm')[1])
                    .popup('hide');
            },
            error: function (xhr, ajaxOptions, thrownError) {
                document.getElementById(elementId).reset();
            }
        });
        return false;
    });

    var textContent = ('textContent' in document) ? 'textContent' : 'innerText';

    function valueOutput(element) {
        var value = element.value;
        var output = element.parentNode.getElementsByTagName('output')[0] || element.parentNode.parentNode.getElementsByTagName('output')[0];
        output[textContent] = value;
    }

    $(document).on('input', 'input[type="range"]', function (e) {
        valueOutput(e.target);
    });

    $("input[type='range']").each(function () {
        valueOutput(this);
    });
});