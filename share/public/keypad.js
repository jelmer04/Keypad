$(document).ready(function() {

var url = "../../generator";

var connected_state = true;
var connected_poll;

function done() {
  console.log("Sent!");
  if (connected_state == false) {
    connected();
  }
  connected_state = true;
}

function fail() {
  console.log("Failed!");
  if (connected_state == true) {
    disconnected();
  }
  connected_state = false;
}

function connected () {
  hide_bar();
  $("#connected").fadeIn();
  connected_poll = setTimeout(hide_bar, 2000);
};

function disconnected () {
  clearTimeout(connected_poll);
  hide_bar();
  $("#disconnected").fadeIn();
};

function hide_bar() {
  $(".bar").fadeOut();
};

$(".bar").hide()
connected();

$("#retry").click(function(e) {
  $.ajax({
    type: "GET",
    url: url
  })
  .done(done).fail(fail);
  e.preventDefault();
});

$("#button-clear").click(function(e) {
  $.ajax({
    type: "PUT",
    url: url,
    data: {"key_index": "1"}
  })
  .done(done).fail(fail);
  e.preventDefault();
});

$("#button-equals").click(function(e) {
  $.ajax({
    type: "PUT",
    url: url,
    data: {"key_index": "2"}
  })
  .done(done).fail(fail);
  e.preventDefault();
});

$("#button-slash").click(function(e) {
  $.ajax({
    type: "PUT",
    url: url,
    data: {"key_index": "3"}
  })
  .done(done).fail(fail);
  e.preventDefault();
});

$("#button-star").click(function(e) {
  $.ajax({
    type: "PUT",
    url: url,
    data: {"key_index": "4"}
  })
  .done(done).fail(fail);
  e.preventDefault();
});

$("#button-7").click(function(e) {
  $.ajax({
    type: "PUT",
    url: url,
    data: {"key_index": "5"}
  })
  .done(done).fail(fail);
  e.preventDefault();
});

$("#button-8").click(function(e) {
  $.ajax({
    type: "PUT",
    url: url,
    data: {"key_index": "6"}
  })
  .done(done).fail(fail);
  e.preventDefault();
});

$("#button-9").click(function(e) {
  $.ajax({
    type: "PUT",
    url: url,
    data: {"key_index": "7"}
  })
  .done(done).fail(fail);
  e.preventDefault();
});

$("#button-minus").click(function(e) {
  $.ajax({
    type: "PUT",
    url: url,
    data: {"key_index": "8"}
  })
  .done(done).fail(fail);
  e.preventDefault();
});

$("#button-4").click(function(e) {
  $.ajax({
    type: "PUT",
    url: url,
    data: {"key_index": "9"}
  })
  .done(done).fail(fail);
  e.preventDefault();
});

$("#button-5").click(function(e) {
  $.ajax({
    type: "PUT",
    url: url,
    data: {"key_index": "10"}
  })
  .done(done).fail(fail);
  e.preventDefault();
});

$("#button-6").click(function(e) {
  $.ajax({
    type: "PUT",
    url: url,
    data: {"key_index": "11"}
  })
  .done(done).fail(fail);
  e.preventDefault();
});

$("#button-plus").click(function(e) {
  $.ajax({
    type: "PUT",
    url: url,
    data: {"key_index": "12"}
  })
  .done(done).fail(fail);
  e.preventDefault();
});

$("#button-1").click(function(e) {
  $.ajax({
    type: "PUT",
    url: url,
    data: {"key_index": "13"}
  })
  .done(done).fail(fail);
  e.preventDefault();
});


$("#button-2").click(function(e) {
  $.ajax({
    type: "PUT",
    url: url,
    data: {"key_index": "14"}
  })
  .done(done).fail(fail);
  e.preventDefault();
});


$("#button-3").click(function(e) {
  $.ajax({
    type: "PUT",
    url: url,
    data: {"key_index": "15"}
  })
  .done(done).fail(fail);
  e.preventDefault();
});


$("#button-enter").click(function(e) {
  $.ajax({
    type: "PUT",
    url: url,
    data: {"key_index": "16"}
  })
  .done(done).fail(fail);
  e.preventDefault();
});


$("#button-0").click(function(e) {
  $.ajax({
    type: "PUT",
    url: url,
    data: {"key_index": "17"}
  })
  .done(done).fail(fail);
  e.preventDefault();
});


$("#button-dot").click(function(e) {
  $.ajax({
    type: "PUT",
    url: url,
    data: {"key_index": "18"}
  })
  .done(done).fail(fail);
  e.preventDefault();
});


});
