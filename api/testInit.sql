-- delete all data for seeding
SET FOREIGN_KEY_CHECKS = 0;
TRUNCATE TABLE conferenceapplication;
TRUNCATE TABLE report;
TRUNCATE TABLE applicationcode;
TRUNCATE TABLE apikey;
TRUNCATE TABLE usersecret;
TRUNCATE TABLE workshopapplication;
TRUNCATE TABLE workshopattendee;
TRUNCATE TABLE workshop;
TRUNCATE TABLE travel;
TRUNCATE TABLE votinganswer;
TRUNCATE TABLE votingquestion;
TRUNCATE TABLE userroleassignment;
TRUNCATE TABLE user;
TRUNCATE TABLE sensible;
TRUNCATE TABLE role;
TRUNCATE TABLE council;
TRUNCATE TABLE conference;
TRUNCATE TABLE applicationtype;
SET FOREIGN_KEY_CHECKS = 1;


-- Inserting an application type
INSERT INTO applicationtype (name,goIsAllowed)
VALUES ('Application Type A',True);

-- Inserting another application type
INSERT INTO applicationtype (name,goIsAllowed)
VALUES ('Application Type B',False);

-- Inserting another application type
INSERT INTO applicationtype (name,goIsAllowed)
VALUES ('Application Type C',False);

-- Inserting a conference record
INSERT INTO conference (name, startdate, enddate, participationagreement, arrivedcouncils, conferenceapplicationphase, workshopapplicationphase, workshopsuggestionphase, texts, dropdowns)
VALUES (
    'conference 1',
    '2023-10-10 08:00:00',
    '2023-10-12 18:00:00',
    'Agreement content for conference 1',
    10,
    '{"start": "2023-09-01", "end": "2023-09-30"}',
    '{"start": "2023-09-15", "end": "2023-09-25"}',
    '{"start": "2023-08-20", "end": "2023-08-30"}',
    '{"welcome_text": "Welcome to conference 1", "about_text": "About conference 1"}',
    '{"dropdown1": ["value1", "value2"], "dropdown2": ["optionA", "optionB"]}'
);

-- Inserting another conference record
INSERT INTO conference (name, startdate, enddate, participationagreement, arrivedcouncils, conferenceapplicationphase, workshopapplicationphase, workshopsuggestionphase, texts, dropdowns)
VALUES (
    'conference 2',
    '2023-11-15 09:00:00',
    '2023-11-18 17:00:00',
    'Agreement content for conference 2',
    15,
    '{"start": "2023-10-10", "end": "2023-11-01"}',
    '{"start": "2023-10-25", "end": "2023-11-10"}',
    '{"start": "2023-10-15", "end": "2023-10-30"}',
    '{"welcome_text": "Welcome to conference 2", "about_text": "About conference 2"}',
    '{"dropdown1": ["value3", "value4"], "dropdown2": ["optionC", "optionD"]}'
);

-- Inserting another conference record
INSERT INTO conference (name, startdate, enddate, participationagreement, arrivedcouncils, conferenceapplicationphase, workshopapplicationphase, workshopsuggestionphase, texts, dropdowns)
VALUES (
    'conference 3',
    '2024-01-05 10:00:00',
    '2024-01-08 20:00:00',
    'Agreement content for conference 3',
    20,
    '{"start": "2023-12-01", "end": "2023-12-31"}',
    '{"start": "2023-12-15", "end": "2023-12-28"}',
    '{"start": "2023-12-10", "end": "2023-12-25"}',
    '{"welcome_text": "Welcome to conference 3", "about_text": "About conference 3"}',
    '{"dropdown1": ["value5", "value6"], "dropdown2": ["optionE", "optionF"]}'
);

-- Inserting a council record for a German university
INSERT INTO council (name, zip, city, university, street, isblocked)
VALUES ('Student council - University of Munich', 80333, 'Munich', 'University of Munich', 'Geschwister-Scholl-Platz 1', 0);

-- Inserting a council record for a German university
INSERT INTO council (name, zip, city, university, street, isblocked)
VALUES ('Student council - Technical University of Munich', 80333, 'Munich', 'Technical University of Munich', 'Arcisstraße 21', 0);

-- Inserting a council record for a German university
INSERT INTO council (name, zip, city, university, street, isblocked)
VALUES ('Student council - Ludwig Maximilian University of Munich', 80539, 'Munich', 'Ludwig Maximilian University of Munich', 'Geschwister-Scholl-Platz 1', 0);

