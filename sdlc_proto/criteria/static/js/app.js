$(function () {
    $('.cell-container')
        .popup({
            on: 'click',
            inline: false
        })
    ;

    $('.score-container')
        .popup({
            on: 'click',
            inline: false
        })
    ;

    function getParameterByName(name, url) {
        if (!url) url = window.location.href;
        name = name.replace(/[\[\]]/g, "\\$&");
        var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)"),
            results = regex.exec(url);
        if (!results) return null;
        if (!results[2]) return '';
        return decodeURIComponent(results[2].replace(/\+/g, " "));
    }

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
                var cid = elementId.split('criteriaForm')[1];

                var criteriaCell = $('#criteriaCell' + cid);

                criteriaCell
                    .popup('hide');


                var textContent = ('textContent' in document) ? 'textContent' : 'innerText';
                criteriaCell.children('.benefits-score')[0][textContent] = 'B' + getParameterByName('benefits', formData);
                criteriaCell.children('.hurts-score')[0][textContent] = 'H' + getParameterByName('hurts', formData);
            },
            error: function (xhr, ajaxOptions, thrownError) {
                document.getElementById(elementId).reset();
            }
        });
        return false;
    });

    $('.save-score').click(function () {
        var form = $(this).closest('form.score-criteria');
        var formData = form.serialize();
        var elementId = form.attr('id');

        $.ajax({
            url: '/criteria/score',
            data: formData,
            type: 'post',
            cache: false,
            success: function (data) {
                console.log('success ', elementId, 'score');
                var sid = elementId.split('scoreForm')[1];

                var scoreCell = $('#scoreCell' + sid);

                scoreCell
                    .popup('hide');

                scoreCell.css('background', 'inherit');


                var textContent = ('textContent' in document) ? 'textContent' : 'innerText';
                scoreCell.children('.score')[0][textContent] = getParameterByName('score', formData);
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

        if (element.name === "benefits") {
            const textList = [
                'مزیت خاصی محسوب نمی‌شه',
                'کار رو کمی راحت‌تر می‌کنه',
                'مفید و بدرد بخوره',
                'بسیار کار راه‌اندازه'
            ];

            value = value + "   وجودش " + textList[parseInt(value)];
        } else if (element.name === "hurts") {
            const textList = [
                'مشکلی به وجود نمیاره',
                'مشکلات جزئی ایجاد می‌کنه',
                'مشکل سازه',
                'کار رو فلج می‌کنه'
            ];

            value = value + "   عدم وجودش " + textList[parseInt(value)];
        } else if (element.name === "score") {
            const textList = [
                'Not available',
                'Have serious issues',
                'Below average',
                'As expected',
                'Above average',
                'Outstanding'
            ];

            value = value + "   " + textList[parseInt(value)];
        }

        output[textContent] = value;
    }

    $(document).on('input', 'input[type="range"]', function (e) {
        valueOutput(e.target);
    });

    $("input[type='range']").each(function () {
        valueOutput(this);
    });
});