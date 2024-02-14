-- Script listing all shows in hbtn_0d_tvshows that
-- have at lst 1 genre linked
-- Script listing all rows of a db that have one column in common
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