-- Inserting a council record for a German university
INSERT INTO council (name, zip, city, university, street, isblocked)
VALUES ('Student council - Humboldt University of Berlin', 10115, 'Berlin', 'Humboldt University of Berlin', 'Unter den Linden 6', 0);

-- Inserting a council record for a German university
INSERT INTO council (name, zip, city, university, street, isblocked)
VALUES ('Student council - Technical University of Berlin', 10623, 'Berlin', 'Technical University of Berlin', 'Straße des 17. Juni 135', 0);

-- Inserting a council record for a German university
INSERT INTO council (name, zip, city, university, street, isblocked)
VALUES ('Student council - University of Hamburg', 20146, 'Hamburg', 'University of Hamburg', 'Edmund-Siemers-Allee 1', 0);

-- Inserting a council record for a German university
INSERT INTO council (name, zip, city, university, street, isblocked)
VALUES ('Student council - University of Cologne', 50923, 'Cologne', 'University of Cologne', 'Albertus-Magnus-Platz', 0);

-- Inserting a council record for a German university
INSERT INTO council (name, zip, city, university, street, isblocked)
VALUES ('Student council - Goethe University Frankfurt', 60323, 'Frankfurt', 'Goethe University Frankfurt', 'Theodor-W.-Adorno-Platz 1', 0);

-- Inserting a council record for a German university
INSERT INTO council (name, zip, city, university, street, isblocked)
VALUES ('Student council - University of Stuttgart', 70174, 'Stuttgart', 'University of Stuttgart', 'Keplerstraße 7', 0);

-- Inserting a council record for a German university
INSERT INTO council (name, zip, city, university, street, isblocked)
VALUES ('Student council - University of Heidelberg', 69117, 'Heidelberg', 'University of Heidelberg', 'Grabengasse 1', 0);
-- Inserting a user role
INSERT INTO role (name) VALUES ('User');

-- Inserting an admin role
INSERT INTO role (name) VALUES ('Admin');

-- Inserting a council role
INSERT INTO role (name) VALUES ('Council');

-- Inserting a host role
INSERT INTO role (name) VALUES ('Host');

-- Test data for the Sensible db table
INSERT INTO sensible (sex, street, zip, city, comment, sleepingpreference, eatingpreference, intolerances, phone, conferencecount, accomodation)
VALUES
  ('Male', '123 Main Street', 12345, 'New York', 'No special comments', 'Early riser', 'Vegetarian', 'None', '555-123-4567', 3, '{"type": "hotel", "name": "Hotel ABC", "address": "456 Elm Street"}'),
  ('Female', '456 Elm Street', 67890, 'Los Angeles', 'Allergic to nuts', 'Night owl', 'Vegan', 'Nuts', '555-987-6543', 2, '{"type": "apartment", "name": "City View Apartments", "address": "789 Oak Avenue"}'),
  ('Male', '789 Oak Avenue', 54321, 'Chicago', 'Lactose intolerant', 'Early riser', 'Omnivore', 'Dairy', '555-345-6789', 4, '{"type": "hostel", "name": "Downtown Hostel", "address": "101 Pine Street"}'),
  ('Female', '101 Pine Street', 98765, 'San Francisco', 'No special comments', 'Night owl', 'Vegetarian', 'None', '555-789-0123', 1, '{"type": "hotel", "name": "Luxury Hotel", "address": "111 River Road"}'),
  ('Male', '111 River Road', 13579, 'Miami', 'Allergic to seafood', 'Early riser', 'Omnivore', 'Seafood', '555-234-5678', 2, '{"type": "apartment", "name": "Beachside Apartments", "address": "222 Beach Blvd"}');

-- Test data for the User db table
INSERT INTO user (email, firstname, lastname, councilid, birthday, status)
VALUES
  ('user1@example.com', 'John', 'Doe', 1, '1990-03-15', 'Active'),
  ('user2@example.com', 'Jane', 'Smith', 1, '1985-07-22', 'Active'),
  ('user3@example.com', 'Bob', 'Johnson', 2, '1995-11-10', 'Inactive'),
  ('user4@example.com', 'Alice', 'Brown', 2, '1988-04-05', 'Active'),
  ('user5@example.com', 'Chris', 'Lee', 3, '1992-09-30', 'Active');

