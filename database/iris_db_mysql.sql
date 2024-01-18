-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema iris_v2_1
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema iris_v2_1
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `iris_v2_1` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `iris_v2_1` ;

-- -----------------------------------------------------
-- Table `iris_v2_1`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `iris_v2_1`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(255) NULL DEFAULT NULL,
  `last_name` VARCHAR(255) NULL DEFAULT NULL,
  `middle_name` VARCHAR(255) NULL DEFAULT NULL,
  `added` VARCHAR(255) NULL DEFAULT NULL,
  `updated` VARCHAR(255) NULL DEFAULT NULL,
  `email` VARCHAR(255) NULL DEFAULT NULL,
  `phone_number` VARCHAR(10) NULL DEFAULT NULL,
  `password` VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `iris_v2_1`.`alarms`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `iris_v2_1`.`alarms` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL DEFAULT NULL,
  `end_time` VARCHAR(255) NULL DEFAULT NULL,
  `added` VARCHAR(255) NULL DEFAULT NULL,
  `updated` VARCHAR(255) NULL DEFAULT NULL,
  `does_repeat` TINYINT NULL DEFAULT NULL,
  `repeat_days` VARCHAR(255) NULL DEFAULT NULL,
  `non_repeat_date` VARCHAR(255) NULL DEFAULT NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_alarms_users1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_alarms_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `iris_v2_1`.`users` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 25
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `iris_v2_1`.`async_thread_to_dos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `iris_v2_1`.`async_thread_to_dos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `added` VARCHAR(255) NULL DEFAULT NULL,
  `updated` VARCHAR(255) NULL DEFAULT NULL,
  `user_id` INT NOT NULL,
  `to_do` VARCHAR(2000) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_async_thread_to_dos_users1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_async_thread_to_dos_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `iris_v2_1`.`users` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `iris_v2_1`.`habit`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `iris_v2_1`.`habit` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL DEFAULT NULL,
  `due_time` VARCHAR(45) NULL DEFAULT NULL,
  `done_for_day` TINYINT NULL DEFAULT NULL,
  `priority` VARCHAR(45) NULL DEFAULT NULL,
  `added` DATETIME NULL DEFAULT NULL,
  `updated` DATETIME NULL DEFAULT NULL,
  `repeat_days` VARCHAR(255) NULL DEFAULT NULL,
  `description` VARCHAR(5000) NULL DEFAULT NULL,
  `reminded` TINYINT NULL DEFAULT NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_habit_users1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_habit_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `iris_v2_1`.`users` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 21
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `iris_v2_1`.`completed_habit`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `iris_v2_1`.`completed_habit` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `habit_id` INT NOT NULL,
  `added` DATETIME NULL DEFAULT NULL,
  `updated` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_completed_daily_to_do_daily_to_do1_idx` (`habit_id` ASC) VISIBLE,
  CONSTRAINT `fk_completed_daily_to_do_daily_to_do1`
    FOREIGN KEY (`habit_id`)
    REFERENCES `iris_v2_1`.`habit` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 4
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `iris_v2_1`.`devices`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `iris_v2_1`.`devices` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL DEFAULT NULL,
  `compute` VARCHAR(255) NULL DEFAULT NULL,
  `added` DATETIME NULL DEFAULT NULL,
  `updated` DATETIME NULL DEFAULT NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_devices_users1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_devices_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `iris_v2_1`.`users` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `iris_v2_1`.`current_locations`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `iris_v2_1`.`current_locations` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `latitude` FLOAT NULL DEFAULT NULL,
  `longitude` FLOAT NULL DEFAULT NULL,
  `added` VARCHAR(255) NULL DEFAULT NULL,
  `updated` VARCHAR(255) NULL DEFAULT NULL,
  `device_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_current_locations_devices1_idx` (`device_id` ASC) VISIBLE,
  CONSTRAINT `fk_current_locations_devices1`
    FOREIGN KEY (`device_id`)
    REFERENCES `iris_v2_1`.`devices` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `iris_v2_1`.`lights`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `iris_v2_1`.`lights` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `on_off` VARCHAR(45) NULL DEFAULT NULL,
  `lights_color` VARCHAR(255) NULL DEFAULT NULL,
  `lights_brightness` INT NULL DEFAULT NULL,
  `does_repeat` VARCHAR(45) NULL DEFAULT 'NO',
  `repeat_days` VARCHAR(255) NULL DEFAULT NULL,
  `time` VARCHAR(45) NULL DEFAULT NULL,
  `non_repeat_date` VARCHAR(255) NULL DEFAULT NULL,
  `added` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 10
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `iris_v2_1`.`note_file`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `iris_v2_1`.`note_file` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `note_name` VARCHAR(255) NULL DEFAULT NULL,
  `added` VARCHAR(255) NULL DEFAULT NULL,
  `updated` VARCHAR(255) NULL DEFAULT NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_note_file_users1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_note_file_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `iris_v2_1`.`users` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `iris_v2_1`.`note`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `iris_v2_1`.`note` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `note_text` VARCHAR(2000) NULL DEFAULT NULL,
  `added` VARCHAR(45) NULL DEFAULT NULL,
  `updated` VARCHAR(45) NULL DEFAULT NULL,
  `description` VARCHAR(255) NULL DEFAULT NULL,
  `note_file_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_note_note_file1_idx` (`note_file_id` ASC) VISIBLE,
  CONSTRAINT `fk_note_note_file1`
    FOREIGN KEY (`note_file_id`)
    REFERENCES `iris_v2_1`.`note_file` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 4
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `iris_v2_1`.`reminders`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `iris_v2_1`.`reminders` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `end_time` VARCHAR(45) NULL DEFAULT NULL,
  `reminder` VARCHAR(2000) NULL DEFAULT NULL,
  `to_say` VARCHAR(255) NULL DEFAULT NULL,
  `added` DATETIME NULL DEFAULT NULL,
  `updated` DATETIME NULL DEFAULT NULL,
  `does_repeat` TINYINT NULL DEFAULT NULL,
  `repeat_days` VARCHAR(255) NULL DEFAULT NULL,
  `non_repeat_date` VARCHAR(255) NULL DEFAULT NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_reminders_users1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_reminders_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `iris_v2_1`.`users` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 5
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `iris_v2_1`.`settings`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `iris_v2_1`.`settings` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `added` VARCHAR(255) NULL DEFAULT NULL,
  `updated` VARCHAR(255) NULL DEFAULT NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_settings_users1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_settings_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `iris_v2_1`.`users` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `iris_v2_1`.`tasks`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `iris_v2_1`.`tasks` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `task_name` VARCHAR(255) NULL DEFAULT NULL,
  `description` VARCHAR(255) NULL DEFAULT NULL,
  `due_date` VARCHAR(255) NULL DEFAULT NULL,
  `priority` VARCHAR(45) NULL DEFAULT NULL,
  `status` VARCHAR(45) NULL DEFAULT NULL,
  `added` DATETIME NULL DEFAULT NULL,
  `updated` DATETIME NULL DEFAULT NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_tasks_users1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_tasks_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `iris_v2_1`.`users` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 4
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `iris_v2_1`.`timers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `iris_v2_1`.`timers` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `end_date` DATETIME NULL DEFAULT NULL,
  `name` VARCHAR(255) NULL DEFAULT NULL,
  `added` DATETIME NULL DEFAULT NULL,
  `updated` DATETIME NULL DEFAULT NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_timers_users1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_timers_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `iris_v2_1`.`users` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
