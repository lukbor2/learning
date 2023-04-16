SELECT 
    final_01_country,
    final_01_date,
    SUM(confirmed_number),
    SUM(deaths_number),
    SUM(recovered_number),
    SUM(current_positive),
    SUM(confirmed_delta),
    SUM(deaths_delta),
    SUM(recovered_delta),
    SUM(current_positive_delta),
    SUM(hospitalized),
    SUM(in_icu),
    SUM(hospitalized_tot),
    SUM(tested),
    SUM(tested_pos),
    SUM(hospitalized_delta),
    SUM(in_icu_delta),
    SUM(tested_pos_delta)
FROM final_01
WHERE final_01_country = 'Australia'
GROUP BY final_01_country, final_01_date
