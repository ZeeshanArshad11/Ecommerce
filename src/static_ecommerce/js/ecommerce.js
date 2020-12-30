$(document).ready(function(){

  // Contact Form Handler
  var contactForm = $(".contact-form")
  var contactFormMethod = contactForm.attr("method")
  var contactFormAction = contactForm.attr("action")

  // Reuseable Function
  function displaySubmitting(submitBtn, defaultTxt, dosubmit){
    if (dosubmit){
      submitBtn.addClass("disabled")
      submitBtn.html("<i class='fa fa-spin fa-spinner'></i> Sending... ")
    }else{
      submitBtn.removeClass('disbabled')
      submitBtn.html(defaultTxt)
    }
  }

  contactForm.submit(function(event){
    event.preventDefault()
    var contactFormData = contactForm.serialize()
    var contactFormSubmitBtn = contactForm.find("[type='submit']")
    var contactFormSubmitBtnTxt = contactFormSubmitBtn.text()
    displaySubmitting(contactFormSubmitBtn, "", true)

    $.ajax({
      method: contactFormMethod,
      url:  contactFormAction,
      data: contactFormData,
      success: function(data){
        contactForm[0].reset()
        $.alert({
          title: 'Success!',
          content: data.message,
          theme: 'modern'
        })
        setTimeout(function(){
          displaySubmitting(contactFormSubmitBtn, contactFormSubmitBtnTxt, false)
        }, 500)
      },
      error : function(error){
        var jsonData = error.responseJSON
        var msg = ""
        $.each(jsonData, function(key, value){ // key, value for Dictionary and index, value for Array
          msg += key +": "+ value[0].message + "</br>"
        })
        $.alert({
          title: 'Oops!',
          content: msg ,
          theme: 'modern',
        })
        setTimeout(function(){
          displaySubmitting(contactFormSubmitBtn, contactFormSubmitBtnTxt, false)
        }, 500)
      }
    })
  })




  // Auto Search
  var searchForm = $('.search-form')
  var searchInput = searchForm.find("[name='q']") // input name='q'
  var typingTimer ;
  var typingInterval = 500 // .5 second
  var searchBtn = searchForm.find("[type='submit']")

  searchInput.keyup(function(event){
    // key released
    clearTimeout(typingTimer)
    typingTimer = setTimeout(performSearch, typingInterval)
  })

  searchInput.keydown(function(event){
    clearTimeout(typingTimer)
  })  


  function displaySearch(){
    searchBtn.addClass("disabled")
    searchBtn.html("<i class='fa fa-spin fa-spinner'></i> Searching ...")
  }

  function performSearch(){
    displaySearch()
    var query = searchInput.val()
    console.log(event)
    setTimeout(function(){
      window.location.href = '/search/?q=' + query
    }, 1000)
  }




  // add or Remove Product from Cart 
  var productForm = $(".form-product-ajax")

  productForm.submit(function(event){
    event.preventDefault();
    //console.log("form is not sending")

    var thisForm = $(this)
    var actionEndPoint = thisForm.attr("action");
    var dataEndPoint = thisForm.attr("data-endpoint");
    var httpMethod = thisForm.attr("method");
    var formData = thisForm.serialize();

    $.ajax({
      url : actionEndPoint,
      method : httpMethod,
      data : formData,

      success : function(data){
        // console.log("Success")
        // console.log(data)
        // console.log("added",data.added)
        // console.log("removed",data.removed)
        var submitSpan = thisForm.find(".submit-span")
        // console.log(submitSpan.html())
        if (data.added){
          submitSpan.html("In CART <button type='submit' class='btn btn-danger btn-sm'>Remove ?</button>")
        }else{
          submitSpan.html("<button type='submit' class='btn btn-success'>ADD in CART</button>")
        }
        
        var navbarCount = $(".navbar-cart-count")
        navbarCount.text(data.cartItemCount)
        var currentPath = window.location.href
        if (currentPath.indexOf('cart') != -1){
          refreshCart()
        }
      },
      error: function(errorData){
        $.alert({
          title: 'Oops!',
          content: 'Something Wrong!',
          theme: 'modern'
        })
      }
    }) // Closing Ajax in Submit
  }) // Closing Submit Function
  function refreshCart(){
    console.log('In Current Cart')
    var carTable = $('.cart-table')
    var cartBody = carTable.find('.cart-body')
    var productRows = cartBody.find(".cart-products")
    var CurrentUrl = window.location.href




    var refreshCartUrl = '/api/cart/';
    var refreshCartMethod = 'GET';
    var data = {};
    $.ajax({
      url : refreshCartUrl,
      method : refreshCartMethod,
      data : data,
      success : function(data){
        
        var hiddenCartItemRemoveForm = $('.cart-item-remove-form')
        if (data.products.length > 0){
          productRows.html(" ")
          i = data.products.length
          $.each(data.products, function(index, value){
            var newCartItemRemove = hiddenCartItemRemoveForm.clone()
            newCartItemRemove.css("display","block")
            newCartItemRemove.find(".cart-item-product-id").val(value.id)
            cartBody.prepend("<tr><th scope=\"row\">"+ i +"</th><td><a href='"+ value.url +"'>"+ value.name +"</a><small>"+ +" </small></td> <td>"+ value.price +"</td> </tr>")
            i --
          })
          cartBody.find(".cart-subtotal").html(data.subtotal)
          cartBody.find(".cart-total").html(data.total)
        }
        else{
          window.location.href = currentUrl
        }
      },
      error : function(errorData){
        // console.log('error')
        // console.log(errorData)
        $.alert({
          title: 'Oops!',
          content: 'Something Wrong!',
          theme: 'modern'
        })
      }
    }) // Closing ajax in refreshCart
  } // Closing refreshCart Function
})// Closing Ready Function