const $ = window.$;
const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
$.ajax({
  type: 'GET',
  url: url,
  success: function (response) {
    for (const movie in response.results) { $('#list_movies').append('<li>' + response.results[movie].title + '</li>'); }
  }
});
