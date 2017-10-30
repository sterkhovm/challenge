$( document ).ready(function() {

    $('.carousel').carousel({
        interval: 5000
    });

    $("#b5-carousel").owlCarousel({
        items : 3,
        navigation: true,
        navigationText : ["",""]
    });

    function afterAction() {
        $('.b8_oc_cur').text(this.owl.currentItem+1)
        $('.b8_oc_last').text(this.owl.owlItems.length)
    }

    $("#b8-carousel, #b9-carousel").owlCarousel({
        navigation : true,
        slideSpeed : 1000,
        paginationSpeed : 400,
        singleItem:true,
        navigationText : ["",""],
        afterAction : afterAction
    });

    $('.h_call, .cmp_link, .b7_ling, .b10_link, .b7_item, .pmr_choose, .kurs_btn, .predmet_head_btn').on('click', function(e){
        e.stopPropagation();
        e.preventDefault();
        $('#modal1').bPopup({
            modalCLose: true,
            closeClass:'close1'
        });
    });

    $('.h_pay').on('click', function(e){
        e.stopPropagation();
        e.preventDefault();
        $('#kassa_modal').bPopup({
            modalCLose: true,
            closeClass:'close1'
        });
    });

    $('.slide_btn').on('click', function(e){
        e.stopPropagation();
        e.preventDefault();
        $('#slide-modal'+'-'+this.id).bPopup({
            modalCLose: true,
            closeClass:'close1'
        });
    });

    $('.mff_phone').mask("+7 (999) 999-99-99");

    $('.ocenter_expandeble_click').on('click', function(){
        $(this).parent().toggleClass('open');
    })

    $('.sc_item').on('click', function(){
        $(this).toggleClass('open');
    })

    $('.sc_item_dd span').on('click', function(){
        $(this).parent().parent().find('.sc_item_main').text($(this).html());
    })

    $('.scmi_delete').on('click', function(){
        $(this).parent().remove();
    })

    // $('#modal2').bPopup({
    //     modalCLose: true,
    //     closeClass:'close1'
    //   });
    //
    //    $('.modal3').bPopup({
    //
    //     modalCLose: true,
    //     closeClass:'close1'
    //   });

    $('.show_modal3').on('click', function(e){
        e.stopPropagation();
        e.preventDefault();
        var modal = $('.modal2-'+this.id);
        // modal.addClass();
        modal.bPopup({
            modalCLose: true,
            closeClass:'close1',
            follow: [false, false]
        });
    });


    $('.sc_add').on('click',function(){
        var dc = '';
        if($(this).parent().find('.sc_skurs1').find('.sc_item_main').text() == "Стандартный курс") {
            dc ='Станд. курс';
        } else if($(this).parent().find('.sc_skurs1').find('.sc_item_main').text() == "Интенсивный курс") {
            dc ='Интенс. курс';
        } else if($(this).parent().find('.sc_skurs1').find('.sc_item_main').text() == "Спецкурс") {
            dc ='Спецкурс';
        } else if($(this).parent().find('.sc_skurs1').find('.sc_item_main').text() == "Индивидуальный курс") {
            dc ='Индивид. курс';
        }

        $('.sc_mid').append('<div class="sc_mid_item"><div class="scmi_delete" onClick="$(this).parent().remove();"><img src="img/delete.png"></div><span class="scmi_s1">'+$(this).parent().find('.sc_kurs').find('.sc_item_main').text()+'</span><span class="scmi_s2">'+$(this).parent().find('.sc_skurs').find('.sc_item_main').text()+'</span><span class="scmi_s3">'+dc+'</span><span class="scmi_s4">'+$(this).parent().find('.sc_skurs2').find('.sc_item_main').text()+'</span><span class="scmi_s5">6900 р. / мес.</span><span class="scmi_s6">55 200 р. / 32 нед.</span>'+'</div>')
    })

    //         <div class="sc_mid_item">
    //     <div class="scmi_delete"><img src="img/delete.png"></div>
    //     <span class="scmi_s1">Математика</span>
    //     <span class="scmi_s2">ЕГЭ</span>
    //     <span class="scmi_s3">Стандарт. курс</span>
    //     <span class="scmi_s4">Помесячно</span>
    //     <span class="scmi_s5">6900 р. / мес.</span>
    //     <span class="scmi_s6">55 200 р. / 32 нед.</span>
    // </div>

});