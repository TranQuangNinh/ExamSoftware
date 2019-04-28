$(document).ready(function () {
    // setTimeout(function () {
    //     $('.show_errors').fadeOut();
    // }, 2000);
    $('.show_errors').delay(2000).fadeOut();

    $('.page_link').on('click', function (e) {
        e.preventDefault();
        window.location = $(this).attr('href');
    })
})