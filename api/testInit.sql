-- Inserting an API key for User 1
INSERT INTO ApiKey (apiKey, note, createdOn, validUntil, userId)
VALUES ('abc123', 'API Key for User 1', '2023-09-23', '2023-12-31', 1);

-- Inserting an API key for User 2
INSERT INTO ApiKey (apiKey, note, createdOn, validUntil, userId)
VALUES ('xyz456', 'API Key for User 2', '2023-09-24', '2024-12-31', 2);

-- Inserting an API key for User 3
INSERT INTO ApiKey (apiKey, note, createdOn, validUntil, userId)
VALUES ('qwerty', 'API Key for User 3', '2023-09-25', '2023-10-31', 3);

-- Inserting an API key without expiry for User 1
INSERT INTO ApiKey (apiKey, note, createdOn, userId)
VALUES ('noexpiry', 'API Key with no expiry for User 1', '2023-09-26', 1);

-- Inserting an API key with an empty note for User 2
INSERT INTO ApiKey (apiKey, note, createdOn, validUntil, userId)
VALUES ('emptynote', '', '2023-09-27', '2023-11-30', 2);

-- Inserting an application code for conference 1, council 1, application type 1
INSERT INTO ApplicationCode (conferenceId, councilId, priority, code, isUsed, applicationTypeId)
VALUES (1, 1, 1, 'ABC123', 0, 1);

-- Inserting an application code for conference 2, council 2, application type 2
INSERT INTO ApplicationCode (conferenceId, councilId, priority, code, isUsed, applicationTypeId)
VALUES (2, 2, 2, 'XYZ456', 1, 2);

-- Inserting an application code for conference 1, council 2, application type 1
INSERT INTO ApplicationCode (conferenceId, councilId, priority, code, isUsed, applicationTypeId)
VALUES (1, 2, 3, 'DEF789', 0, 1);

-- Inserting an application code for conference 3, council 3, application type 3
INSERT INTO ApplicationCode (conferenceId, councilId, priority, code, isUsed, applicationTypeId)
VALUES (3, 3, 1, 'GHI456', 1, 3);

-- Inserting an application code for conference 2, council 1, application type 2
INSERT INTO ApplicationCode (conferenceId, councilId, priority, code, isUsed, applicationTypeId)
VALUES (2, 1, 2, 'JKL789', 0, 2);

-- Inserting an application code for conference 3, council 1, application type 1
INSERT INTO ApplicationCode (conferenceId, councilId, priority, code, isUsed, applicationTypeId)
VALUES (3, 1, 1, 'MNO123', 0, 1);

-- Inserting an application code for conference 2, council 3, application type 2
INSERT INTO ApplicationCode (conferenceId, councilId, priority, code, isUsed, applicationTypeId)
VALUES (2, 3, 2, 'PQR456', 1, 2);

-- Inserting an application code for conference 1, council 3, application type 3
INSERT INTO ApplicationCode (conferenceId, councilId, priority, code, isUsed, applicationTypeId)
VALUES (1, 3, 3, 'STU789', 0, 3);

-- Inserting an application type
INSERT INTO ApplicationType (name)
VALUES ('Application Type A');

-- Inserting another application type
INSERT INTO ApplicationType (name)
VALUES ('Application Type B');

-- Inserting another application type
INSERT INTO ApplicationType (name)
VALUES ('Application Type C');

-- Inserting a conference record
INSERT INTO Conference (name, startDate, endDate, participationAgreement, arrivedCouncils, conferenceApplicationPhase, workshopApplicationPhase, workshopSuggestionPhase, texts, dropdowns)
VALUES (
    'Conference 1',
    '2023-10-10 08:00:00',
    '2023-10-12 18:00:00',
    'Agreement content for Conference 1',
    10,
    '{"start": "2023-09-01", "end": "2023-09-30"}',
    '{"start": "2023-09-15", "end": "2023-09-25"}',
    '{"start": "2023-08-20", "end": "2023-08-30"}',
    '{"welcome_text": "Welcome to Conference 1", "about_text": "About Conference 1"}',
    '{"dropdown1": ["value1", "value2"], "dropdown2": ["optionA", "optionB"]}'
);

