# BIS 698 
# CMU FACILITIES MANAGEMENT SYSTEM SQL SCRIPTS
# GROUP-1
# FOR DROPPING TABLES
use sp2024bis698g1s;
DROP TABLE IF EXISTS TASK_UPDATE;
DROP TABLE IF EXISTS TASK;
DROP TABLE IF EXISTS CATEGORY;
DROP TABLE IF EXISTS EMP_DEPARTMENT;
DROP TABLE IF EXISTS FM_DEPARTMENT;
DROP TABLE IF EXISTS EMPLOYEE_SKILL;
DROP TABLE IF EXISTS SKILL;
DROP TABLE IF EXISTS EMPLOYEE;
DROP TABLE IF EXISTS REQUESTOR;
DROP TABLE IF EXISTS ROOM;
DROP TABLE IF EXISTS FLOOR;
DROP TABLE IF EXISTS BUILDING;



# CREATING BUILDING TABLE
DROP TABLE  IF EXISTS BUILDING;
CREATE TABLE BUILDING (
    BUILD_ID INT PRIMARY KEY,
    BUILD_NAME VARCHAR(100),
    BUILD_LOCATION VARCHAR(100)
);

# INSERTING VALUES INTO BUILDING TABLE
INSERT INTO BUILDING (BUILD_ID, BUILD_NAME, BUILD_LOCATION)
VALUES 
(1, 'ALUMNI HOUSE', 'North Campus'),
(2, 'ANSPACH HALL', 'Central Campus'),
(3, 'ATHLETIC COMPLEX', 'South Campus'),
(4, 'ATLANTA TV 6 FM91.7', 'East Campus'),
(5, 'BARNES HALL', 'West Campus'),
(6, 'BARNES KITCHEN', 'Central Campus'),
(7, 'BARSTOW PROPERTY', 'North Campus'),
(8, 'BAY CITY FM 90.1', 'South Campus'),
(9, 'BEAVER ISLAND', 'West Campus'),
(10, 'BEDDOW HALL', 'Central Campus'),
(11, 'BENNETT TRACK', 'East Campus'),
(12, 'BIOLOGY/PBS STORAGE', 'North Campus'),
(13, 'BIOSCIENCES BUILDING', 'Central Campus'),
(14, 'BOVEE UNIVERSITY CENTER', 'South Campus'),
(15, 'BROOKS HALL', 'West Campus'),
(16, 'CABLE HEAD DISH STATION', 'East Campus'),
(17, 'CADILLAC TV 27\ROOM 001', 'North Campus'),
(18, 'CALKINS HALL', 'Central Campus'),
(19, 'CAMPBELL HALL', 'South Campus'),
(20, 'CAMPUS', 'Central Campus'),
(21, 'CAREY DINING', 'West Campus'),
(22, 'CAREY HALL', 'East Campus'),
(23, 'CART\SMART ZONE BUILDING', 'North Campus'),
(24, 'CELANI', 'Central Campus'),
(25, 'CENTRAL ENERGY FACILITY', 'South Campus'),
(26, 'CHEYBOGAN M\W\ROOM 001', 'West Campus'),
(27, 'CHIPPEWA CHAMPIONS CENTER', 'East Campus'),
(28, 'CHIPPEWA RIVER M\W', 'North Campus'),
(29, 'COBB HALL', 'Central Campus'),
(30, 'COMBINED SERVICES BUILDING', 'South Campus');

# CREATING FLOOR TABLE
DROP TABLE IF EXISTS FLOOR;
CREATE TABLE FLOOR (
    FLOOR_ID INT PRIMARY KEY,
    FLOOR_NO VARCHAR(50),
    BUILD_ID INT,
    FOREIGN KEY (BUILD_ID) REFERENCES BUILDING(BUILD_ID)
);

# INSERTING VALUES INTO FLOOR TABLE
INSERT INTO FLOOR (FLOOR_ID, FLOOR_NO, BUILD_ID)
VALUES 
    (1, 'floor1', 1),
    (2, 'floor2', 1),
    (3, 'floor3', 1),
    (4, 'floor4', 1),
    (5, 'floor1', 1),
    (6, 'floor2', 2),
    (7, 'floor3', 2),
    (8, 'floor4', 2),
    (9, 'floor1', 2),
    (10, 'floor2', 2),
    (11, 'floor3', 3),
    (12, 'floor4', 3),
    (13, 'floor1', 3),
    (14, 'floor2', 3),
    (15, 'floor3', 3),
    (16, 'floor4', 4),
    (17, 'floor1', 4),
    (18, 'floor2', 4),
    (19, 'floor3', 4),
    (20, 'floor4', 4),
    (21, 'floor1', 5),
    (22, 'floor2', 5),
    (23, 'floor3', 5),
    (24, 'floor4', 5),
    (25, 'floor1', 5),
    (26, 'floor2', 6),
    (27, 'floor3', 6),
    (28, 'floor4', 6),
    (29, 'floor1', 6),
    (30, 'floor2', 6);
    
    
    # CREATING ROOM TABLE
    DROP TABLE IF EXISTS ROOM;
    CREATE TABLE ROOM (
    ROOM_ID INT PRIMARY KEY,
    ROOM_NO VARCHAR(10),
    FLOOR_ID INT,
    FOREIGN KEY (FLOOR_ID) REFERENCES FLOOR(FLOOR_ID)
);

