-- Create Db
USE GoogleApps;

--drop tABLE app_data

--Create Table
CREATE TABLE app_data (
    id uniqueidentifier not null default NEWID(),
    appname NVARCHAR(255) unique,
    ratingcount INT,
    installs INT,
    price FLOAT,
    size INT,
    version INT,
    last_update INT,
    contentRating NVARCHAR(100),
    category NVARCHAR(100),
    ad_supported BIT
);

--Insert Dummy Values
--INSERT INTO app_data (
--    appname,
--    ratingcount,
--    installs,
--    price,
--    size,
--    version,
--    last_update,
--    contentRating,
--    category,
--    ad_supported
--) VALUES (
--    'Dummy App2',
--    1000,
--    5000,
--    2.99,
--    1024,
--    1,
--    7,
--    'Everyone',
--    'Books',
--    1
--);

SELECT * FROM app_data