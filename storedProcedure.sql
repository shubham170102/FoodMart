USE grocery_store;
DROP PROCEDURE IF EXISTS GetTotalSalesPerDay;
DROP PROCEDURE IF EXISTS GetTopSellingProducts;
DROP PROCEDURE IF EXISTS GetAverageOrderValue;
DELIMITER //

CREATE PROCEDURE GetTotalSalesPerDay()
BEGIN
    SELECT DATE(timestamp) AS date, SUM(total_price) AS total_sales 
    FROM grocery_store.orders 
    GROUP BY DATE(timestamp);
END //

CREATE PROCEDURE GetTopSellingProducts()
BEGIN
    SELECT p.name, COUNT(*) AS total_orders
    FROM grocery_store.orderInfo od
    JOIN grocery_store.inventory p ON od.product_id = p.product_id
    GROUP BY p.product_id
    ORDER BY total_orders DESC
    LIMIT 10;
END //

CREATE PROCEDURE GetAverageOrderValue()
BEGIN
    SELECT AVG(total_price) AS avg_order_value
    FROM grocery_store.orders;
END //

DELIMITER ;
