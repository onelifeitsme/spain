const form_review = $('#review_form');
const comments_list = $('.review_jump');
const url_refresh = 'refresh/';
const url_form = 'review/';

form_review.on('submit', function (e) {
    e.preventDefault();
    $.ajax({
        url: url_form,
        type: 'POST',
        csrfmiddlewaretoken: getCookie('csrftoken'),
        data: form_review.serialize(),
        success: function (data) {
            resetForm(form_review);
            $([document.documentElement, document.body]).animate({
                scrollTop: comments_list.offset().top - 150
            }, 500);
            refreshTemplate(url_refresh, form_review);
        },
        error: function (data) {
            alert('Ошибка')
        },
    })
});

let refreshTemplate = function (url) {
    return $.ajax({
        url: url,
        type: 'GET',
        success: function (data) {
            comments_list.html(data);
        },
        error: function (data) {
            alert(data);
        },
    });
};

let resetForm = function (obj) {
    obj.each(function () {
        this.reset();
    })
}