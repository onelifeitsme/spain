$(function () {
	"use strict";
	const filter_form_form = $('.radio-custom');
	filter_form_form.click(function () {
		let label_value = $("label[for='"+this.id+"']").html();
		$(this).parent().parent().parent().parent().parent().parent().parent().parent().find('span').html(label_value);
	});
});