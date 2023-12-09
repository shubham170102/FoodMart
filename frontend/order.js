$(function () {
    // Fetch and populate product data
    $.get('http://127.0.0.1:5000/getInventory', function (response) {
        if (response) {
            var options = '<option value="">--Select Product--</option>';
            $.each(response, function (index, product) {
                options += `<option value="${product.product_id}" data-price="${product.price_per_quantity}">${product.name}</option>`;
            });
            $('#productSelect').html(options);
        }
    });

    // Add more button functionality
    $('#addMoreButton').click(function () {
        addProductRow();
    });

    // Change event for product select
    $(document).on('change', '.product-select', function () {
        var price = $(this).find('option:selected').data('price');
        var quantity = $(this).closest('.product-row').find('.product-quantity').val();
        var total = price * quantity;
        $(this).closest('.product-row').find('.product-total').val(total.toFixed(2));
        updateGrandTotal();
    });

    // Change event for quantity input
    $(document).on('input', '.product-quantity', function () {
        var price = $(this).closest('.product-row').find('.product-select option:selected').data('price');
        var quantity = $(this).val();
        var total = price * quantity;
        $(this).closest('.product-row').find('.product-total').val(total.toFixed(2));
        updateGrandTotal();
    });

    // Remove product row functionality
    $(document).on('click', '.remove-product', function () {
        $(this).closest('.product-row').remove();
        updateGrandTotal();
    });

    // Save order functionality
    $('#saveOrder').click(function () {
        var orderDetails = $('.product-row').map(function () {
            return {
                product_id: $(this).find('.product-select').val(),
                quantity: $(this).find('.product-quantity').val(),
                total: $(this).find('.product-total').val()
            };
        }).get();

        var orderData = {
            customer_name: $('#customerName').val(),
            total_price: $('#grandTotal').text(),
            order_details: orderDetails
        };

        $.post('http://127.0.0.1:5000/addOrder', { data: JSON.stringify(orderData) }, function (response) {
            console.log('Order saved:', response);
            // Handle success feedback here
        }).fail(function (error) {
            console.error('Error saving order:', error);
            // Handle errors here
        });
    });
});

function addProductRow() {
    var newRow = $('<div class="product-row">');
    newRow.html(`
        <select class="product-select">
            <option value="">Select Product</option>
            // Options will be added here dynamically
        </select>
        <input type="number" class="product-quantity" value="1">
        <input type="text" class="product-total" readonly>
        <button class="remove-product">Remove</button>
    `);
    // Populate product options
    $("#productSelect option").clone().appendTo(newRow.find('.product-select'));
    $('#orderItems').append(newRow);
}


function updateGrandTotal() {
    var grandTotal = 0;
    $('.product-row').each(function () {
        var total = parseFloat($(this).find('.product-total').val()) || 0;
        grandTotal += total;
    });
    $('#grandTotal').text(grandTotal.toFixed(2));
}

