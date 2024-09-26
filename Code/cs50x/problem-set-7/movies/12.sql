SELECT title FROM movies
INNER JOIN stars s1 ON movies.id = s1.movie_id
INNER JOIN stars s2 ON movies.id = s2.movie_id
INNER JOIN people p1 ON s1.person_id = p1.id
INNER JOIN people p2 ON s2.person_id = p2.id WHERE (
    p1.name = 'Bradley Cooper' OR p1.name = 'Jennifer Lawrence'
    ) AND (
        p2.name = 'Bradley Cooper' OR p2.name = 'Jennifer Lawrence'
    ) GROUP BY movies.title HAVING COUNT(DISTINCT s1.person_id) = 2;
