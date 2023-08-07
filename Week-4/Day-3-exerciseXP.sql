-- Exercise 1 - DVD Rental


SELECT * FROM language;


SELECT film.title, film.description, language.name
FROM film
JOIN language ON film.language_id = language.language_id;


SELECT film.title, film.description, language.name
FROM language
LEFT JOIN film ON film.language_id = language.language_id;


CREATE TABLE new_film (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL
);

INSERT INTO new_film (name) VALUES 
   ('Beyond the skies'),
   ('Extraction'),
   ('Mission Impossible: Oblivion');


CREATE TABLE customer_review (
    review_id INT PRIMARY KEY AUTO_INCREMENT,
    film_id INT,
    language_id INT,
    title VARCHAR(255),
    score INT,
    review_text TEXT,
    last_update TIMESTAMP,
    CONSTRAINT fk_film FOREIGN KEY (film_id) REFERENCES new_film (id) ON DELETE CASCADE,
    CONSTRAINT fk_language FOREIGN KEY (language_id) REFERENCES language (language_id) ON DELETE CASCADE
);


INSERT INTO customer_review (film_id, language_id, title, score, review_text, last_update)
VALUES (1, 1, 'Great Movie', 9, 'This movie was fantastic!', NOW());

INSERT INTO customer_review (film_id, language_id, title, score, review_text, last_update)
VALUES (2, 2, 'Disappointing', 4, 'I was expecting more from this movie.', NOW());

--When a film is deleted from the new_film table, the corresponding entry in the customer_review 
--table will also be automatically deleted due to the ON DELETE CASCADE constraint.




-- Exercise 2 - DVD Rental


UPDATE films
SET language = 'French'  
WHERE film_id IN (SELECT film_id FROM actors WHERE actor_name = 'Penelope Monroe');

UPDATE films
SET language = 'English'  
WHERE film_id IN (SELECT film_id FROM film_ratings WHERE rating = 'R') 
AND length < '01:00:00';

UPDATE films
SET language = 'Spanish'  
WHERE film_id IN (SELECT film_id FROM rentals WHERE rental_date >= '2005-07-28' 
AND rental_date <= '2005-08-01' AND return_date IS NULL);

UPDATE films
SET language = 'Japanese'  
WHERE film_id IN (SELECT film_id FROM film_descriptions WHERE description LIKE '%boat%' 
OR title LIKE '%boat%' AND replacement_cost > 100);

Foreign keys (references) defined for the customer table are:
- store_id referencing store.store_id
- address_id referencing address.address_id


DROP TABLE customer_review;


SELECT COUNT(*) FROM rentals WHERE return_date IS NULL;


SELECT * FROM rentals
JOIN films ON rentals.film_id = films.film_id
WHERE return_date IS NULL
ORDER BY rental_rate DESC
LIMIT 30;


    
SELECT * FROM films
JOIN film_categories ON films.film_id = film_categories.film_id
JOIN actors ON films.film_id = actors.film_id
WHERE film_categories.category_name = 'Sumo'
AND actors.actor_name = 'Penelope Monroe';

    
SELECT * FROM films
JOIN film_ratings ON films.film_id = film_ratings.film_id
WHERE film_ratings.rating = 'R'
AND films.length < '01:00:00';


SELECT * FROM films
JOIN rentals ON films.film_id = rentals.film_id
JOIN customers ON rentals.customer_id = customers.customer_id
WHERE customers.first_name = 'Matthew' AND customers.last_name = 'Mahan'
AND rentals.rental_rate > 4.00
AND rentals.rental_date >= '2005-07-28' AND rentals.rental_date <= '2005-08-01';


SELECT * FROM films
JOIN rentals ON films.film_id = rentals.film_id
JOIN customers ON rentals.customer_id = customers.customer_id
WHERE customers.first_name = 'Matthew' AND customers.last_name = 'Mahan'
AND (films.title LIKE '%boat%' OR films.description LIKE '%boat%')
AND films.replacement_cost > 100;