-- Test data for UserRoleAssignment db table 
INSERT INTO userroleassignment (userid, roleid, conferenceid)
VALUES
  (1, 1, 1),
  (2, 2, 2),
  (3, 3, 1),
  (4, 1, 3),
  (5, 2, 1);

-- Test data for VotingQuestion db table
INSERT INTO votingquestion (conferenceid, type, questiontext, arrivedcouncilcount, isopen, issecret, resolvedon, votingoptions, votes, result)
VALUES
  (1, 'Multiple Choice', 'What should be the conference theme?', 5, true, false, '2023-10-15 18:00:00', '["Option A", "Option B", "Option C"]', '{"Option A": 3, "Option B": 2, "Option C": 0}', 'Option A'),
  (1, 'Yes/No', 'Should we extend conference hours?', 5, true, false, '2023-10-16 12:00:00', '["Yes", "No"]', '{"Yes": 4, "No": 1}', 'Yes'),
  (2, 'Multiple Choice', 'Select the venue for the conference dinner', 4, true, false, '2023-10-18 15:00:00', '["Venue X", "Venue Y", "Venue Z"]', '{"Venue X": 2, "Venue Y": 2, "Venue Z": 0}', 'Venue X'),
  (2, 'Yes/No', 'Should we provide shuttle service?', 4, true, false, '2023-10-20 09:00:00', '["Yes", "No"]', '{"Yes": 3, "No": 1}', 'Yes'),
  (3, 'Multiple Choice', 'Select the keynote speaker', 3, true, false, '2023-10-22 14:00:00', '["Speaker A", "Speaker B", "Speaker C"]', '{"Speaker A": 2, "Speaker B": 1, "Speaker C": 0}', 'Speaker A');

-- Test data for VotingAnswer db table
INSERT INTO votinganswer (questionid, councilid, priority, vote)
VALUES
  (1, 1, 1, 'Option A'),
  (1, 2, 2, 'Option B'),
  (2, 3, 1, 'Option C'),
  (2, 4, 2, 'Option D'),
  (3, 5, 1, 'Option E');

  -- Test data for the Travel db table
INSERT INTO travel (conferenceid, userid, transportation, parkingspace, arrivaltimestamp, arrivalplace, departuretimestamp, note)
VALUES
  (1, 1, 'Car', 1, '2023-09-25 08:00:00', 'conference Center', '2023-09-30 18:00:00', 'Driving from home'),
  (1, 2, 'Train', 2, '2023-09-26 10:30:00', 'Train Station', '2023-10-01 15:45:00', 'Taking the express train'),
  (2, 3, 'Plane', 3, '2023-09-27 14:15:00', 'Airport', '2023-10-02 12:30:00', 'Flying in a day early'),
  (2, 4, 'Bus', 4, '2023-09-28 16:45:00', 'Bus Station', '2023-10-03 14:20:00', 'Group bus ride'),
  (3, 5, 'Car', 5, '2023-09-29 09:30:00', 'Hotel', '2023-10-04 17:30:00', 'Parking included');

-- Test data for Workshop db table
INSERT INTO workshop (conferenceid, name, shortname, overview, maxvisitors, difficulty, place, start, duration, note, hostisexternal, hostname)
VALUES
  (1, 'Introduction to Python Programming', 'Python Intro', 'A beginner-friendly workshop on Python programming.', 30, 'Beginner', 'Room A', '2023-10-10 09:00:00', 120, 'Bring your laptop.', false, 'John Doe'),
  (1, 'Advanced Data Analysis with Pandas', 'Pandas Analysis', 'A hands-on workshop for data analysis using Pandas.', 20, 'Intermediate', 'Room B', '2023-10-12 13:30:00', 90, 'Prerequisite: Basic Python knowledge.', false, 'Jane Smith'),
  (2, 'Web Development with React', 'React Dev', 'Learn to build web applications with React.', 25, 'Intermediate', 'Room C', '2023-10-15 10:00:00', 150, 'Bring your laptop and install Node.js.', true, 'External Company A'),
  (2, 'Machine Learning Workshop', 'ML Workshop', 'Explore machine learning algorithms and techniques.', 15, 'Advanced', 'Room D', '2023-10-18 14:00:00', 180, 'Prerequisite: Basic machine learning knowledge.', false, 'Alice Brown'),
  (3, 'Introduction to SQL Databases', 'SQL Intro', 'A beginners guide to SQL databases and queries.', 30, 'Beginner', 'Room E', '2023-10-20 11:00:00', 120, 'No prior knowledge required.', true, 'External Company B');