# INSERTING VALUES INTO ROOM TABLE
INSERT INTO ROOM (ROOM_ID, ROOM_NO, FLOOR_ID)
VALUES
    (1, 'Room1', 1),
    (2, 'Room2', 1),
    (3, 'Room3', 1),
    (4, 'Room4', 1),
    (5, 'Room1', 1),
    (6, 'Room2', 2),
    (7, 'Room3', 2),
    (8, 'Room4', 2),
    (9, 'Room1', 2),
    (10, 'Room2', 2),
    (11, 'Room3', 3),
    (12, 'Room4', 3),
    (13, 'Room1', 3),
    (14, 'Room2', 3),
    (15, 'Room3', 3),
    (16, 'Room4', 4),
    (17, 'Room1', 4),
    (18, 'Room2', 4),
    (19, 'Room3', 4),
    (20, 'Room4', 4),
    (21, 'Room1', 5),
    (22, 'Room2', 5),
    (23, 'Room3', 5),
    (24, 'Room4', 5),
    (25, 'Room1', 5),
    (26, 'Room2', 6),
    (27, 'Room3', 6),
    (28, 'Room4', 6),
    (29, 'Room1', 6),
    (30, 'Room2', 6);


# CREATING REQUESTOR TABLE
DROP TABLE IF EXISTS REQUESTOR;
CREATE TABLE REQUESTOR (
    REQ_ID INT AUTO_INCREMENT PRIMARY KEY,
    ROOM_ID INT,
    REQ_GLOBALID VARCHAR(100),
    REQ_FNAME VARCHAR(100),
    REQ_LNAME VARCHAR(100),
    REQ_EMAIL VARCHAR(100),
    REQ_PHONE VARCHAR(20),
    REQ_DATE DATE,
    REQ_DESCR TEXT,
    FOREIGN KEY (ROOM_ID) REFERENCES ROOM(ROOM_ID)
);

# INSERTING VALUES INTO REQUESTOR TABLE
INSERT INTO REQUESTOR (REQ_ID, ROOM_ID, REQ_GLOBALID, REQ_FNAME, REQ_LNAME, REQ_EMAIL, REQ_PHONE, REQ_DATE, REQ_DESCR)
VALUES
    (1, 1, 'REQ_001', 'John', 'Doe', 'john.doe@cmich.edu', '123-456-7890', '2024-03-21', 'Requesting maintenance for HVAC system in conference room.'),
    (2, 2, 'REQ_002', 'Jane', 'Smith', 'jane.smith@cmich.edu', '987-654-3210', '2024-03-20', 'Requesting plumbing repairs in restroom.'),
    (3, 3, 'REQ_003', 'Michael', 'Johnson', 'michael.johnson@cmich.edu', '456-789-0123', '2024-03-19', 'Requesting grounds maintenance for campus landscaping.'),
    (4, 4, 'REQ_004', 'Emily', 'Brown', 'emily.brown@cmich.edu', '789-012-3456', '2024-03-18', 'Requesting fire safety inspection for building.'),
    (5, 5, 'REQ_005', 'David', 'Martinez', 'david.martinez@cmich.edu', '321-654-9870', '2024-03-17', 'Requesting security system update for office area.'),
    (6, 6, 'REQ_006', 'Sarah', 'Wilson', 'sarah.wilson@cmich.edu', '654-987-0123', '2024-03-16', 'Requesting electrical repairs in classroom.'),
    (7, 7, 'REQ_007', 'Christopher', 'Anderson', 'christopher.anderson@cmich.edu', '987-012-3456', '2024-03-15', 'Requesting exterior lighting installation for parking lot.'),
    (8, 8, 'REQ_008', 'Jessica', 'Taylor', 'jessica.taylor@cmich.edu', '210-543-8765', '2024-03-14', 'Requesting storm sewer inspection for campus.'),
    (9, 9, 'REQ_009', 'Daniel', 'Thomas', 'daniel.thomas@cmich.edu', '543-876-0987', '2024-03-13', 'Requesting painting work for building exteriors.'),
    (10, 10, 'REQ_010', 'Ashley', 'Hernandez', 'ashley.hernandez@cmich.edu', '876-098-7654', '2024-03-12', 'Requesting plumbing repairs in restroom.'),
    (11, 11, 'REQ_011', 'Matthew', 'Young', 'matthew.young@cmich.edu', '098-765-4321', '2024-03-11', 'Requesting maintenance for chilled water systems.'),
    (12, 12, 'REQ_012', 'Amanda', 'King', 'amanda.king@cmich.edu', '654-321-0987', '2024-03-10', 'Requesting electrical repairs in office area.'),
    (13, 13, 'REQ_013', 'James', 'Lee', 'james.lee@cmich.edu', '321-098-7654', '2024-03-09', 'Requesting signage maintenance for parking lot.'),
    (14, 14, 'REQ_014', 'Jennifer', 'Gonzalez', 'jennifer.gonzalez@cmich.edu', '098-765-4321', '2024-03-08', 'Requesting maintenance for HVAC system in classroom.'),
    (15, 15, 'REQ_015', 'Ryan', 'Perez', 'ryan.perez@cmich.edu', '543-210-9876', '2024-03-07', 'Requesting landscaping work for campus grounds.'),
    (16, 16, 'REQ_016', 'Emma', 'Rodriguez', 'emma.rodriguez@cmich.edu', '210-987-6543', '2024-03-06', 'Requesting roof repairs for building.'),
    (17, 17, 'REQ_017', 'Noah', 'Martinez', 'noah.martinez@cmich.edu', '876-543-2109', '2024-03-05', 'Requesting plumbing repairs in restroom.'),
    (18, 18, 'REQ_018', 'Olivia', 'Lopez', 'olivia.lopez@cmich.edu', '109-876-5432', '2024-03-04', 'Requesting installation of curbs and gutters.'),
    (19, 19, 'REQ_019', 'Ethan', 'Gonzalez', 'ethan.gonzalez@cmich.edu', '876-543-2109', '2024-03-03', 'Requesting sanitary sewer inspection for campus.'),
    (20, 20, 'REQ_020', 'Isabella', 'Hernandez', 'isabella.hernandez@cmich.edu', '543-210-9876', '2024-03-02', 'Requesting sidewalk repairs for campus.'),
    (21, 21, 'REQ_021', 'Mason', 'Diaz', 'mason.diaz@cmich.edu', '210-987-6543', '2024-03-01', 'Requesting lighting upgrade for interior.'),
    (22, 22, 'REQ_022', 'Sophia', 'Brown', 'sophia.brown@cmich.edu', '876-543-2109', '2024-02-29', 'Requesting maintenance for building mechanical systems.'),   
    (23, 23, 'REQ_023', 'Liam', 'Wilson', 'liam.wilson@cmich.edu', '109-876-5432', '2024-02-28', 'Requesting grounds maintenance for campus landscaping.'),
    (24, 24, 'REQ_024', 'Olivia', 'Garcia', 'olivia.garcia@cmich.edu', '876-543-2109', '2024-02-27', 'Requesting security system update for building.'),
    (25, 25, 'REQ_025', 'Ethan', 'Rodriguez', 'ethan.rodriguez@cmich.edu', '543-210-9876', '2024-02-26', 'Requesting electrical repairs in classroom.'),
    (26, 26, 'REQ_026', 'Ava', 'Martinez', 'ava.martinez@cmich.edu', '210-987-6543', '2024-02-25', 'Requesting exterior lighting installation for campus.'),
    (27, 27, 'REQ_027', 'Lucas', 'Hernandez', 'lucas.hernandez@cmich.edu', '876-543-2109', '2024-02-24', 'Requesting storm sewer inspection for campus.'),
    (28, 28, 'REQ_028', 'Amelia', 'Lopez', 'amelia.lopez@cmich.edu', '109-876-5432', '2024-02-23', 'Requesting painting work for building exteriors.'),
    (29, 29, 'REQ_029', 'William', 'Gonzalez', 'william.gonzalez@cmich.edu', '876-543-2109', '2024-02-22', 'Requesting plumbing repairs in restroom.'),
    (30, 30, 'REQ_030', 'Sophia', 'Smith', 'sophia.smith@cmich.edu', '543-210-9876', '2024-02-21', 'Requesting maintenance for HVAC system in office area.');

