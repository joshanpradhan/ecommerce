    $(document).ready(function() {

        //automatic   search

        var searchForm = $(".search-form");
        var searchInput = searchForm.find("[name='q']");
        var typingTimer;
        var typingInterval = 1500;


        searchInput.keyup(function(event) {
            clearTimeout(typingTimer)
            typingTimer = setTimeout(performSearch, typingInterval)
        })
        searchInput.keydown(function(event) {
            clearTimeout(typingTimer)

        })


        function performSearch() {

            var query = searchInput.val()
            window.location.href = '/search/?q=' + query;

        }


        //cart + add products
        var productForm = $(".form-product-ajax");
        productForm.submit(function(event) {

            event.preventDefault();
            var thisForm = $(this)
            // var actionEndpoint = thisForm.attr("action");
            var actionEndpoint = thisForm.attr("data-endpoint");
            var httpMethod = thisForm.attr("method");
            var formData = thisForm.serialize();

            $.ajax({
                url: actionEndpoint,
                method: httpMethod,
                data: formData,
                success: function(data) {
                    var submitSpan = thisForm.find(".submit-span");
                    if (data.added) {
                        submitSpan.html("<button type='submit' class='buy-now btn btn-sm btn-danger'>Remove From Cart</button>");
                    } else {
                        submitSpan.html("<button type='submit' class='buy-now btn btn-sm btn-primary'>Add To Cart</button>");
                    }

                    var navbarCount = $(".navbar-cart-count");
                    navbarCount.text(data.cartItemCount);
                    if (window.location.href.indexOf("cart") != -1) {
                        refreshCart()
                    }
                },
                error: function(errorData) {

                    console.log("error");
                    console.log(errorData);
                }

            })

        })

        function refreshCart() {
            console.log("Hello in current cart")
            var cartTable = $(".cart-table");
            var cartBody = cartTable.find(".cart-body");
            var cartTotal = cartTable.find(".total");
            var productRows = cartBody.find(".cart-product");
            var currentUrl = window.location.href
            var refreshCartUrl = "/api/cart/"
            var refreshCartMethod = "GET";
            var data = {};

            $.ajax({
                url: refreshCartUrl,
                method: refreshCartMethod,
                data: data,
                success: function(data) {
                    console.log("aaa")
                    var hiddenCartItemRemoveForm = $(".cart-item-remove-form");
                    if (data.products.length > 0) {
                        productRows.html(" ");
                        $.each(data.products, function(index, value) {

                            var newCartItemRemove = hiddenCartItemRemoveForm.clone();
                            newCartItemRemove.css("display", "block");
                            newCartItemRemove.find(".cart-item-product-id").val(value.id)
                            cartBody.prepend('<tr class="cart-product"> <td class="product-thumbnail"><img src="' + value.image + '"alt="' + value.title + '" class="img-fluid" style="height:150px;width:300px"> </td> <td class= "product-name" ><h2 class="h5 text-black"><a href="' + value.url + '">' + value.title + '</a></h2> </td><td>$' + value.price + '</td ><td><div class="input-group mb-3" style="max-width: 120px;"><div class="input-group-prepend"><button class="btn btn-outline-primary js-btn-minus" type="button">&minus;</button></div><input type="text" class="form-control text-center" value="1" placeholder="" aria-label="Example text with button addon" aria-describedby="button-addon1"><div class="input-group-append"><button class="btn btn-outline-primary js-btn-plus" type="button">&plus;</button></div></div></td><td > $' + value.price + '</td><td>' + newCartItemRemove.html() + '</td></tr>');



                        })
                        $(".cart-subtotal").text(data.subtotal);
                        $(".cart-total").text(data.total);

                    } else {
                        window.location.href = currentUrl;
                    }


                },
                error: function(errorData) {
                    console.log("error bmnbnb")
                    console.log(errorData)

                }
            })

        }

    })