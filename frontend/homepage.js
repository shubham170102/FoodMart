$(function() {
    loadHomepageOrders();

    function loadHomepageOrders() {
        $.get('http://127.0.0.1:5000/getAllOrders', function(response) {
            if(response) {
                var tableContent = '';
                var totalCost = 0;

                $.each(response, function(index, order) {
                    var orderTotal = parseFloat(order.total_price);
                    totalCost += orderTotal;

                    tableContent += '<tr>' +
                        '<td>'+ new Date(order.timestamp).toLocaleString() +'</td>'+
                        '<td>'+ order.order_id +'</td>'+
                        '<td>'+ order.customer_name +'</td>'+
                        '<td>'+ orderTotal.toFixed(2) + ' $</td></tr>';
                });

                tableContent += '<tr><td colspan="3" style="text-align: right;"><b>Total</b></td><td><b>'+ totalCost.toFixed(2) +' $</b></td></tr>';
                $("#ordersTable tbody").html(tableContent);
            }
        }).fail(function() {
            console.error('Error fetching order data.');
        });
    }
});
