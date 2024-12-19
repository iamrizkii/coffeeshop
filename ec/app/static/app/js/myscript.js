


$('.plus-cart').click(function() {
    var id = $(this).attr("pid").toString();
    var eml = this.parentNode.children[2];
    console.log("pid =", id);
    $.ajax({
        type: "GET",
        url: "/pluscart/",
        data: {
            prod_id:id
        },
        success: function(data) {
            console.log("data =", data);
            eml.innerText = data.quantity;
            document.getElementById("amount").innerText = data.amount;
            document.getElementById("totalamount").innerText = data.totalamount;
        }
    });
});

$('.minus-cart').click(function() {
    var id = $(this).attr("pid").toString();
    var eml = this.parentNode.children[2];
    $.ajax({
      type: "GET",
      url: "/minuscart/",
      data: {
        prod_id:id
      },
      success: function(data) {
        eml.innerText = data.quantity;
        document.getElementById("amount").innerText = data.amount;
        document.getElementById("totalamount").innerText = data.totalamount;
      }
    });
  });

  $('.remove-cart').click(function() {
    var id = $(this).attr("pid").toString();
    var eml = this;
    $.ajax({
        type: "GET",
        url: "/removecart/",
        data: {
            prod_id: id
        },
        success: function(data) {
            // Update the amount and total amount directly in the DOM
            document.getElementById("amount").innerText = 'Rp. ' + data.amount;
            document.getElementById("totalamount").innerText = 'Rp. ' + data.totalamount;

            // Remove the cart item row from the DOM
            $(eml).closest('.row').remove();

            // If the cart is now empty, display the "Cart is Empty" message
            if ($('#cart-items').children().length == 0) {
                $('#cart-items').html('<h1 class="text-center mb-5">Cart is Empty</h1>');
            }
        }
    });
});

  
  $('.plus-wishlist').click(function() {
    var id = $(this).attr("pid").toString();
    $.ajax({
      type: "GET",
      url: "/pluswishlist",
      data: {
        prod_id: id
      },
      success: function(data) {
        //alert(data.message)
        window.location.href = 'http://localhost:8000/product-detail/' + id;
      }
    });
  });

  $('.minus-wishlist').click(function() {
    var id = $(this).attr("pid").toString();
    $.ajax({
      type: "GET",
      url: "/minuswishlist",
      data: {
        prod_id: id
      },
      success: function(data) {
        window.location.href = 'http://localhost:8000/product-detail/' + id;
      }
    });
  });