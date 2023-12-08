$(function () {
    loadInventory();
    $(".add-product").on("click", function (e) {
        e.preventDefault();
        showModal();
    });
});

function loadInventory() {
    $.get('http://127.0.0.1:5000/getInventory', function (response) {
        if (response) {
            var table = '';
            $.each(response, function (index, product) {
                table += '<tr data-id="' + product.product_id + '" data-name="' + product.name + '" data-unit="' + product.quantity_name + '" data-price="' + product.price_per_quantity + '">' +
                    '<td>' + product.name + '</td>' +
                    '<td>' + product.quantity_name + '</td>' +
                    '<td>' + product.price_per_quantity + '</td>' +
                    '<td><button class="btn btn-xs btn-danger delete-product">Delete</button></td></tr>';
            });
            $("table").find('tbody').empty().html(table);
        }
    });
}

$(document).on("click", ".delete-product", function () {
    var tr = $(this).closest('tr');
    var data = {
        product_id: tr.data('id')
    };
    var isDelete = confirm("Are you sure to delete " + tr.data('name') + " item?");
    if (isDelete) {
        callApi("POST", 'http://127.0.0.1:5000/deleteFromInventory', data);
    }
});

function callApi(method, url, data) {
    $.ajax({
        method: method,
        url: url,
        data: data
    }).done(function (msg) {
        window.location.reload();
    }).fail(function (jqXHR, textStatus, errorThrown) {
        console.error("Error in API Call!", textStatus, errorThrown, jqXHR);
    });
}

$("#saveProduct").on("click", function () {
    var data = $("#productForm").serializeArray();
    var requestPayload = {
        product_name: null,
        quantity_id: null,
        price_per_quantity: null
    };
    for (var i=0;i<data.length;++i) {
        var element = data[i];
        switch(element.name) {
            case 'name':
                requestPayload.product_name = element.value;
                break;
            case 'unit':
                requestPayload.quantity_id = element.value;
                break;
            case 'price':
                requestPayload.price_per_quantity = element.value;
                break;
        }
    }
    callApi("POST", 'http://127.0.0.1:5000/addToInventory', {
        'data': JSON.stringify(requestPayload)
    });
});


function showModal() {
    $("#myModal").find('h2').text('Add New Product');
    $("#name, #price").val('');
    $.get('http://127.0.0.1:5000/getQuantity', function (response) {
        if (response) {
            var options = '<option value="">--Select--</option>';
            $.each(response, function (index, quantity) {
                options += '<option value="' + quantity.quantity_id + '">' + quantity.quantity_name + '</option>';
            });
            $("#unit").empty().html(options);
        }
    });
    $("#myModal").show();
}

function closeModal() {
    $("#myModal").hide();
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function (event) {
    var modal = document.getElementById("myModal");
    if (event.target === modal) {
        closeModal();
    }
}