-- Inserting another conference record
INSERT INTO Conference (name, startDate, endDate, participationAgreement, arrivedCouncils, conferenceApplicationPhase, workshopApplicationPhase, workshopSuggestionPhase, texts, dropdowns)
VALUES (
    'Conference 2',
    '2023-11-15 09:00:00',
    '2023-11-18 17:00:00',
    'Agreement content for Conference 2',
    15,
    '{"start": "2023-10-10", "end": "2023-11-01"}',
    '{"start": "2023-10-25", "end": "2023-11-10"}',
    '{"start": "2023-10-15", "end": "2023-10-30"}',
    '{"welcome_text": "Welcome to Conference 2", "about_text": "About Conference 2"}',
    '{"dropdown1": ["value3", "value4"], "dropdown2": ["optionC", "optionD"]}'
);

-- Inserting another conference record
INSERT INTO Conference (name, startDate, endDate, participationAgreement, arrivedCouncils, conferenceApplicationPhase, workshopApplicationPhase, workshopSuggestionPhase, texts, dropdowns)
VALUES (
    'Conference 3',
    '2024-01-05 10:00:00',
    '2024-01-08 20:00:00',
    'Agreement content for Conference 3',
    20,
    '{"start": "2023-12-01", "end": "2023-12-31"}',
    '{"start": "2023-12-15", "end": "2023-12-28"}',
    '{"start": "2023-12-10", "end": "2023-12-25"}',
    '{"welcome_text": "Welcome to Conference 3", "about_text": "About Conference 3"}',
    '{"dropdown1": ["value5", "value6"], "dropdown2": ["optionE", "optionF"]}'
);

-- Inserting a conference application record
INSERT INTO ConferenceApplication (userId, conferenceId, timestamp, priority, sensibleId, councilId, status, isAllowedToVote, applicationTypeId)
VALUES (1, 1, '2023-10-05 10:00:00', 1, NULL, 1, 'Pending', 1, 1);

-- Inserting another conference application record
INSERT INTO ConferenceApplication (userId, conferenceId, timestamp, priority, sensibleId, councilId, status, isAllowedToVote, applicationTypeId)
VALUES (2, 2, '2023-10-15 14:30:00', 2, 1, 2, 'Approved', 0, 2);

-- Inserting another conference application record
INSERT INTO ConferenceApplication (userId, conferenceId, timestamp, priority, sensibleId, councilId, status, isAllowedToVote, applicationTypeId)
VALUES (3, 1, '2023-10-20 16:45:00', 3, NULL, 3, 'Pending', 1, 1);

-- Inserting another conference application record
INSERT INTO ConferenceApplication (userId, conferenceId, timestamp, priority, sensibleId, councilId, status, isAllowedToVote, applicationTypeId)
VALUES (4, 2, '2023-10-25 09:30:00', 4, 2, 2, 'Rejected', 1, 3);

-- Inserting another conference application record
INSERT INTO ConferenceApplication (userId, conferenceId, timestamp, priority, sensibleId, councilId, status, isAllowedToVote, applicationTypeId)
VALUES (5, 3, '2023-11-05 12:15:00', 1, NULL, 1, 'Approved', 0, 2);

-- Inserting another conference application record
INSERT INTO ConferenceApplication (userId, conferenceId, timestamp, priority, sensibleId, councilId, status, isAllowedToVote, applicationTypeId)
VALUES (6, 1, '2023-11-10 15:00:00', 2, 3, 2, 'Pending', 1, 1);

-- Inserting a council record for a German university
INSERT INTO Council (name, zip, city, university, street, isBlocked)
VALUES ('Student Council - University of Munich', 80333, 'Munich', 'University of Munich', 'Geschwister-Scholl-Platz 1', 0);

-- Inserting a council record for a German university
INSERT INTO Council (name, zip, city, university, street, isBlocked)
VALUES ('Student Council - Technical University of Munich', 80333, 'Munich', 'Technical University of Munich', 'Arcisstraße 21', 0);

-- Inserting a council record for a German university
INSERT INTO Council (name, zip, city, university, street, isBlocked)
VALUES ('Student Council - Ludwig Maximilian University of Munich', 80539, 'Munich', 'Ludwig Maximilian University of Munich', 'Geschwister-Scholl-Platz 1', 0);

