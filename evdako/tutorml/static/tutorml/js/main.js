let swiper_slider = new Swiper(".slider", {
  spaceBetween: 20,
  speed: 600,
  centeredSlides: true,
  loop: true,
  autoplay: {
    delay: 10000,
    disableOnInteraction: false,
  },
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
});

let swiper_reviews = new Swiper(".reviews", {
  speed: 600,
  centeredSlides: true,
  loop: true,
  // effect: "cards",
  effect: "coverflow",
  coverflowEffect: {
    slideShadows: false,
    rotate: 30,
    stretch: 0,
    depth: 400,
    modifier: 1
  },
  autoplay: {
    delay: 55000,
    disableOnInteraction: false,
  },
  breakpoints: {
    1064: {
      slidesPerView: 3,
    },
  }
});

$(window).scroll(function () {
  if ($(window).scrollTop() > 200) {
    $('#scroll-up').addClass("scrollup_show");
  } else {
    $('#scroll-up').removeClass("scrollup_show");
  }
});

if ($(".nav_toggle")) {
  $(".nav_toggle").click(function () {
    $(".nav_menu").addClass("show_menu");
    $(".nav_close").show();
    $(".nav_toggle").hide();
  })
}
if ($(".nav_close")) {
  $(".nav_close").click(function () {
    $(".nav_menu").removeClass("show_menu");
    $(".nav_close").hide();
    $(".nav_toggle").show();
  })
}

function subscribe() {
  var subscribe_form = document.forms.subscribe;
  var email = subscribe_form.email;
  var news = subscribe_form.news.checked;
  var articles = subscribe_form.articles.checked;
  var comments = subscribe_form.comments.checked;
  var result = "";

  if (!email.value || !email.value.includes("@")) alert('Неправильно указана почта!');
  else if (!news && !articles && !comments) alert("Вы ничего не выбрали!");
  else {
    result = "На почту '" + email.value + "' будут приходить: \n";
    if (news) result += "Новости о продуктах\n";
    if (articles) result += "Новые статьи\n";
    if (comments) result += "Комментарии к Вашим статьям";
    alert(result);
  }
}

function login() {
  var login_form = document.forms.login;
  var username = login_form.username.value;
  var password = login_form.password.value;
  var remember = login_form.remember.checked;

  if (!username || !password) alert("Введите имя пользователя и пароль!");
  else {
    alert("Вы успешно вошли!");
    window.close();
    window.open("index.html");
  }
}

function register() {
  var register_form = document.forms.register;
  var username = register_form.username.value;
  var email = register_form.email.value;
  var password = register_form.password.value;
  var password2 = register_form.password2.value;

  if (!username || !email || !password || !password2) alert("Заполните все поля!");
  else if (!email.includes("@")) alert('Неправильно указана почта!');
  else if (password != password2) alert("Пароли не совпадают!");
  else {
    alert("Пользователь '" + username + "' с почтой '" + email + "' успешно зарегистрирован!");
    window.close();
    window.open("index.html");
  }
}