# CREATING EMPLOYEE TABLE
DROP TABLE IF EXISTS EMPLOYEE;
CREATE TABLE EMPLOYEE (
    EMP_ID INT PRIMARY KEY,
    EMP_GLOBALID VARCHAR(100),
    EMP_PASSWORD VARCHAR(20),
    EMP_FNAME VARCHAR(100),
    EMP_LNAME VARCHAR(100),
    EMP_EMAIL VARCHAR(100),
    EMP_CONTACT VARCHAR(20),
    EMP_ROLE VARCHAR(100),
    EMP_DOJ DATE,
    EMP_ADDRESS VARCHAR(255),
    EMP_STREET VARCHAR(100),
    EMP_CITY VARCHAR(100),
    EMP_STATE VARCHAR(100),
    EMP_ZIPCODE VARCHAR(20),
);

# INSERTING VALUES INTO EMPLOYEE TABLE
INSERT INTO EMPLOYEE (EMP_ID, EMP_GLOBALID,EMP_PASSWORD, EMP_FNAME, EMP_LNAME, EMP_EMAIL, EMP_CONTACT, EMP_ROLE, EMP_DOJ, EMP_ADDRESS, EMP_STREET, EMP_CITY, EMP_STATE, EMP_ZIPCODE)
VALUES
    (201, 'EMP_001', 'Test@12345', 'John', 'Doe', 'john.doe@cmich.edu', '+1234567890', 'Facilities Manager', '2023-01-01', '123 Main St', 'Sunset Blvd', 'Los Angeles', 'CA', '90001'),
    (202, 'EMP_002', 'Test@12345', 'Jane', 'Smith', 'jane.smith@cmich.edu', '+1987654321', 'Employee Manager', '2023-01-15', '456 Elm St', 'Ocean Ave', 'Miami', 'FL', '33101'),
    (203, 'EMP_003', 'Test@12345', 'Michael', 'Johnson', 'michael.johnson@cmich.edu', '+1765432987', 'Employee Manager', '2023-02-01', '789 Oak St', 'Broadway', 'New York', 'NY', '10001'),
    (204, 'EMP_004', 'Test@12345', 'Emily', 'Brown', 'emily.brown@cmich.edu', '+1654321987', 'Employee Manager', '2023-02-15', '101 Pine St', 'Main St', 'Chicago', 'IL', '60601'),
    (205, 'EMP_005', 'Test@12345', 'David', 'Martinez', 'david.martinez@cmich.edu', '+1543219876', 'Employee Manager', '2023-03-01', '222 Cedar St', 'Market St', 'San Francisco', 'CA', '94101'),
    (206, 'EMP_006', 'Test@12345', 'Sarah', 'Wilson', 'sarah.wilson@cmich.edu', '+1432198765', 'Employee Manager', '2023-03-15', '333 Maple St', 'Park Ave', 'Boston', 'MA', '02101'),
    (207, 'EMP_007', 'Test@12345', 'Christopher', 'Anderson', 'christopher.anderson@cmich.edu', '+1321987654', 'Employee Manager', '2023-04-01', '444 Walnut St', 'Lincoln St', 'Seattle', 'WA', '98101'),
    (208, 'EMP_008', 'Test@12345', 'Jessica', 'Taylor', 'jessica.taylor@cmich.edu', '+1219876543', 'Employee', '2023-04-15', '555 Cherry St', 'Washington St', 'Philadelphia', 'PA', '19101'),
    (209, 'EMP_009', 'Test@12345', 'Daniel', 'Thomas', 'daniel.thomas@cmich.edu', '+1198765432', 'Employee', '2023-05-01', '666 Peach St', 'Elm St', 'Dallas', 'TX', '75201'),
    (210, 'EMP_010', 'Test@12345', 'Ashley', 'Hernandez', 'ashley.hernandez@cmich.edu', '+1987654321', 'Employee', '2023-05-15', '777 Plum St', 'Spring St', 'Atlanta', 'GA', '30301'),
    (211, 'EMP_011', 'Test@12345', 'Matthew', 'Young', 'matthew.young@cmich.edu', '+1876543210', 'Employee Manager', '2023-06-01', '888 Apple St', 'King St', 'Houston', 'TX', '77001'),
    (212, 'EMP_012', 'Test@12345', 'Amanda', 'King', 'amanda.king@cmich.edu', '+1765432109', 'Employee', '2023-06-15', '999 Banana St', 'Highland Ave', 'Denver', 'CO', '80201'),
    (213, 'EMP_013', 'Test@12345', 'James', 'Lee', 'james.lee@cmich.edu', '+1654321098', 'Employee Manager', '2023-07-01', '1011 Orange St', 'Forest Ave', 'Phoenix', 'AZ', '85001'),
    (214, 'EMP_014', 'Test@12345', 'Jennifer', 'Gonzalez', 'jennifer.gonzalez@cmich.edu', '+1543210987', 'Employee', '2023-07-15', '1212 Lemon St', 'Park Pl', 'San Diego', 'CA', '92101'),
    (215, 'EMP_015', 'Test@12345', 'Ryan', 'Perez', 'ryan.perez@cmich.edu', '+1432109876', 'Employee Manager', '2023-08-01', '1313 Lime St', 'Oak St', 'Portland', 'OR', '97201'),
    (216, 'EMP_016', 'Test@12345', 'Emma', 'Rodriguez', 'emma.rodriguez@cmich.edu', '+1321098765', 'Employee', '2023-08-15', '1414 Grape St', 'Madison St', 'Las Vegas', 'NV', '89101'),
    (217, 'EMP_017', 'Test@12345', 'Noah', 'Martinez', 'noah.martinez@cmich.edu', '+1210987654', 'Employee', '2023-09-01', '1515 Olive St', 'Franklin St', 'Miami', 'FL', '33101'),
    (218, 'EMP_018', 'Test@12345', 'Olivia', 'Lopez', 'olivia.lopez@cmich.edu', '+1109876543', 'Employee', '2023-09-15', '1616 Fig St', 'Jefferson St', 'Chicago', 'IL', '60601'),
    (219, 'EMP_019', 'Test@12345', 'Ethan', 'Gonzalez', 'ethan.gonzalez@cmich.edu', '+1098765432', 'Employee Manager', '2023-10-01', '1717 Pear St', 'Monroe St', 'Boston', 'MA', '02101'),
    (220, 'EMP_020', 'Test@12345', 'Isabella', 'Hernandez', 'isabella.hernandez@cmich.edu', '+1987654321', 'Employee', '2023-10-15', '1818 Berry St', 'Jackson St', 'Philadelphia', 'PA', '19101'),
    (221, 'EMP_021', 'Test@12345', 'Benjamin', 'Tran', 'benjamin.tran@cmich.edu', '+1987654321', 'Employee', '2024-04-01', '2829 Orange St', 'Forest Ave', 'Chicago', 'IL', '60601'),
    (222, 'EMP_023', 'Test@12345', 'Sophia', 'Rodriguez', 'sophia.rodriguez@cmich.edu', '+1765432109', 'Employee', '2023-11-15', '1920 Apple St', 'Adams St', 'Seattle', 'WA', '98101'),
    (223, 'EMP_024', 'Test@12345', 'Oliver', 'Lee', 'oliver.lee@cmich.edu', '+1654321098', 'Employee Manager', '2023-12-01', '2021 Banana St', 'Jefferson St', 'Denver', 'CO', '80201'),
    (224, 'EMP_025', 'Test@12345', 'Emma', 'Chen', 'emma.chen@cmich.edu', '+1543210987', 'Employee Manager', '2023-12-15', '2122 Cherry St', 'Monroe St', 'Phoenix', 'AZ', '85001'),
    (225, 'EMP_026', 'Test@12345', 'William', 'Wong', 'william.wong@cmich.edu', '+1432109876', 'Employee', '2024-01-01', '2223 Grape St', 'Madison St', 'San Francisco', 'CA', '94101'),
    (226, 'EMP_027', 'Test@12345', 'Amelia', 'Garcia', 'amelia.garcia@cmich.edu', '+1321098765', 'Employee', '2024-01-15', '2324 Elm St', 'Washington St', 'Houston', 'TX', '77001'),
    (227, 'EMP_028', 'Test@12345', 'Elijah', 'Martinez', 'elijah.martinez@cmich.edu', '+1210987654', 'Employee Manager', '2024-02-01', '2425 Fig St', 'Park Pl', 'Miami', 'FL', '33101'),
    (228, 'EMP_029', 'Test@12345', 'Ava', 'Lopez', 'ava.lopez@cmich.edu', '+1109876543', 'Employee Manager', '2024-02-15', '2526 Grape St', 'Ocean Ave', 'Dallas', 'TX', '75201'),
    (229, 'EMP_030', 'Test@12345', 'Alexander', 'Nguyen', 'alexander.nguyen@cmich.edu', '+1098765432', 'Employee Manager', '2024-03-01', '2627 Lemon St', 'Broadway', 'Atlanta', 'GA', '30301'),
    (230, 'EMP_031', 'Test@12345', 'Charlotte', 'Kim', 'charlotte.kim@cmich.edu', '+1234567890', 'Employee Manager', '2024-03-15', '2728 Lime St', 'Lincoln St', 'Boston', 'MA', '02101');