-- Inserting a council record for a German university
INSERT INTO Council (name, zip, city, university, street, isBlocked)
VALUES ('Student Council - Humboldt University of Berlin', 10115, 'Berlin', 'Humboldt University of Berlin', 'Unter den Linden 6', 0);

-- Inserting a council record for a German university
INSERT INTO Council (name, zip, city, university, street, isBlocked)
VALUES ('Student Council - Technical University of Berlin', 10623, 'Berlin', 'Technical University of Berlin', 'Straße des 17. Juni 135', 0);

-- Inserting a council record for a German university
INSERT INTO Council (name, zip, city, university, street, isBlocked)
VALUES ('Student Council - University of Hamburg', 20146, 'Hamburg', 'University of Hamburg', 'Edmund-Siemers-Allee 1', 0);

-- Inserting a council record for a German university
INSERT INTO Council (name, zip, city, university, street, isBlocked)
VALUES ('Student Council - University of Cologne', 50923, 'Cologne', 'University of Cologne', 'Albertus-Magnus-Platz', 0);

-- Inserting a council record for a German university
INSERT INTO Council (name, zip, city, university, street, isBlocked)
VALUES ('Student Council - Goethe University Frankfurt', 60323, 'Frankfurt', 'Goethe University Frankfurt', 'Theodor-W.-Adorno-Platz 1', 0);

-- Inserting a council record for a German university
INSERT INTO Council (name, zip, city, university, street, isBlocked)
VALUES ('Student Council - University of Stuttgart', 70174, 'Stuttgart', 'University of Stuttgart', 'Keplerstraße 7', 0);

-- Inserting a council record for a German university
INSERT INTO Council (name, zip, city, university, street, isBlocked)
VALUES ('Student Council - University of Heidelberg', 69117, 'Heidelberg', 'University of Heidelberg', 'Grabengasse 1', 0);

-- Inserting a report for a user
INSERT INTO Report (userId, reportType, reportStatus, reportTime, reportApplicationInfo)
VALUES (1, 1, 1, '2023-10-05 08:45:00', 'Report for application XYZ');

-- Inserting a report for a user
INSERT INTO Report (userId, reportType, reportStatus, reportTime, reportApplicationInfo)
VALUES (2, 2, 2, '2023-10-10 14:30:00', 'Report for application ABC');

-- Inserting a report for a user
INSERT INTO Report (userId, reportType, reportStatus, reportTime, reportApplicationInfo)
VALUES (3, 1, 1, '2023-10-15 16:45:00', 'Report for application DEF');

-- Inserting a report for a user
INSERT INTO Report (userId, reportType, reportStatus, reportTime, reportApplicationInfo)
VALUES (4, 3, 1, '2023-10-20 10:15:00', 'Report for application GHI');

-- Inserting a report for a user
INSERT INTO Report (userId, reportType, reportStatus, reportTime, reportApplicationInfo)
VALUES (5, 2, 2, '2023-11-05 09:00:00', 'Report for application JKL');

-- Inserting a report for a user
INSERT INTO Report (userId, reportType, reportStatus, reportTime, reportApplicationInfo)
VALUES (6, 1, 1, '2023-11-10 12:15:00', 'Report for application MNO');

-- Inserting a report for a user
INSERT INTO Report (userId, reportType, reportStatus, reportTime, reportApplicationInfo)
VALUES (7, 2, 1, '2023-11-15 15:30:00', 'Report for application PQR');

-- Inserting a report for a user
INSERT INTO Report (userId, reportType, reportStatus, reportTime, reportApplicationInfo)
VALUES (8, 1, 2, '2023-11-20 11:45:00', 'Report for application STU');

-- Inserting a report for a user
INSERT INTO Report (userId, reportType, reportStatus, reportTime, reportApplicationInfo)
VALUES (9, 3, 1, '2023-12-05 09:30:00', 'Report for application VWX');

-- Inserting a report for a user
INSERT INTO Report (userId, reportType, reportStatus, reportTime, reportApplicationInfo)
VALUES (10, 2, 1, '2023-12-10 13:00:00', 'Report for application YZA');

-- Inserting a user role
INSERT INTO Role (name) VALUES ('User');

-- Inserting an admin role
INSERT INTO Role (name) VALUES ('Admin');

-- Inserting a council role
INSERT INTO Role (name) VALUES ('Council');

-- Inserting a host role
INSERT INTO Role (name) VALUES ('Host');