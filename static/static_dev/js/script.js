
$(document).ready(function() {

        var form = $('.formBuyProduct');
        var form_for_all_pages = $('.formsfor');
        function basketUpdating(product_id, numb, is_delete){
            var data  = {};
            data.product_id = product_id;
            data.numb = numb;
            var csrf_token = $('.formsfor [name="csrfmiddlewaretoken"]').val();
            data.csrfmiddlewaretoken = csrf_token;
            var url = form.attr("action");
            if (is_delete){
                data["is_delete"] = true;
                url = form_for_all_pages.attr("action");
            }
            $.ajax({
               url: url,
               type: "POST",
               data: data,
               cache: true,
               success: function (data) {
                   console.log(data.products_total_nmb);
                   console.log("dtutu");
                   if (data.products_total_nmb || data.products_total_nmb == 0){
                        $('#basket_total_nmb').text("("+data.products_total_nmb+")");
                        $('#table-basket tbody').html("");
                        $.each(data.products, function(k, v){
                            $('#table-basket').append('<tr><td>'+v.product_name+'</ td><td>'+v.numb+' шт.</td><td> по '+v.price_per_item+' руб.</ td><td><a class="delete-item" href="#" data-product_id="'+v.id+'">X</a></td></ tr>');
                        });
                    };
               },
               error: function(){
                   console.log("error");
               },
            });
        };

        form.on('submit', function(e){
            e.preventDefault();
            var clikedForm = $(this).find('.inBuyProduct');
            var numb = clikedForm.val();
            var in_buy_btn = $(this).find('.inBuyBtn');
            var product_name = in_buy_btn.data("product_name");
            var product_id = in_buy_btn.data("product_id");
            var product_price = in_buy_btn.data("product_price");
            basketUpdating(product_id, numb, is_delete=false);
        });

        function reshowBasket(){
            $('.dropdown-menu').addClass('show');
        };
        $(document).on('click', '.delete-item', function(e) {
            e.preventDefault();
            product_id = $(this).data("product_id")
            numb = 0;
            basketUpdating(product_id, numb, is_delete=true)
            reshowBasket();
        });

        $('#myModal').on('shown.bs.modal', function () {
          $('#myInput').trigger('focus')
        })

        $(document).on('click', '.navbar-toggler', function() {
            var elements = this.getElementsByTagName('span');
              for (var i = 0; i < elements.length; i++) {
                    elements[i].classList.toggle("show")

              }
          });
//modal window for modal forms
        $(function() {
        $(".login-btn").modalForm({formURL: "{% url 'accounts:login' %}"});
        $(".signup-btn").modalForm({formURL: "{% url 'accounts:signup' %}"});
        $(".create-callme").modalForm({formURL: "{% url 'create_callme' %}"});
        // $(".btn-main").modalForm({formURL: "{% url 'main_form' %}"});
        // $(".edu-btn").each(function () {
        //         $(this).modalForm({formURL: $(this).data('id')});
        //     });
        $(".btn-event").each(function () {
                $(this).modalForm({formURL: $(this).data('id')});
            });
        });
//modal error window
        $('#modal_message').modal({show:true});
//placeholders for callback's form
        document.getElementById('id_contact_name').placeholder = 'Александр';
        document.getElementById('id_contact_phone').placeholder = '+7 (765)256-12-15';
        // document.getElementById('id_contact_email').placeholder = 'info@likwid.ru';
//minicarousel owl buttons
        var owl = $('.owl-carousel');
        owl.owlCarousel({
            loop:true,
            margin:10,
            nav:false,
            dots:false,
            responsive:{
                0:{
                    items:1

                },
                600:{
                    items:2
                },
                1000:{
                    items:3

                }
            }
        });
        // Go to the next item
        $('.customNextBtn').click(function() {
            owl.trigger('next.owl.carousel');
        });
        // Go to the previous item
        $('.customPrevBtn').click(function() {
            // With optional speed parameter
            // Parameters has to be in square bracket '[]'
            owl.trigger('prev.owl.carousel');
        });

        $(function(){
          $("#id_contact_phone").mask("+7 999 999-9999");
        });
        $(function(){
          $("input[type='number']").inputSpinner();
        });
        // cart Dropdown menu
        $(document).on('click', '.cartDropdown', function() {
            var elements = this.getElementsByTagName('span');
              for (var i = 0; i < elements.length; i++) {
                    elements[i].classList.toggle("show")

              }
          });
});