# CREATING SKILL TABLE
DROP TABLE IF EXISTS SKILL;
CREATE TABLE SKILL (
    SKILL_ID INT PRIMARY KEY,
    SKILL_NAME VARCHAR(100),
    SKILL_DESC TEXT
);

# INSERTING VALUES INTO SKILL TABLE
INSERT INTO SKILL (SKILL_ID, SKILL_NAME, SKILL_DESC)
VALUES
    (1, 'Facilities Maintenance', 'Experience in maintaining and repairing various building components and systems, including roofs, exterior walls, windows, floors, and interior walls.'),
    (2, 'HVAC Systems Management', 'Knowledge of heating, ventilation, and air conditioning (HVAC) systems maintenance and troubleshooting.'),
    (3, 'Electrical Systems Maintenance', 'Experience in maintaining electrical systems in buildings, including wiring, outlets, and lighting fixtures.'),
    (4, 'Plumbing Maintenance', 'Skilled in plumbing maintenance and repairs for commercial and residential properties.'),
    (5, 'Building Security Management', 'Knowledge of building security systems and procedures to ensure the safety and security of occupants.'),
    (6, 'Emergency Response Planning', 'Experience in developing and implementing emergency response plans for facilities, including evacuation procedures and disaster preparedness.'),
    (7, 'Fire Safety Management', 'Understanding of fire safety regulations and procedures, including fire alarm systems and evacuation protocols.'),
    (8, 'Waste Management', 'Experience in managing waste disposal and recycling programs for facilities.'),
    (9, 'Space Planning', 'Ability to plan and optimize space utilization within buildings and facilities.'),
    (10, 'Inventory Management', 'Experience in inventory management and procurement for facilities maintenance supplies.'),
    (11, 'Energy Efficiency Management', 'Knowledge of energy-efficient practices and technologies for reducing utility costs in buildings.'),
    (12, 'Budget Management', 'Experience in budgeting and financial management for facilities maintenance operations.'),
    (13, 'Contract Management', 'Ability to negotiate and manage contracts with vendors and service providers for facility maintenance services.'),
    (14, 'Custodial Services Management', 'Experience in managing custodial staff and services for facility cleanliness and sanitation.'),
    (15, 'Groundskeeping', 'Experience in landscaping and groundskeeping maintenance for exterior areas of facilities.'),
    (16, 'Tenant Relations', 'Ability to maintain positive relationships with tenants and address their needs and concerns effectively.'),
    (17, 'Asset Management', 'Experience in tracking and maintaining facility assets and equipment.'),
    (18, 'Health and Safety Compliance', 'Knowledge of health and safety regulations and practices to ensure compliance in facility operations.'),
    (19, 'Teamwork', 'Effective collaboration and teamwork abilities for coordinating facility maintenance tasks with colleagues.'),
    (20, 'Problem-Solving Skills', 'Ability to identify and solve maintenance issues and challenges efficiently and effectively.'),
    (21, 'Communication Skills', 'Strong verbal and written communication skills for interacting with stakeholders and team members.'),
    (22, 'Project Management', 'Experience in planning, coordinating, and executing facility maintenance projects.'),
    (23, 'Quality Assurance', 'Implementation of quality assurance measures to maintain high standards in facility maintenance.'),
    (24, 'Safety Inspections', 'Conducting regular safety inspections to identify and address potential hazards in facilities.'),
    (25, 'Risk Assessment', 'Ability to assess risks and develop strategies to mitigate potential hazards in facilities.'),
    (26, 'Supervision and Leadership', 'Experience in supervising and leading facility maintenance teams to achieve organizational goals.'),
    (27, 'Regulatory Compliance', 'Understanding and adherence to regulatory requirements and compliance standards in facility operations.'),
    (28, 'Vendor Management', 'Managing relationships with vendors and contractors for facility maintenance services.'),
    (29, 'Equipment Maintenance', 'Experience in maintaining and servicing equipment used in facility maintenance activities.'),
    (30, 'Customer Service', 'Providing excellent customer service to building occupants and addressing their needs and concerns promptly.');

