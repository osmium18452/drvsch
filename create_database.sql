CREATE DATABASE drive_school;
USE drive_school;

# coach
CREATE TABLE IF NOT EXISTS coach
(
cno CHAR(9),
cname CHAR(20),
PRIMARY KEY (cno)
);

# students
CREATE TABLE IF NOT EXISTS student
(
sno CHAR(9),
sname CHAR(20),
PRIMARY KEY (sno)
);

# field
CREATE TABLE IF NOT EXISTS field
(
fno CHAR(9),
floc CHAR(50),
fcap INT,
PRIMARY KEY (fno)
);

# exam
CREATE TABLE IF NOT EXISTS exam
(
eno CHAR(9),
etime DATE,
fno CHAR(9),
PRIMARY KEY (eno),
FOREIGN KEY (fno) REFERENCES field(fno)
);

# lesson
CREATE TABLE IF NOT EXISTS lesson
(
lno CHAR(9),
fno CHAR(9),
cno CHAR(9),
PRIMARY KEY (lno),
FOREIGN KEY (cno) REFERENCES coach(cno),
FOREIGN KEY (fno) REFERENCES field(fno)
);

# student-exam
CREATE TABLE IF NOT EXISTS SE
(
sno CHAR(9),
eno CHAR(9),
PRIMARY KEY (sno, eno),
FOREIGN KEY (sno) REFERENCES student(sno),
FOREIGN KEY (eno) REFERENCES exam(eno)
);

# student-field
CREATE TABLE IF NOT EXISTS SF
(
sno CHAR(9),
fno CHAR(9),
sftime DATE,
PRIMARY KEY (sno, fno, sftime),
FOREIGN KEY (sno) REFERENCES student(sno),
FOREIGN KEY (fno) REFERENCES field(fno)
);

# student-lesson
CREATE TABLE IF NOT EXISTS SL
(
sno CHAR(9),
lno CHAR(9),
PRIMARY KEY (sno, lno),
FOREIGN KEY (sno) REFERENCES student(sno),
FOREIGN KEY (lno) REFERENCES lesson(lno)
)
