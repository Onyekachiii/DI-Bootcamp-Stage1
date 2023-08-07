-- Exercise 1 - Items & Customers

SELECT * FROM items
ORDER BY price;


SELECT * FROM items
WHERE price >= 80
ORDER BY price DESC;


SELECT first_name, last_name FROM customers
ORDER BY first_name
LIMIT 3;


SELECT last_name FROM customers
ORDER BY last_name DESC;




-- Exercise 2 - DVD Rental Database

SELECT * FROM customer;

SELECT first_name || ' ' || last_name AS full_name FROM customer;

SELECT DISTINCT create_date FROM customer;

SELECT * FROM customer ORDER BY first_name DESC;

SELECT film_id, title, description, release_year, rental_rate FROM film ORDER BY rental_rate ASC;

SELECT address, phone FROM address WHERE district = 'Texas';

SELECT * FROM film WHERE film_id = 15 OR film_id = 150;

SELECT film_id, title, description, length, rental_rate FROM film WHERE title LIKE 'YourFavoriteMovie%';

SELECT film_id, title, description, length, rental_rate FROM film WHERE title LIKE 'Yo%' AND length = LENGTH('YourFavoriteMovie') AND rental_rate = (SELECT rental_rate FROM film WHERE title = 'YourFavoriteMovie');

SELECT film_id, title, description, length, rental_rate FROM film ORDER BY rental_rate ASC LIMIT 10;

SELECT film_id, title, description, length, rental_rate FROM film WHERE rental_rate > (SELECT rental_rate FROM film ORDER BY rental_rate ASC LIMIT 10 OFFSET 10) ORDER BY rental_rate ASC LIMIT 10;

SELECT customer.first_name, customer.last_name, payment.amount, payment.payment_date FROM customer JOIN payment ON customer.customer_id = payment.customer_id ORDER BY customer.customer_id ASC;

SELECT * FROM film WHERE film_id NOT IN (SELECT film_id FROM inventory);

SELECT city.city, country.country FROM city JOIN country ON city.country_id = country.country_id;

SELECT c.customer_id, c.first_name, c.last_name, p.amount, p.payment_date, s.staff_id
FROM customer c
JOIN payment p ON c.customer_id = p.customer_id
JOIN staff s ON p.staff_id = s.staff_id
ORDER BY s.staff_id;