# CREATING EMPLOYEE_SKILL
DROP TABLE IF EXISTS EMPLOYEE_SKILL;
CREATE TABLE EMPLOYEE_SKILL (
    EMP_ID INT,
    SKILL_ID INT,
    FOREIGN KEY (EMP_ID) REFERENCES EMPLOYEE(EMP_ID),
    FOREIGN KEY (SKILL_ID) REFERENCES SKILL(SKILL_ID)
);

# INSERTING VALUES INTO EMPLOYEE SKILL
INSERT INTO EMPLOYEE_SKILL (SKILL_ID, EMP_ID)
VALUES
    (1, 201),
    (2, 202),
    (3, 203),
    (4, 204),
    (5, 205),
    (6, 206),
    (7, 207),
    (8, 208),
    (9, 209),
    (10, 210),
    (11, 211),
    (12, 212),
    (13, 213),
    (14, 214),
    (15, 215),
    (16, 216),
    (17, 217),
    (18, 218),
    (19, 219),
    (20, 220),
    (21, 221),
    (22, 222),
    (23, 223),
    (24, 224),
    (25, 225),
    (26, 226),
    (27, 227),
    (28, 228),
    (29, 229),
    (30, 230);
    

# CREATING FM DEPT TABLE
DROP TABLE IF EXISTS FM_DEPARTMENT;
CREATE TABLE FM_DEPARTMENT (
    FM_ID INT PRIMARY KEY,
    FM_DEPTNAME VARCHAR(100),
    FM_DEPTLOC VARCHAR(100)
);

