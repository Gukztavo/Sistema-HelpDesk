
CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255) NOT NULL
);

CREATE TABLE categories (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255) NOT NULL
);

CREATE TABLE statuses (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255) NOT NULL
);

CREATE TABLE tickets (
  id INT AUTO_INCREMENT PRIMARY KEY,
  title VARCHAR(255) NOT NULL,
  category_id varchar(15),
  description TEXT,
  deadline DATE,
  status_id varchar(15) default'Novo',
  created_at date,
  solved_at DATE,
  created_by INT,
  handled_by INT
);
Drop table tickets;
select * from tickets;

INSERT INTO statuses (name) VALUES ('Novo'), ('Em atendimento'), ('Resolvido');