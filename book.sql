CREATE DATABASE IF NOT EXISTS `playlists` DEFAULT CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci;
USE `playlists`;
SET NAMES utf8mb4; 



CREATE TABLE IF NOT EXISTS `users`(
		`id` INT NOT NULL,
        `playlist_name` VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
        `playlist_link` VARCHAR(255) NOT NULL,
        PRIMARY KEY (`id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE utf8mb4_unicode_ci;

ALTER TABLE `users` CHANGE `playlist_name` `playlist_name` VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL;
ALTER TABLE `users` 
  MODIFY COLUMN `id` INT AUTO_INCREMENT;

SELECT * FROM `users`;


