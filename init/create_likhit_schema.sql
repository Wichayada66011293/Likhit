USE likhit_db;

-- Main user table
CREATE TABLE User (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    phone_number VARCHAR(10) UNIQUE,
    email VARCHAR(255),
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Personal profile (1 per user still assumed)
CREATE TABLE Personal_Profile (
    profile_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    full_name VARCHAR(255),
    gender VARCHAR(50),
    age INT,
    FOREIGN KEY (user_id) REFERENCES User(user_id)
);

-- User training sessions (multiple allowed)
CREATE TABLE Training (
    training_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    picture_labeling VARCHAR(255),
    sound_labeling VARCHAR(255),
    FOREIGN KEY (user_id) REFERENCES User(user_id)
);

-- Languages user can speak (multiple entries allowed)
CREATE TABLE Language (
    language_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    language_type VARCHAR(100),
    FOREIGN KEY (user_id) REFERENCES User(user_id)
);

-- Types of work that exist (static list)
CREATE TABLE Work_Type (
    work_type_id INT PRIMARY KEY AUTO_INCREMENT,
    work VARCHAR(255),
    data VARCHAR(255)
);

-- Work assigned to users (user can have many work assignments)
CREATE TABLE Work (
    work_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    language_type VARCHAR(100),
    work_type_id INT,
    FOREIGN KEY (user_id) REFERENCES User(user_id),
    FOREIGN KEY (work_type_id) REFERENCES Work_Type(work_type_id)
);
