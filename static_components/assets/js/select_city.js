// const findCityByCountry = () => {


// const country = document.querySelector('#id_country');
// const city = document.querySelector('#id_city');
//
// const selectValue = (sel) => sel.options[sel.selectedIndex].value;
// const findCityByCountryId = (id, select) => {
//   const options = Array.from(select.options).filter(v => v.value === id);
//   const result = []
//   options.map((el, index) => {
//     result[index].id = el.value;
//     result[index].name = el.text;
//   })
//   console.log(result);
//   return result;
// };
//
// country.addEventListener('select', (event) => {
//   const chosenCountry = selectValue(event.target);
//   if (chosenCountry === 'None') return;
//
//   const filteredCitiesList = findCityByCountryId(parseFloat(chosenCountry), city);
//   const options = Array.from(city.querySelectorAll('option:not(:first-child)'));
//   options.map((el) => el.remove());
//
//   filteredCitiesList.map((el) => {
//     let newOption = new Option(el.name, el.id);
//     console.log(newOption);
//     city.add(newOption, undefined);
//   })
// })
// }

// document.addEventListener('DOMContentLoaded', () => {
//     // findCityByCountry();
//     console.log(1111111111111);
//     console.log(document.getElementById("id_country"));
//     console.log(2222222222222);
//     console.log(document.getElementById("id_country").value === "None");
//     console.log(3333333333333);
//     if (document.getElementById("id_country").value === "None") {
//         document.getElementById('id_city').disabled = true;
//     } else {
//         document.getElementById('id_city').disabled = false;
//     }
// });