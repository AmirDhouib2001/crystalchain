Drop table if EXISTS Department;
CREATE TABLE Department (
    ID INT PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
  	LOCATION VARCHAR(45));

Drop table if exists Employee;
CREATE TABLE Employee (
    ID INT PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    Dept_ID INT,
    SALARY VARCHAR(45),
    FOREIGN KEY (Dept_ID) REFERENCES Department(ID));

INSERT INTO DEPARTMENT (ID, NAME, LOCATION) VALUES
(1, 'Executive', 'Sydney'),
(2, 'Production', 'Sydney'),
(3, 'Resources', 'Cape Town'),
(4, 'Technical', 'Texas'),
(5, 'Management', 'Paris');

INSERT INTO EMPLOYEE (ID, NAME, SALARY, Dept_ID) VALUES
(1, 'Candice', '4685', 1),
(2, 'Julia', '2559', 2),
(3, 'Bob', '4405', 4),
(4, 'Scarlet', '2350', 1),
(5, 'Ileana', '1151', 4);

SELECT Department.Name, COUNT(Employee.ID) AS NbEmployee
FROM Department
LEFT JOIN Employee ON Department.ID = Employee.Dept_ID
GROUP BY Department.Name
ORDER BY NbEmployee DESC,Department.Name