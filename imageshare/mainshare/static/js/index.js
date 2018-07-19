$(document).on('click', 'a[href^="#"]', function (event) {
    event.preventDefault();

    $('html, body').animate({
        scrollTop: $($.attr(this, 'href')).offset().top - 50
    }, 500);
});
showinfo = (i)=>{
  dict=eval(i)
  $('#imageimage').attr('src',dict.image);
  $('#imagedescription').text(dict.desc);
  $('#imagetitle').text(dict.name);
  $("#imagelink").val(window.location.origin+'/#'+dict.id);
  $("#ImageModal").modal('show');
}
copyaction = ()=>{
document.getElementById("imagelink").select();
document.execCommand("Copy");
}
