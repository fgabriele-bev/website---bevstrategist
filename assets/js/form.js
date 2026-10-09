/* Contact form: sends the message to Formspree without leaving the page.
   Without JavaScript the form still works as a normal POST. No cookies, no tracking. */
(function () {
  var form = document.querySelector('.contact-form');
  if (!form || !window.fetch || !window.FormData) return;
  var status = form.querySelector('.form-status');
  var button = form.querySelector('button[type="submit"]');
  form.addEventListener('submit', function (event) {
    event.preventDefault();
    button.disabled = true;
    status.className = 'form-status wide';
    status.textContent = '';
    fetch(form.action, { method: 'POST', body: new FormData(form), headers: { Accept: 'application/json' } })
      .then(function (response) {
        if (!response.ok) throw new Error('send failed');
        form.reset();
        status.textContent = form.getAttribute('data-ok');
        status.className = 'form-status wide is-ok';
      })
      .catch(function () {
        status.textContent = form.getAttribute('data-fail');
        status.className = 'form-status wide is-fail';
      })
      .then(function () { button.disabled = false; });
  });
})();
