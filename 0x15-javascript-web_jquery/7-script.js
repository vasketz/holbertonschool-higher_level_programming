const $ = window.$;
const url = 'https://swapi-api.hbtn.io/api/people/15/?format=json';
$.ajax({
  type: 'GET',
  url: url,
  success: function (response) {
    $('#character').text(response.name);
  }
});
