const $ = window.$;
$('#toggle_header').click(function () {
  $('header').toggleClass('red').toggleClass('green');
});
