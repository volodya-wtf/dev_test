SELECT
    *
FROM
    cities
    CROSS JOIN customers;

SELECT
    customers.id AS customer_id,
    customer.name AS name,
    cities.name AS city
FROM
    cities
    RIGHT OUTER JOIN customers ON cities.id = customers.city_key
ORDER BY
    customers.id;

SELECT
    cities.id AS city_key,
    cities.name AS city,
    customer.id AS customer_id,
    customer.name AS name
FROM
    cities
    LEFT OUTER JOIN customers ON cities.id = customers.city_key
ORDER BY
    cities.id