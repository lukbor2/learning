CREATE 
    ALGORITHM = UNDEFINED 
    DEFINER = `root`@`localhost` 
    SQL SECURITY DEFINER
VIEW `ratios_01` AS
    SELECT 
        `v`.`confirmed_country` AS `confirmed_country`,
        `v`.`confirmed_region` AS `confirmed_region`,
        `v`.`confirmed_date` AS `confirmed_date`,
        `v`.`confirmed_number` AS `confirmed_number`,
        `v`.`deaths_number` AS `deaths_number`,
        `v`.`recovered_number` AS `recovered_number`,
        `v`.`current_positive` AS `current_positive`,
        ((`v`.`deaths_number` / `v`.`confirmed_number`) * 100) AS `death_ratio`
    FROM
        `current_positive` `v`