# INSERT VALUES INTO FM_DEPARTMENT
INSERT INTO FM_DEPARTMENT (FM_ID, FM_DEPTNAME)
VALUES 
    (301, 'Maintenance Department'),
    (302, 'Repair Department'),
    (303, 'Security Department'),
    (304, 'Landscaping Department'),
    (305, 'Emergency Response Department'),
    (306, 'Electrical Systems Department'),
    (307, 'HVAC Systems Department'),
    (308, 'Plumbing Systems Department'),
    (309, 'Fire Safety Department'),
    (310, 'Building Exterior Department'),
    (311, 'Building Interior Department'),
    (312, 'Water Systems Department'),
    (313, 'Sanitary Systems Department'),
    (314, 'Mechanical Systems Department'),
    (315, 'Parking Facilities Department'),
    (316, 'Road Maintenance Department'),
    (317, 'Storm Sewer Systems Department'),
    (318, 'Lighting Systems Department'),
    (319, 'Waste Management Department'),
    (320, 'Emergency Preparedness Department'),
    (321, 'Budget Management Department'),
    (322, 'Contract Management Department'),
    (323, 'Regulatory Compliance Department'),
    (324, 'Risk Assessment Department'),
    (325, 'Customer Service Department'),
    (326, 'Project Management Department'),
    (327, 'Quality Assurance Department'),
    (328, 'Health and Safety Compliance Department'),
    (329, 'Team Leadership Department'),
    (330, 'Communication Skills Department');
    
    #CREATING EMPLOYEE_DEPARTMENT TABLE
DROP TABLE IF EXISTS EMP_DEPARTMENT;
CREATE TABLE EMP_DEPARTMENT (
    EMP_ID INT,
    FM_ID INT,
    FOREIGN KEY (EMP_ID) REFERENCES EMPLOYEE(EMP_ID),
    FOREIGN KEY (FM_ID) REFERENCES FM_DEPARTMENT(FM_ID),
    PRIMARY KEY (EMP_ID, FM_ID)
);
# INSERT  VALUES INTO EMPLOYEE_DEPARTMENT
INSERT INTO EMP_DEPARTMENT (EMP_ID, FM_ID)
VALUES 
    (201, 301),
    (202, 302),
    (203, 303),
    (204, 304),
    (205, 305),
    (206, 306),
    (207, 307),
    (208, 308),
    (209, 309),
    (210, 310),
    (211, 311),
    (212, 312),
    (213, 313),
    (214, 314),
    (215, 315),
    (216, 316),
    (217, 317),
    (218, 318),
    (219, 319),
    (220, 320),
    (221, 321),
    (222, 322),
    (223, 323),
    (224, 324),
    (225, 325),
    (226, 326),
    (227, 327),
    (228, 328),
    (229, 329),
    (230, 330);
    
# CREATING CATEGORY TABLE
DROP TABLE IF EXISTS CATEGORY;
CREATE TABLE CATEGORY (
    CAT_ID INT PRIMARY KEY,
    CAT_NAME VARCHAR(100),
    FM_ID INT,
    FOREIGN KEY (FM_ID) REFERENCES FM_DEPARTMENT(FM_ID)
);

# INSERT VALUES INTO CATEGORY TABLE
INSERT INTO CATEGORY (CAT_ID, CAT_NAME, FM_ID)
VALUES
    (1, 'Maintenance', 301),
    (2, 'Repair', 302),
    (3, 'Security', 303),
    (4, 'Landscaping', 304),
    (5, 'Emergency Response', 305),
    (6, 'Electrical Systems', 306),
    (7, 'HVAC Systems', 307),
    (8, 'Plumbing Systems', 308),
    (9, 'Fire Safety', 309),
    (10, 'Building Exterior', 310),
    (11, 'Building Interior', 311),
    (12, 'Water Systems', 312),
    (13, 'Sanitary Systems', 313),
    (14, 'Mechanical Systems', 314),
    (15, 'Parking Facilities', 315),
    (16, 'Road Maintenance', 316),
    (17, 'Storm Sewer Systems', 317),
    (18, 'Lighting Systems', 318),
    (19, 'Waste Management', 319),
    (20, 'Emergency Preparedness', 320),
    (21, 'Budget Management', 321),
    (22, 'Contract Management', 322),
    (23, 'Regulatory Compliance', 323),
    (24, 'Risk Assessment', 324),
    (25, 'Customer Service', 325),
    (26, 'Project Management', 326),
    (27, 'Quality Assurance', 327),
    (28, 'Health and Safety Compliance', 328),
    (29, 'Team Leadership', 329),
    (30, 'Communication Skills', 330);
    


