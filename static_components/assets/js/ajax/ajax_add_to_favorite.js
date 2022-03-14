// $(document).ready(function () {
//   // отслеживаем событие отправки формы
//   $('.btn').click(function () {
//       // создаем AJAX-вызов
//       $.ajax({
//           data: $(this).serialize(),
//           url: "{% url 'favorite_add' %}",
//           // если успешно, то
//           success: function (response) {
//               console.log("i'm clicked");
//
//               // if (response.is_taken == true) {
//               //     $('#id_username').removeClass('is-valid').addClass('is-invalid');
//               //     $('#id_username').after('<div class="invalid-feedback d-block" id="usernameError">This username is not available!</div>')
//               // }
//               // else {
//               //     $('#id_username').removeClass('is-invalid').addClass('is-valid');
//               //     $('#usernameError').remove();
//               //
//               // }
//           },
//           // если ошибка, то
//           error: function (response) {
//               // предупредим об ошибке
//               console.log(response.responseJSON.errors)
//           }
//       });
//       // return false;
//   });
// })


