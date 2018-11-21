(function ($) {

    "use strict";
    var Win_width_ = window.innerWidth;
    var $window = $(window),
        $doc = $(document),
        $owl1 = $('#main-slider'),
        $owl2 = $('.vehicle-slider'),
        $inputs = $('input[type="text"],input[type="email"],input[type="number"],textarea,select'),
        $owl3 = $('#package-box'),
        $owl4 = $('#feeds-slider'),
        $owl5 = $('.drivers-portfolio'),
        $owl6 = $('.partners'),
		$owl7 = $('#main-slider_v2'),
		$owl8 = $('#blog-slider'),
        $menutog = $('.navbar-toggle'),
        $scrolltop = $('.scrolltop')

    var hide_element = $('header,footer,section,nav')
    hide_element.addClass('hide')
    // Run On Page Load
    $window.on("load", function () {

        //******************* PAGE LOADER ******************//
        $('body').removeClass('no-scroll');
        hide_element.removeClass('hide')
        $('#loader-wrapper').fadeOut(600, function () {
            $(this).remove();
        });


        //******************* ADD ACTIVE CLASS ON CURRENT PAGE ******************//
        var pgurl = window.location.href.substr(window.location.href.lastIndexOf("/") + 1);
        $("header .navbar-nav>li a").each(function () {
            if ($(this).attr("href") == pgurl || $(this).attr("href") == '')
                $(this).parent('li').addClass('active');
            $(this).closest('li.dropdown').addClass('active');
            $(this).click(function () {
                var li_ = $(this).parent('li')
                li_.addClass('active')
                $('header .navbar-nav li').not(li_).removeClass('active')
            })
        })

        //******************* ADD BOX-SHADOW ON INPUTS AND SELECT ******************//
        $inputs.each(function () {
            var ths = $(this)
            ths.click(function () {
                $(this).closest('.input-group').addClass('input-shadow');
            }).blur(function () {
                $('.input-group').removeClass('input-shadow');
            })
        })
        $('.bootstrap-select').click(function () {
            $(this).closest('.input-group').addClass('input-shadow');

        })

        //******************* TRANSITION EFFECT IN OWL-CAROUSEL CONTENT ******************//
        function wowOwl(elm) {
            elm.find('.owl-item').each(function () {
                $(this).hasClass('active') ?
                    $(this).find('*[data-animation]').each(function () {
                        var th = $(this)
                        var cls = th.attr('data-animation')
                        var del = th.attr('data-animation-delay')
                        th.css({
                            "animation-delay": del
                        }).addClass(cls)
                    }) :
                    $(this).find('*[data-animation]').each(function () {
                        var th = $(this)
                        var cls = th.attr('data-animation')
                        th.removeClass(cls)
                    })
            })
        }

        //******************* HOME PAGE OWL-CAROUSEL ******************//
        $owl1.owlCarousel({
            items: 1,
            loop: true,
            autoplay: true,
            autoplayTimeout: 5000,
            autoplayHoverPause: true,
            nav: false,
            dots: true,
            navText: ['<i class="fa fa-long-arrow-left"></i>', '<i class="fa fa-long-arrow-right"></i>'],
            navContainerClass: 'owl-nav',
            dotsClass: 'owl-dots counter',
            responsive: {
                0: {
                    nav: false,
                    dots: false,
                },
                750: {
                    nav: true,
                    dots: false,
                },
                1000: {
                    nav: false,
                    dots: true,
                }
            },
            onChanged: function (event) {
                setTimeout(function () {
                    wowOwl($owl1);
                }, 0);
            }
        })




        //******************* OWL-CAROUSEL VEHICLE SLIDER ******************//
        $owl2.owlCarousel({
            items: 4,
            margin: 30,
            loop: false,
            autoplay: true,
            autoplayTimeout: 5000,
            autoplayHoverPause: true,
            nav: false,
            dots: true,
            navText: ['<i class="fa fa-long-arrow-left"></i>', '<i class="fa fa-long-arrow-right"></i>'],
            navContainerClass: 'owl-nav',
            dotsClass: 'owl-dots counter',
            responsive: {
                0: {
                    items: 1,
                    dots: false,
                },
                480: {
                    items: 1,
                    dots: false,
                },
                768: {
                    items: 2,
                    nav: true,
                    dots: false,

                },
                1000: {
                    items: 3,
                    margin: 10,
                },
                1200: {
                    items: 4,
                    margin: 10,
                }
            }
        })

        //******************* OWL-CAROUSEL PACKAGE SLIDER ******************//
        $owl3.owlCarousel({
            items: 3,
            margin: 30,
            loop: false,
            autoplay: true,
            autoplayTimeout: 5000,
            autoplayHoverPause: true,
            nav: true,
            dots: false,
            navContainerClass: 'owl-nav small-nav',
            navText: ['<i class="fa fa-long-arrow-left"></i>', '<i class="fa fa-long-arrow-right"></i>'],
            responsive: {
                0: {
                    items: 1,
                },
                768: {
                    items: 2,
                },
                1000: {
                    items: 2,
                    margin: 10,
                    loop: false,

                },
                1200: {
                    items: 3,
                    margin: 10,
                }
            }
        })


        //******************* OWL-CAROUSEL DRIVERS PORTFOLIO SLIDER ******************//
        $owl5.owlCarousel({
            items: 3,
            margin: 50,
            loop: false,
            autoplay: false,
            autoplayTimeout: 5000,
            autoplayHoverPause: true,
            nav: false,
            dots: true,
            navContainerClass: 'owl-nav small-nav',
            navText: ['<i class="fa fa-long-arrow-left"></i>', '<i class="fa fa-long-arrow-right"></i>'],
            dotsClass: 'owl-dots counter small-counter',
            responsive: {
                0: {
                    items: 1,
                },
                768: {
                    items: 2,
                },
                1000: {
                    items: 2,

                    loop: false,

                },
                1200: {
                    items: 3,

                }
            }
        })

        //******************* OWL-CAROUSEL DRIVERS P  SLIDER ******************//
        $owl6.owlCarousel({
            items: 5,
            margin: 10,
            loop: true,
            autoplay: true,
            autoplayTimeout: 4000,
            autoplayHoverPause: true,
            nav: false,
            dots: false,
            navContainerClass: 'owl-nav small-nav',
            navText: ['<i class="fa fa-long-arrow-left"></i>', '<i class="fa fa-long-arrow-right"></i>'],
            dotsClass: 'owl-dots counter small-counter',
            responsive: {
                0: {
                    items: 1,
                },
                768: {
                    items: 2,
                },
                1000: {
                    items: 2,
                },
                1200: {
                    items: 4,
                }
            }
        })


//******************* HOME PAGE OWL-CAROUSEL ******************//
        $owl7.owlCarousel({
            items: 1,
            loop: true,
            autoplay: false,
            autoplayTimeout: 5000,
            autoplayHoverPause: true,
            nav: false,
            dots: true,
            navText: ['<i class="fa fa-long-arrow-left"></i>', '<i class="fa fa-long-arrow-right"></i>'],
            navContainerClass: 'owl-nav',
            dotsClass: 'owl-dots counter white pos_bottom',
            responsive: {
                0: {
                    nav: false,
                    dots: false,
                },
                750: {
                    nav: true,
                    dots: false,
                },
                1000: {
                    nav: false,
                    dots: true,
                }
            }

        })
//******************* LATEST BLOG OWL-CAROUSEL ******************//
		  $owl8.owlCarousel({
            items: 3,
            loop: true,
			margin:30,
            autoplay: true,
            autoplayTimeout: 5000,
            autoplayHoverPause: true,
            nav: true,
            dots: false,
            navContainerClass: 'owl-nav small-nav',
            navText: ['<i class="fa fa-long-arrow-left"></i>', '<i class="fa fa-long-arrow-right"></i>'],
            dotsClass: 'owl-dots',
            responsive: {
                0: {

                  items:1
                },
                750: {

                    items:2
                },
                1000: {


                }
            },

        })

        //******************* OWL-CAROUSEL PASSANGER FEED SLIDER ******************//
        $owl4.owlCarousel({
            items: 1,
            loop: false,
            autoplay: true,
            autoplayTimeout: 5000,
            autoplayHoverPause: true,
            nav: false,
            dots: true,
            navText: ['<i class="fa fa-long-arrow-left"></i>', '<i class="fa fa-long-arrow-right"></i>'],
            navContainerClass: 'owl-nav',
            dotsClass: 'owl-dots counter small-counter',
        })

        //******************* GOOGLE GEOCOMPLETE ******************//
        $(".placepicker").geocomplete();


        //******************* VEHICLE-INFO HOVER EFFECT ******************//
        if (Win_width_ > 767) {
            $('.vehicle-info').each(function () {
                var th = $(this)
                var elments = th.find('.dri-thumb, .booknow');

                th.mouseover(function () {
                    th.addClass('active');
                    $('.vehicle-info').not(th).removeClass('active');
                    elments.addClass('bounceIn animated');
                    $('.dri-thumb, .booknow').not(elments).removeClass('bounceIn animated');
                })
            })
        }


        //******************* TAB TRANSITION OPEN EFFECT ******************//
        $('.nav-tabs').each(function () {
            var status_ = $(this).data('animation');
            var animationCls = $(this).data('animation-class');
            var btn_ = $('li a', this);

            if (status_) {
                btn_.click(function () {
                    var elm = $(this);
                    var target_ = elm.attr('href');
                    if ($(target_).hasClass('tab-pane')) {
                        $(target_).addClass('animated' + " " + animationCls)
                        $('.tab-pane').not(target_).removeClass('animated' + " " + animationCls)
                    }
                });
            }
        })

        //******************* BOOK CAB FORM VALIDATION ******************//
         $("#form-book-vehicle").validate({

            debug: false,
            errorClass: "error",
            errorElement: "span",
            rules: {
                vehicle: "required",
                passangers: "required",
                pkup_location: "required",
                pkup_date: "required",
                droff_location: "required",
                email: {
                    required: true,
                    email: true
                }

            },
            messages: {
				vehicle: "Please Select Vehicle",
				passangers: "Please Select Vehicle",
				pkup_location: "Please Fill Pickup Location",
				pkup_date: "Please Fill Pickup Date",
				droff_location: "Please Fill Drop Off Location",
                email: "Requried valid email address"

            },
            highlight: function (element, errorClass) {
                $(element).removeClass(errorClass);
            },
			 submitHandler: function (form) {
                $.ajax({
                    url: form.action,
                    type: form.method,
                    data: $(form).serialize(),
                    success: function (response) {
                        $(form).after('<div class="alert alert-success"><strong>Success!</strong> Your Cab has been successfully Booked! </div>')
						 $('#form-book-vehicle')[0].reset();

                        setTimeout(function () {
                            $(".alert.alert-success").fadeOut(400);
                        }, 5000)
                    }

                });
            }

        });



        //******************* FOOTER MESSAGE FORM VALIDATION ******************//
        $("#message-form").validate({
            debug: false,
            errorClass: "error",
            errorElement: "span",
            rules: {
                name: {
                    required: true,
                    minlength: 2
                },
                email: {
                    required: true,
                    email: true
                },
                typemessage: {
                    required: true,
                    maxlength: 250
                }
            },
            messages: {
                name: {
                    required: "Please enter a Name",
                    minlength: "Your Name must consist of at least 2 characters"
                },
                email: "Please enter a valid email address",
                typemessage: {
                    required: "Please Type a Message",
                    maxlength: "Message characters Mammum 250 characters"
                },
            },
            highlight: function (element, errorClass) {
                $(element).removeClass(errorClass);
            },
            submitHandler: function (form) {
                $.ajax({
                    url: form.action,
                    type: form.method,
                    data: $(form).serialize(),
                    success: function (response) {
                        $(form).after('<div class="alert alert-success"><strong>Success!</strong> Your Message has been successfully submited ! </div>')

						$('#message-form')[0].reset();
                        setTimeout(function () {
                            $(".alert.alert-success").fadeOut(400);
                        }, 100)
                    }

                });
            }
        });


        //******************* BOOK FORM PACKAGE ACTIVE STATUS ******************//
        $('.pkg-item').each(function () {
            var th = $(this);
            var inp = th.find('input:radio');
            th.click(function () {
                th.find('input:radio').prop("checked", true)
                th.addClass('active')
                $('.pkg-item').not(th).removeClass('active');
            })
        })



        //******************* GOOGLE MAP  ******************//
        var s = $("#gmap , .gmap");
        var stylez = [{
            featureType: "all",
            elementType: "all",
            stylers: [{
                saturation: -100
            }]
            }];

        var mapType = new google.maps.StyledMapType(stylez, {
            name: "Grayscale"
        });
        if (s.length > 0) {
            s.each(function () {
                var e = $(this);
                var t = e.attr("data-address") || "Footscray VIC 3011 Australia";
                var mapmarkerIcon = e.data('marker-icon')
                e.gmap3({
                        address: t,
                        zoom: 18,
                        mapTypeId: google.maps.MapTypeId.ROADMAP,
                        mapTypeControlOptions: {
                            mapTypeIds: [google.maps.MapTypeId.ROADMAP, "grayscale", ]
                        }
                    })
                    .marker(function (map) {
                        return {
                            position: map.getCenter(),
                            icon: mapmarkerIcon,
                            animation: google.maps.Animation.DROP,
                        };
                    })
                    .styledmaptype(

                        "grayscale",

                     [{
                            featureType: "all",
                            stylers: [
                             //  { hue: "#000000" },
                                {
                                    saturation: -100
                             },
                             // { lightness: -20 },
                                {
                                    gamma: .9
                             },
                         ]
                     }],

                        {
                            name: "Style 1"
                        }
                    )
            })
        }


        //******************* GO TO TOP SCROLL  ******************//
       var scrollTrigger = 200, // px
            backToTop = function () {
                var scrollTop = $(window).scrollTop();
                if (scrollTop > scrollTrigger) {
					if($('header').data('sticky') == true)
					{
						$('header').addClass('sticky-header')
					}

                    $scrolltop.addClass('animated bounceIn');
                } else {

					$('header').removeClass('sticky-header')

                    $scrolltop.removeClass('animated bounceIn');
                }
            };

        $(window).on('scroll', function () {
            backToTop();
        });
        $scrolltop.on('click', function (e) {
            e.preventDefault();
            $('html,body').animate({
                scrollTop: 0
            }, 700);
        });


        //******************* SMOOTH SCROLL #ID LINKS ******************//
        $('header .navbar-nav a[href*="#"]')
            .click(function (event) {
                if (
                    location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') &&
                    location.hostname == this.hostname
                ) {
                    // Figure out element to scroll to
                    var target = $(this.hash);
                    target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
                    // Does a scroll target exist?
                    if (target.length) {
                        // Only prevent default if animation is actually gonna happen
                        event.preventDefault();
                        $('html, body').animate({
                            scrollTop: target.offset().top
                        }, 1000, function () {
                            // Callback after animation
                            // Must change focus!
                            var $target = $(target);
                            $target.focus();
                            if ($target.is(":focus")) { // Checking if the target was focused
                                return false;
                            } else {
                                $target.attr('tabindex', '-1'); // Adding tabindex for elements not focusable
                                $target.focus(); // Set focus again
                            };
                        });
                    }
                }
            });

        //******************* ACTIVE SIDEBAR ******************//
        if (Win_width_ < 1600) {

            $menutog.click(function () {
                $(this).toggleClass('close')
                $('header .navbar-collapse').toggleClass('active')
                $('body').toggleClass('sidebar-active')
                var li = $('header .navbar-nav li');

                var i;

                if ($(this).hasClass('close')) {
                    for (i = 0; i <= li.length; i++) {
                        li.eq(i).attr('style', ['animation-delay:0.' + i + 's;-webkit-animation-delay:0.' + i + 's']).addClass('animated slideInRight');
                    }
                } else {
                    $('header .navbar-nav li').removeAttr('style').removeClass('animated slideInRight')
                }

            })

        }
        //*******************  VERTICAL CENTER ELEMENT ******************//

        function virtcal_center(target_, elm) {
            // target_ is from center which element eg. body
            // elm is which element you want center
            // for example -> virtcal_center($('body'),$('div'));

            var height_ = $(target_).height() / 2;
            var elm_height_ = $(elm).height() / 2;

            var result = height_ - elm_height_;
            $(elm).css({
                top: result
            })
        }

        virtcal_center($('.notfound'), $('.notfound-box'));

		//************** CHANGE DIRECTION FUNCTION ***************//

		$('.directions_select').on('change',function(){

			var val_ = $(this).val();

			if(val_ == "di_return")
			{
				$('.drop_of_date').removeAttr('style').addClass('animated bounceId').removeClass('hide');;
				$('.name_selectr').removeClass('col-md-12').addClass('col-md-6');

			}
			else if(val_ == "di_oneway"){
				$('.drop_of_date').css('display','none').addClass('hide');
				$('.name_selectr').removeClass('col-md-6').addClass('col-md-12');
			}
		})

        //******************* VERTICAL CENTER ELEMENT ******************//

			//***************** ENABLE GET ROUTE BUTTON *********************//
			$('.placepicker').on('blur', function(){

				if($('#droff_location').val() !="" && $('#pkup_location').val() !="" )
				{
					$('.routeInfobtn').removeAttr('disabled')
					Getdirection();
				}
				else{$('.routeInfobtn').attr('disabled','disabled')}
			})
        //******************* WOW ANIMATION ******************//
        new WOW().init()

    })
})(jQuery)