# CREATING TASK TABLE
DROP TABLE IF EXISTS TASK;
CREATE TABLE TASK (
    TASK_ID INT AUTO_INCREMENT PRIMARY KEY,
    REQ_ID INT,
    ASSGND_BY_EMP_ID INT,
    ASSGND_TO_EMP_ID INT, 
    CAT_ID INT,
    TASK_DESC TEXT,
    TASK_SEVERITY VARCHAR(20),
    TASK_STATUS VARCHAR(20),
    TASK_STARTDT DATE,
    TASK_ENDDT DATE,
   FOREIGN KEY (REQ_ID) REFERENCES REQUESTOR(REQ_ID),
    FOREIGN KEY (ASSGND_BY_EMP_ID) REFERENCES EMPLOYEE(EMP_ID),
    FOREIGN KEY (ASSGND_TO_EMP_ID) REFERENCES EMPLOYEE(EMP_ID),
    FOREIGN KEY (CAT_ID) REFERENCES CATEGORY(CAT_ID)
);

# INSERT VALUES INTO TASK TABLE
INSERT INTO TASK (TASK_ID, REQ_ID, ASSGND_BY_EMP_ID, ASSGND_TO_EMP_ID, CAT_ID, TASK_DESC, TASK_SEVERITY, TASK_STATUS, TASK_STARTDT, TASK_ENDDT)
VALUES
    (1, 1, 201, 207, 1, 'Inspect and repair HVAC system in building A', 'High', 'Open', '2024-03-21', NULL),
    (2, 2, 202, 214, 2, 'Fix plumbing issue in restroom on the 2nd floor', 'Medium', 'In Progress', '2024-03-20', NULL),
    (3, 3, 203, 219, 3, 'Mow lawn and trim trees in the campus garden', 'Low', 'Completed', '2024-03-19', '2024-03-19'),
    (4, 4, 204, 209, 4, 'Test fire alarm systems in all buildings', 'High', 'Open', '2024-03-18', NULL),
    (5, 5, 205, 229, 5, 'Address security issue in parking lot C', 'High', 'In Progress', '2024-03-17', NULL),
    (6, 6, 206, 228, 6, 'Repair electrical wiring in room 101', 'Medium', 'Completed', '2024-03-16', '2024-03-16'),
    (7, 7, 207, 226, 7, 'Install new lighting fixtures in the hallway', 'Low', 'Open', '2024-03-15', NULL),
    (8, 8, 208, 224, 8, 'Inspect storm sewer systems on campus', 'Medium', 'In Progress', '2024-03-14', NULL),
    (9, 9, 209, 208, 9, 'Paint exterior walls of building B', 'Medium', 'Completed', '2024-03-13', '2024-03-13'),
    (10, 10, 210, 202, 10, 'Repair leaking pipes in the basement', 'High', 'Open', '2024-03-12', NULL),
    (11, 11, 211, 209, 1, 'Replace HVAC filters in building C', 'Low', 'Completed', '2024-03-11', '2024-03-11'),
    (12, 12, 212, 207, 2, 'Unclog drains in restroom on the 3rd floor', 'Medium', 'In Progress', '2024-03-10', NULL),
    (13, 13, 213, 206, 3, 'Prune trees near the entrance gate', 'Low', 'Completed', '2024-03-09', '2024-03-09'),
    (14, 14, 214, 206, 4, 'Test fire extinguishers in all classrooms', 'High', 'Open', '2024-03-08', NULL),
    (15, 15, 215, 207, 5, 'Investigate vandalism report near the library', 'High', 'In Progress', '2024-03-07', NULL),
    (16, 16, 216, 214, 6, 'Replace faulty light switches in the gymnasium', 'Medium', 'Completed', '2024-03-06', '2024-03-06'),
    (17, 17, 217, 219, 7, 'Upgrade emergency exit signs in the auditorium', 'Low', 'Open', '2024-03-05', NULL),
    (18, 18, 218, 214, 8, 'Clean storm drains along the main road', 'Medium', 'In Progress', '2024-03-04', NULL),
    (19, 19, 219, 219, 9, 'Touch up paint on benches in the park', 'Low', 'Completed', '2024-03-03', '2024-03-03'),
    (20, 20, 220, 214, 10, 'Repair broken sidewalk near the cafeteria', 'High', 'Open', '2024-03-02', NULL),
    (21, 21, 221, 219, 1, 'Inspect and repair heating system in the gym', 'High', 'Open', '2024-03-01', NULL),
    (22, 22, 222, 214, 2, 'Fix leaking faucet in the administrative office', 'Medium', 'In Progress', '2024-02-29', NULL),
    (23, 23, 223, 219, 3, 'Mow lawn and trim bushes around the library', 'Low', 'Completed', '2024-02-28', '2024-02-28'),
    (24, 24, 224, 224, 4, 'Test emergency lighting in the lecture halls', 'High', 'Open', '2024-02-27', NULL),
    (25, 25, 225, 229, 5, 'Investigate strange odor in the chemistry lab', 'High', 'In Progress', '2024-02-26', NULL),
    (26, 26, 226, 204, 6, 'Replace burnt-out bulbs in the parking garage', 'Medium', 'Completed', '2024-02-25', '2024-02-25'),
    (27, 27, 227, 209, 7, 'Install new HVAC filters in the cafeteria', 'Low', 'Open', '2024-02-24', NULL),
    (28, 28, 228, 204, 8, 'Clean gutters on the dormitory buildings', 'Medium', 'In Progress', '2024-02-23', NULL),
    (29, 29, 229, 209, 9, 'Repaint crosswalk lines on campus roads', 'Low', 'Completed', '2024-02-22', '2024-02-22'),
    (30, 30, 230, 204, 10, 'Repair damaged fence around the athletic field', 'High', 'Open', '2024-02-21', NULL);

