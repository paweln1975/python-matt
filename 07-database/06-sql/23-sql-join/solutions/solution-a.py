
result = """

SELECT
    `users`.`firstname`,
    `users`.`lastname`,
    `addresses`.`street`,
    `addresses`.`city`,
    `addresses`.`country`
FROM `users`
LEFT JOIN `addresses`
ON `users`.`id` == `addresses`.`user_id`



"""
