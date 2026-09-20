CREATE VIEW `current_positive` AS
    SELECT 
        c.confirmed_country,
        c.confirmed_region,
        c.confirmed_date,
        c.confirmed_number,
        d.deaths_number,
        r.recovered_number,
        c.confirmed_number - (d.deaths_number + r.recovered_number) AS current_positive,
        c.confirmed_delta,
        c.confirmed_delta_p,
        d.deaths_delta,
        d.deaths_delta_p,
        r.recovered_delta,
        r.recovered_delta_p,
        c.confirmed_delta - (d.deaths_delta + r.recovered_delta) AS current_positive_delta,
        CONCAT(c.confirmed_country, c.confirmed_region) AS country_region
    FROM
        confirmed AS c,
        deaths AS d,
        recovered AS r
    WHERE
        ((c.confirmed_country = d.deaths_country)
            AND (d.deaths_country = r.recovered_country))
            AND ((c.confirmed_region = d.deaths_region)
            AND (d.deaths_region = r.recovered_region))
            AND ((c.confirmed_date = d.deaths_date)
            AND (d.deaths_date = r.recovered_date))
    ORDER BY c.confirmed_country , c.confirmed_region , c.confirmed_date