# CREATING TASK UPDATE TABLE
DROP TABLE IF EXISTS TASK_UPDATE;
CREATE TABLE TASK_UPDATE (
    UPDATE_ID INT PRIMARY KEY,
    TASK_ID INT,
    EMP_ID INT,
    UPDATE_INFO TEXT,
    UPDATE_DATE DATE,
    FOREIGN KEY (TASK_ID) REFERENCES TASK(TASK_ID),
    FOREIGN KEY (EMP_ID) REFERENCES EMPLOYEE(EMP_ID)
);

# INSERTING VALUES INTO TASK_UPDATE TABLE
INSERT INTO TASK_UPDATE (UPDATE_ID, TASK_ID, EMP_ID, UPDATE_INFO, UPDATE_DATE)
VALUES
    (1001, 1, 201, 'Completed routine maintenance on building HVAC systems.', '2024-03-21'),
    (1002, 2, 202, 'Repaired plumbing issues in restroom facilities.', '2024-03-20'),
    (1003, 3, 203, 'Performed groundskeeping tasks including lawn mowing and tree trimming.', '2024-03-19'),
    (1004, 4, 204, 'Conducted fire safety inspection and tested fire alarm systems.', '2024-03-18'),
    (1005, 5, 205, 'Responded to emergency call and addressed building security issue.', '2024-03-17'),
    (1006, 6, 206, 'Completed electrical repair work in building interior.', '2024-03-16'),
    (1007, 7, 207, 'Installed new exterior lighting fixtures for enhanced security.', '2024-03-15'),
    (1008, 8, 208, 'Performed routine inspection of storm sewer systems.', '2024-03-14'),
    (1009, 9, 209, 'Completed painting and touch-up work on building exteriors.', '2024-03-13'),
    (1010, 10, 210, 'Responded to water leak and repaired damaged pipes.', '2024-03-12'),
    (1011, 11, 211, 'Conducted preventive maintenance on chilled water systems.', '2024-03-11'),
    (1012, 12, 212, 'Inspected and maintained campus electrical distribution systems.', '2024-03-10'),
    (1013, 13, 213, 'Performed routine inspection of parking lot signage.', '2024-03-09'),
    (1014, 14, 214, 'Responded to HVAC system malfunction and restored functionality.', '2024-03-08'),
    (1015, 15, 215, 'Completed landscaping work including planting flowers and shrubs.', '2024-03-07'),
    (1016, 16, 216, 'Inspected and repaired building roofs for leaks and damages.', '2024-03-06'),
    (1017, 17, 217, 'Conducted routine maintenance on building plumbing systems.', '2024-03-05'),
    (1018, 18, 218, 'Installed new curbs and gutters along campus roadways.', '2024-03-04'),
    (1019, 19, 219, 'Performed routine inspection of sanitary sewer systems.', '2024-03-03'),
    (1020, 20, 220, 'Repaired broken sidewalk sections for improved pedestrian safety.', '2024-03-02'),
    (1021, 21, 221, 'Completed interior lighting upgrade for energy efficiency improvement.', '2024-03-01'),
    (1022, 22, 222, 'Conducted preventive maintenance on building mechanical systems.', '2024-02-29'),
    (1023, 23, 223, 'Performed routine inspection of campus exterior lighting.', '2024-02-28'),
    (1024, 24, 224, 'Responded to emergency call and addressed building security issue.', '2024-02-27'),
    (1025, 25, 225, 'Completed electrical repair work in building interior.', '2024-02-26'),
    (1026, 26, 226, 'Installed new exterior lighting fixtures for enhanced security.', '2024-02-25'),
    (1027, 27, 227, 'Performed routine inspection of storm sewer systems.', '2024-02-24'),
    (1028, 28, 228, 'Completed painting and touch-up work on building exteriors.', '2024-02-23'),
    (1029, 29, 229, 'Responded to water leak and repaired damaged pipes.', '2024-02-22'),
    (1030, 30, 230, 'Conducted preventive maintenance on chilled water systems.', '2024-02-21');

ALTER TABLE TASK
ADD COLUMN ASSGND_BY_EMP_ID INT NULL,
ADD COLUMN ASSGND_TO_EMP_ID INT NULL; 

ALTER TABLE TASK
ADD FOREIGN KEY (REQ_ID) REFERENCES REQUESTOR(REQ_ID),
ADD FOREIGN KEY (CAT_ID) REFERENCES CATEGORY(CAT_ID);


ALTER TABLE requestor
ADD COLUMN BUILD_ID int,
ADD COLUMN FLOOR_ID int,
ADD FOREIGN KEY (BUILD_ID) REFERENCES building(BUILD_ID),
ADD FOREIGN KEY (FLOOR_ID) REFERENCES floor(FLOOR_ID);