-- Test data for WorkshopApplication db table
INSERT INTO workshopapplication (workshopid, userid, priority, ishost)
VALUES
  (1, 1, 1, false),
  (1, 2, 2, false),
  (2, 3, 1, false),
  (2, 4, 2, true),
  (3, 5, 1, false);

-- Test data for WorkshopAttendandee db table
INSERT INTO workshopattendee (workshopid, userid, ishost)
VALUES
  (1, 1, false),
  (1, 2, false),
  (2, 3, true),
  (3, 4, false),
  (3, 5, false);

-- Test data for UserSecret db table with standard password "admin"
INSERT INTO usersecret (userid, password, registrationtoken, registrationtokenvaliduntil)
VALUES
  (1, '$2b$12$PszEt9WwCr9kpZhFt5IYNOF3rTgjStqnoWl/T78xIi.9AJW9gPhQ.', 'token1', '2023-10-01 12:00:00'),
  (2, '$2b$12$PszEt9WwCr9kpZhFt5IYNOF3rTgjStqnoWl/T78xIi.9AJW9gPhQ.', 'token2', '2023-10-02 14:00:00'),
  (3, '$2b$12$PszEt9WwCr9kpZhFt5IYNOF3rTgjStqnoWl/T78xIi.9AJW9gPhQ.', 'token3', '2023-10-03 16:00:00'),
  (4, '$2b$12$PszEt9WwCr9kpZhFt5IYNOF3rTgjStqnoWl/T78xIi.9AJW9gPhQ.', 'token4', '2023-10-04 18:00:00'),
  (5, '$2b$12$PszEt9WwCr9kpZhFt5IYNOF3rTgjStqnoWl/T78xIi.9AJW9gPhQ.', 'token5', '2023-10-05 20:00:00');

-- Inserting an API key for User 1
INSERT INTO apikey (apikey, note, createdon, validuntil, userid)
VALUES ('abc123', 'API Key for User 1', '2023-09-23', '2025-12-31', 1);

-- Inserting an API key for User 2
INSERT INTO apikey (apikey, note, createdon, validuntil, userid)
VALUES ('xyz456', 'API Key for User 2', '2023-09-24', '2025-12-31', 2);

-- Inserting an API key for User 3
INSERT INTO apikey (apikey, note, createdon, validuntil, userid)
VALUES ('qwerty', 'API Key for User 3', '2023-09-25', '2025-10-31', 3);

-- Inserting an API key without expiry for User 1
INSERT INTO apikey (apiKey, note, createdOn, validuntil, userId)
VALUES ('noexpiry', 'API Key with no expiry for User 1', '2023-09-26', '2025-09-26', 1);

-- Inserting an API key with an empty note for User 2
INSERT INTO apikey (apikey, note, createdon, validuntil, userid)
VALUES ('emptynote', '', '2023-09-27', '2025-11-30', 2);

-- Inserting an application code for conference 1, council 1, application type 1
INSERT INTO applicationcode (conferenceid, councilid, priority, code, isused, applicationtypeid)
VALUES (1, 1, 1, 'ABC123', 0, 1);

-- Inserting an application code for conference 2, council 2, application type 2
INSERT INTO applicationcode (conferenceid, councilid, priority, code, isused, applicationtypeid)
VALUES (2, 2, 2, 'XYZ456', 1, 2);

-- Inserting an application code for conference 1, council 2, application type 1
INSERT INTO applicationcode (conferenceid, councilid, priority, code, isused, applicationtypeid)
VALUES (1, 2, 3, 'DEF789', 0, 1);

-- Inserting an application code for conference 3, council 3, application type 3
INSERT INTO applicationcode (conferenceid, councilid, priority, code, isused, applicationtypeid)
VALUES (3, 3, 1, 'GHI456', 1, 3);

-- Inserting an application code for conference 2, council 1, application type 2
INSERT INTO applicationcode (conferenceid, councilid, priority, code, isused, applicationtypeid)
VALUES (2, 1, 2, 'JKL789', 0, 2);

