// player btn size


$(window).resize(function(){
  console.log('resize called');
  var width = $(window).width();
  if(width < 765){
      $('.btn-playr').removeClass('fa-2x');
  }
  if(width >576){
    $('.btn-playr').addClass('fa-2x');
  }
})
.resize();

// hide host 

$(window).scroll(function(){
  if ($(this).scrollTop() > 50) {
     $('#dynamic').addClass('newClass');
  } else {
     $('#dynamic').removeClass('newClass');
  }
});


// slick
$(document).ready(function () {
  $(".responsive").slick({
    dots: true,
    infinite: false,
    speed: 300,
    slidesToShow: 4,
    slidesToScroll: 4,
    responsive: [
      {
        breakpoint: 1024,
        settings: {
          slidesToShow: 3,
          slidesToScroll: 3,
          infinite: true,
          dots: true,
        },
      },
      {
        breakpoint: 600,
        settings: {
          slidesToShow: 2,
          slidesToScroll: 2,
        },
      },
      {
        breakpoint: 480,
        settings: {
          slidesToShow: 2,
          slidesToScroll: 2,
        },
      },
      // You can unslick at a given breakpoint now by adding:
      // settings: "unslick"
      // instead of a settings object
    ],
  });
});
// tooltip

const tooltipTriggerList = document.querySelectorAll(
  '[data-bs-toggle="tooltip"]'
);
const tooltipList = [...tooltipTriggerList].map(
  (tooltipTriggerEl) => new bootstrap.Tooltip(tooltipTriggerEl)
);

// form design

const forms = document.getElementsByTagName("form");

if (forms) {
  let formArray = Array.from(forms);
  formArray.forEach((form) => {
    Array.from(form).forEach((elem) => {
      switch (elem.tagName.toLowerCase()) {
        case "input":
          switch (elem.type.toLowerCase()) {
            case "check":
              elem.classList.add("form-check-input");
              break;

            default:
              elem.classList.add("form-control");
              break;
          }
          break;

        case "textarea":
          elem.classList.add("form-control");
          break;

        default:
          break;
      }
    });
    let labels = form.querySelectorAll("label");
    Array.from(labels).forEach((label) => {
      label.classList.add("form-label");
    });
  });
}

// profile image

$("#profileImage").click(function (e) {
  $("#imageUpload").click();
  $("#profileimageupdate").submit();
});
function fasterPreview(uploader) {
  if (uploader.files && uploader.files[0]) {
    $("#profileImage").attr(
      "src",
      window.URL.createObjectURL(uploader.files[0])
    );
  }
}
$("#imageUpload").change(function () {
  fasterPreview(this);
});
$("#profileImage").click(function (e) {
  $("#imageUpload").click();
});
function fasterPreview(uploader) {
  if (uploader.files && uploader.files[0]) {
    $("#profileImage").attr(
      "src",
      window.URL.createObjectURL(uploader.files[0])
    );
  }
}
$("#imageUpload").change(function () {
  fasterPreview(this);
});

// player
const playerButton = document.querySelector("#player-button");
audio = document.querySelector("audio");
playIcon = `<i class="fa-regular btn-playr fa-circle-play fa-4x "></i>`;
pauseIcon = `<i class="fa-regular btn-playr fa-circle-pause fa-4x"></i>`;
playerButton.addEventListener("click", toggleAudio);
function audioEnded() {
  playerButton.innerHTML = playIcon;
}
audio.onended = audioEnded;

function toggleAudio() {
  if (audio.paused) {
    audio.play();
    playerButton.innerHTML = pauseIcon;
  } else {
    audio.pause();
    playerButton.innerHTML = playIcon;
  }
};

// add and remove favourite

const favouritebutton = document.querySelector("#addtofav");
audio = document.querySelector("audio");
unfavouriteIcon = `<i class="fa-regular fa-heart"></i>`;
unfavouriteIcon = `<i class="fa-solid fa-heart"></i>`;
favouritebutton.addEventListener("click", togglefav());

function togglefav() {
  if (audio.isFavourite) {
    audio.isnotFavourite();
    favouritebutton.innerHTML = unfavouriteIcon;
  } else {
    audio.isFavourite();
    favouritebutton.innerHTML = unfavouriteIcon;
  }
};
