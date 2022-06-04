create table if not exists courseSection(
    CourseID int not null primary key,
    CourseName varchar(20) not null,
    Units int not null,
    SectionNumber int not null
);

create table if not exists Proffesor(
    ProfessorID int not null primary key,
    ProfessorName varchar(20) not null,
    title varchar(20) not null
);

create table if not exists department(
    DepartmentID int not null primary key,
    DepartmentName varchar(20) not null,
    ProfessorID int not null,
    foreign key (ProfessorID) references Proffesor(ProfessorID)
);

create table if not exists Students(
    StudentID int not null primary key,
    StudentName varchar(20) not null,
    Major varchar(20) not null,
    GPA float not null, 
    ProfessorID int not null,
    foreign key(ProfessorID) references Professor(ProfessorID)
);

create table if not exists  Period(
    SemesterID int not null primary key,
    SemesterYear int not null,
    StudentID int not null,
    CourseID int not null,
    SectionNumber int not null,
    ProfessorID int not null,
    foreign key (StudentID) references Students(StudentID),
    foreign key (CourseID) references courseSection(CourseID),
    foreign key (ProfessorID) references Proffesor(ProfessorID)
);

create table if not exists Rooms(
    RoomID int not null primary key,
    RoomNumber int not null,
    RoomCapacity int not null,
    StudentID int not null,
    foreign key  (StudentID) references Students(StudentID)
);