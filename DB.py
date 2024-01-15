"""
CREATE TABLE `ap`.`user` (
  `idUser` INT AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `hashed_password` VARCHAR(45) NOT NULL,
  `tmp_password` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NULL,
  PRIMARY KEY (`idUser`),
  UNIQUE INDEX `idUser_UNIQUE` (`idUser` ASC) VISIBLE);





  CREATE TABLE `ap`.`Doctor` (
  `idDoctor` INT NOT NULL AUTO_INCREMENT,
  `Name` VARCHAR(45) NOT NULL,
  `specialization` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idDoctor`),
  UNIQUE INDEX `idDoctor_UNIQUE` (`idDoctor` ASC) VISIBLE);



CREATE TABLE `ap`.`Clinic` (
  `idClinic` INT NOT NULL AUTO_INCREMENT,
  `Name` VARCHAR(45) NOT NULL,
  `address` VARCHAR(45) NOT NULL,
  `contact` VARCHAR(45) NOT NULL,
  `availability` INT NOT NULL,
  `capacity` INT NOT NULL,
  `admin_name` VARCHAR(45) NOT NULL,
  `admin_email` VARCHAR(45) NOT NULL,
  `admin_hashedpassword` VARCHAR(45) NOT NULL,
  `admin_tmppassword` VARCHAR(45) NULL,
  PRIMARY KEY (`idClinic`),
  UNIQUE INDEX `idDoctor_UNIQUE` (`idClinic` ASC) VISIBLE);

  CREATE TABLE `ap`.`appointment` (
  `idAppointment` INT NOT NULL AUTO_INCREMENT,
  `FK_Clinic` INT NOT NULL,
  `FK_Doctor` INT NOT NULL,
  `FK_User` INT NOT NULL,
  `DateTime` DATETIME NOT NULL,
  `Status` TINYINT NOT NULL,
  PRIMARY KEY (`idAppointment`),
  UNIQUE INDEX `idAppointment_UNIQUE` (`idAppointment` ASC) VISIBLE);

  CREATE TABLE `ap`.`clinicdoctor` (
  `idClinicDoctor` INT NOT NULL AUTO_INCREMENT,
  `FK_Clinic` INT NOT NULL,
  `FK_Doctor` INT NOT NULL,
  PRIMARY KEY (`idClinicDoctor`),
  UNIQUE INDEX `idAppointment_UNIQUE` (`idClinicDoctor` ASC) VISIBLE);



ALTER TABLE `ap`.`appointment`
ADD INDEX `idClinic_idx` (`FK_Clinic` ASC) VISIBLE,
ADD INDEX `Appointment_FK_User_idx` (`FK_User` ASC) VISIBLE,
ADD INDEX `Appointment_FK_Doctor_idx` (`FK_Doctor` ASC) VISIBLE;
;
ALTER TABLE `ap`.`appointment`
ADD CONSTRAINT `Appointment_FK_Clinic`
  FOREIGN KEY (`FK_Clinic`)
  REFERENCES `ap`.`clinic` (`idClinic`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION,
ADD CONSTRAINT `Appointment_FK_User`
  FOREIGN KEY (`FK_User`)
  REFERENCES `ap`.`user` (`idUser`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION,
ADD CONSTRAINT `Appointment_FK_Doctor`
  FOREIGN KEY (`FK_Doctor`)
  REFERENCES `ap`.`doctor` (`idDoctor`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;



ALTER TABLE `ap`.`clinicdoctor`
ADD INDEX `ClinicDoctor_FK_Clinic_idx` (`FK_Clinic` ASC) VISIBLE,
ADD INDEX `ClinicDoctor_FK_Doctor_idx` (`FK_Doctor` ASC) VISIBLE;
;
ALTER TABLE `ap`.`clinicdoctor`
ADD CONSTRAINT `ClinicDoctor_FK_Clinic`
  FOREIGN KEY (`FK_Clinic`)
  REFERENCES `ap`.`clinic` (`idClinic`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION,
ADD CONSTRAINT `ClinicDoctor_FK_Doctor`
  FOREIGN KEY (`FK_Doctor`)
  REFERENCES `ap`.`doctor` (`idDoctor`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;



"""