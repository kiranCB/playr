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
