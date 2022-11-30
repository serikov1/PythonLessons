const btn = document.querySelector("#change_theme");
btn.addEventListener("click", function () {
  document.body.classList.toggle("dark-theme");
  let date = new Date(Date.now() + 86400e3);
  date = date.toUTCString();
  if ( document.cookie.match(/theme=(.+?)(;|$)/)[1] === 'light'){
      document.cookie = "theme=dark; expires=" + date;
      console.log(document.cookie)
  }
  else{
      document.cookie = "theme=light; expires=" + date;
      console.log(document.cookie)
  }
});
if ( document.cookie.match(/theme=(.+?)(;|$)/)[1] === 'dark') {
   document.body.classList.toggle("dark-theme");
}
