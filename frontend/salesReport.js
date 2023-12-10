$(document).ready(function() {
    $.get('http://127.0.0.1:5000/salesReport', function(response) {
        if(response) {
            var tableContent = '';

            // Display top selling products
            $.each(response.top_selling_products, function(index, product) {
                tableContent += '<tr><td>' + product[0] + '</td><td>' + product[1] + '</td></tr>';
            });

            // Display total sales per day with loop
            $.each(response.total_sales_per_day, function(index, sales) {
                tableContent += '<tr><td><b>Total Sales for ' + sales[0] + '</b></td><td>' + '$' + sales[1] + '</td></tr>';
            });

            // Display average order value
            var averageOrderValue = response.average_order_value[0];
            tableContent += '<tr><td><b>Average Order Value</b></td><td>' + '$' + averageOrderValue + '</td></tr>';

            $("#ordersTable tbody").html(tableContent);
        }
    }).fail(function() {
        alert("Error fetching data.");
    });
});