-- Inserting an application code for conference 3, council 1, application type 1
INSERT INTO applicationcode (conferenceid, councilid, priority, code, isused, applicationtypeid)
VALUES (3, 1, 1, 'MNO123', 0, 1);

-- Inserting an application code for conference 2, council 3, application type 2
INSERT INTO applicationcode (conferenceid, councilid, priority, code, isused, applicationtypeid)
VALUES (2, 3, 2, 'PQR456', 1, 2);

-- Inserting an application code for conference 1, council 3, application type 3
INSERT INTO applicationcode (conferenceid, councilid, priority, code, isused, applicationtypeid)
VALUES (1, 3, 3, 'STU789', 0, 3);

-- Inserting a report for a user
INSERT INTO report (userid, reporttype, reportstatus, reporttime, reportapplicationinfo)
VALUES (1, 1, 1, '2023-10-05 08:45:00', 'report for application XYZ');

-- Inserting a report for a user
INSERT INTO report (userid, reporttype, reportstatus, reporttime, reportapplicationinfo)
VALUES (2, 2, 2, '2023-10-10 14:30:00', 'report for application ABC');

-- Inserting a report for a user
INSERT INTO report (userid, reporttype, reportstatus, reporttime, reportapplicationinfo)
VALUES (3, 1, 1, '2023-10-15 16:45:00', 'report for application DEF');

-- Inserting a report for a user
INSERT INTO report (userid, reporttype, reportstatus, reporttime, reportapplicationinfo)
VALUES (4, 3, 1, '2023-10-20 10:15:00', 'report for application GHI');

-- Inserting a report for a user
INSERT INTO report (userid, reporttype, reportstatus, reporttime, reportapplicationinfo)
VALUES (5, 2, 2, '2023-11-05 09:00:00', 'report for application JKL');

-- Inserting a report for a user
INSERT INTO report (userid, reporttype, reportstatus, reporttime, reportapplicationinfo)
VALUES (1, 1, 1, '2023-11-10 12:15:00', 'report for application MNO');

-- Inserting a report for a user
INSERT INTO report (userid, reporttype, reportstatus, reporttime, reportapplicationinfo)
VALUES (2, 2, 1, '2023-11-15 15:30:00', 'report for application PQR');

-- Inserting a report for a user
INSERT INTO report (userid, reporttype, reportstatus, reporttime, reportapplicationinfo)
VALUES (3, 1, 2, '2023-11-20 11:45:00', 'report for application STU');

-- Inserting a report for a user
INSERT INTO report (userid, reporttype, reportstatus, reporttime, reportapplicationinfo)
VALUES (4, 3, 1, '2023-12-05 09:30:00', 'report for application VWX');

-- Inserting a report for a user
INSERT INTO report (userid, reporttype, reportstatus, reporttime, reportapplicationinfo)
VALUES (5, 2, 1, '2023-12-10 13:00:00', 'report for application YZA');

-- Inserting a conference application record
INSERT INTO conferenceapplication (userid, conferenceid, timestamp, priority, sensibleid, councilid, status, isallowedtovote, applicationtypeid)
VALUES (1, 1, '2023-10-05 10:00:00', 1, NULL, 1, 'Pending', 1, 1);

-- Inserting another conference application record
INSERT INTO conferenceapplication (userid, conferenceid, timestamp, priority, sensibleid, councilid, status, isallowedtovote, applicationtypeid)
VALUES (2, 2, '2023-10-15 14:30:00', 2, 1, 2, 'Approved', 0, 2);

-- Inserting another conference application record
INSERT INTO conferenceapplication (userid, conferenceid, timestamp, priority, sensibleid, councilid, status, isallowedtovote, applicationtypeid)
VALUES (3, 1, '2023-10-20 16:45:00', 3, NULL, 3, 'Pending', 1, 1);

-- Inserting another conference application record
INSERT INTO conferenceapplication (userid, conferenceid, timestamp, priority, sensibleid, councilid, status, isallowedtovote, applicationtypeid)
VALUES (4, 2, '2023-10-25 09:30:00', 4, 2, 2, 'Rejected', 1, 3);

-- Inserting another conference application record
INSERT INTO conferenceapplication (userid, conferenceid, timestamp, priority, sensibleid, councilid, status, isallowedtovote, applicationtypeid)
VALUES (5, 3, '2023-11-05 12:15:00', 1, NULL, 1, 'Approved', 0, 2);