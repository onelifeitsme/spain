$(function () {
	"use strict";
	var checkDate = function () {
		$.ajax({
			url: 'checkreserv/',
			type: 'GET',
			success: function (response) {
				$('input[name="checkout"]').daterangepicker({
					singleDatePicker: true,
					dateFormat: 'yy-mm-dd',
					isInvalidDate: function (date) {
						if (date.format("YYYY-MM-DD") in response) {
							return true;
						}
						return false;
					},
				});
				$('input[name="checkout"]').val('');
				$('input[name="checkout"]').attr("placeholder", "Check Out");

				$('input[name="checkin"]').daterangepicker({
					singleDatePicker: true,
					dateFormat: 'yy-mm-dd',
					isInvalidDate: function (date) {
						if (date.format("YYYY-MM-DD") in response) {
							return true;
						}
						return false;
					},
				});
				$('input[name="checkin"]').val('');
				$('input[name="checkin"]').attr("placeholder", "Check In");
			},
			error: function (data) {
				alert('Ошибка загрузки даты');
			},
		})
	};
	checkDate();
})

const form_reserv = $('#reserv_form');
// const comments_list = $('.review_jump');
// const url_refresh = 'refresh/';
const url_reserv = 'reserved/';

form_reserv.on('submit', function (e) {
    e.preventDefault();
    $.ajax({
        url: url_reserv,
        type: 'POST',
        csrfmiddlewaretoken: getCookie('csrftoken'),
        data: form_reserv.serialize(),
        success: function (data) {

						if (!('success' in data)) {
							alert('На выбранный период уже есть резерв');
						} else {
							$('#success_booking_price').text(data.total_price)
							$('#success_booking_checkin').text(data.checkin)
							$('#success_booking_checkout').text(data.checkout)
							$('#success_booking_modal').modal('show');
						};
        },
        error: function (data) {
            if (data.user==undefined) {
                $('#login').modal('show');
            }
        },
    })
});
$('.success_booking_confirm').click(function () {
	location.reload();
});


$(function() {
	$('input[name="checkin"], input[name="checkout"]').on('change',
    function(){
      let checkout = $('input[name="checkout"]').val()
			let checkin = $('input[name="checkin"]').val()
	    if (checkin && checkout)
				lenghtDatePrice(checkin, checkout);
    });
});

let lenghtDatePrice = function (checkin, checkout) {
	let checkinSplited = checkin.split('/');
	let checkoutSplited = checkout.split('/');
	let from_date = _getDate(checkinSplited);
	let to_date = _getDate(checkoutSplited);
	let Days = Math.floor((to_date.getTime() - from_date.getTime())/(1000*60*60*24));
	setTotalPrice(Days + 1);
}
let _getDate = function (date) {
	let year = Number(date[2])
	let month = Number(date[0])
	let day = Number(date[1])
	return new Date(year, month, day)
}

let setTotalPrice = function (days) {
	if (days > 0) {
		let price_per = $('.price_per').text()
		$('.total_price').text(days * Number(price_per))
		$('input[name="total_price"]').val(days * Number(price_per))
	} else	{
		$('.total_price').text(0)
		$('input[name="total_price"]').val(0)
	}
}