

// slick

$(document).ready(function(){
    $('.responsive').slick({
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
              dots: true
            }
          },
          {
            breakpoint: 600,
            settings: {
              slidesToShow: 2,
              slidesToScroll: 2
            }
          },
          {
            breakpoint: 480,
            settings: {
              slidesToShow: 1,
              slidesToScroll: 1
            }
          }
          // You can unslick at a given breakpoint now by adding:
          // settings: "unslick"
          // instead of a settings object
        ]
      });
  });

  const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
  const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))
 
  

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

$("#profileImage").click(function(e) {
  $("#imageUpload").click();
  $("#profileimageupdate").submit();
});
function fasterPreview( uploader ) {
  if ( uploader.files && uploader.files[0] ){
        $('#profileImage').attr('src', 
           window.URL.createObjectURL(uploader.files[0]) );
  }
}
$("#imageUpload").change(function(){
  fasterPreview( this );
});
$("#profileImage").click(function(e) {
  $("#imageUpload").click();
});
function fasterPreview( uploader ) {
  if ( uploader.files && uploader.files[0] ){
        $('#profileImage').attr('src', 
           window.URL.createObjectURL(uploader.files[0]) );
  }
}
$("#imageUpload").change(function(){
  fasterPreview( this );
});


// player
const playerButton = document.querySelector('#player-button'),
      audio = document.querySelector('audio'),
      playIcon = `
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="#3D3132">
    <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM9.555 7.168A1 1 0 008 8v4a1 1 0 001.555.832l3-2a1 1 0 000-1.664l-3-2z" clip-rule="evenodd" />
  </svg>
      `,
      pauseIcon = `
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="#3D3132">
  <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zM7 8a1 1 0 012 0v4a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v4a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd" />
</svg>
      `; 
playerButton.addEventListener('click', toggleAudio);
function audioEnded () {
  playerButton.innerHTML = playIcon;
}
audio.onended = audioEnded;
    
function toggleAudio () {
  if (audio.paused) {
    audio.play();
    playerButton.innerHTML = pauseIcon;
  } else {
    audio.pause();
    playerButton.innerHTML = playIcon;
  }
};









