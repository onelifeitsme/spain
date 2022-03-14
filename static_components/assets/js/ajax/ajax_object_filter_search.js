$('document').ready(function () {
	var searchInputForm = $('.search-input-form');
	searchInputForm.on('input', function (e) {
		e.preventDefault();
		$.ajax({
			url: 'search_by_name/',
			type: 'GET',
      // csrfmiddlewaretoken: getCookie('csrftoken'),
			// data: searchInputForm.serialize(),
			data: {'name': $('.search-input').val()},
			success: function (data) {
				$('.object-list-container').html(data);
				// alert('suc')
			},
			error: function (data) {
				alert('Ошибка');
			},
		})
	})
})
// $('document').ready(function () {
// 	$('.search-input').on('input', function (e) {
// 		e.preventDefault();
// 		$.ajax({
// 			url: '',
// 			type: 'GET',
// 			data: {'search_input': $('.search-input').val()},
// 			success: function (data) {
// 				$('.object-list-container').html(data);
// 			},
// 			error: function (data) {
// 				alert('Ошибка');
// 			},
// 		})
// 	})
// })

