
// Enable tooltips everywhere
var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
  return new bootstrap.Tooltip(tooltipTriggerEl)
})

function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      var cookies = document.cookie.split(';');
      for (var i = 0; i < cookies.length; i++) {
          var cookie = cookies[i].trim();
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}

function csrfSafeMethod(method) {
  // these HTTP methods do not require CSRF protection
  return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

function makeRequest(url, method, body={}) {
  if (csrfSafeMethod(method)) {
    var response = fetch(
      url,
      {
        method: method,
        headers: {
          "Content-Type": "application/json",
        }
      }
    )
  } else {
    var response = fetch(
      url,
      {
        body: body,
        method: method,
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": getCookie('csrftoken')  // Get the CSRF token
        }
      }
    )
  }
  return response;
}