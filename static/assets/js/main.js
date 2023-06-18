$(document).ready(function () {
    // hero image slider
    $('.hero-image').slick({
        infinite: true,
        slidesToShow: 1,
        slidesToScroll: 1,
        prevArrow: "<button type='button' class='slick-prev pull-left'><i class='fa-solid fa-angle-left'></i></button>",
        nextArrow: "<button type='button' class='slick-next pull-right'><i class='fa-solid fa-angle-right'></i></button>"
    });


    $('.feedback-slider').slick({
        autoplay: true,
        autoplaySpeed: 8000,
        infinite: true,
        slidesToShow: 3,
        slidesToScroll: 1,
        arrows: false,
        dots: true,
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
                breakpoint: 780,
                settings: {
                    slidesToShow: 2,
                    slidesToScroll: 2
                }
            },
            {
                breakpoint: 490,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1
                }
            }
        ]

    });

    // Gets the video src from the data-src on each button

    var $videoSrc = '';
    $('.video-btn').click(function () {
        $videoSrc = $(this).attr("data-bs-src");
    });

    // when the modal is opened autoplay it  
    $('#videoModal').on('shown.bs.modal', function (e) {
        $("#modal-preloader").show().delay(5000).fadeOut(100);
        $("#video").attr('src', $videoSrc + "?autoplay=1&amp;modestbranding=1&amp;showinfo=0");
        $('#video_modal_close').show();

    })

    // stop playing the youtube video when I close the modal
    $('#videoModal').on('hidden.bs.modal', function (e) {
        $("#video").attr('src', '');
    })



    // counter && add plus sign
    var count = $('.counter').counterUp({
        delay: 10,
        time: 1000
    });

    function addPlus() {
        $('.plus').html('+');
    }

    $.when.apply(this, count).done(function () {
        setTimeout(addPlus, 1400);
    });

    $('#menu_btn').click(function (e) {
        e.preventDefault();
        $('.phone-menu').addClass('show');
        $('#menu_overlay').addClass('menu-overlay');
    });

    $('#menu_close').click(function (e) {
        e.preventDefault();
        $('.phone-menu').removeClass('show');
        $('#menu_overlay').removeClass('menu-overlay');
    });
    $('#menu_overlay').click(function (e) {
        e.preventDefault();
        $('.phone-menu').removeClass('show');
        $('#menu_overlay').removeClass('menu-overlay');

        console.log('ok')
    });
});