-- 01. Querying data 조회
SELECT LastName FROM employees;
SELECT LastName, FirstName AS '이름' FROM employees;
SELECT * FROM employees;
SELECT Name, Milliseconds / 60000 AS '재생시간(분)' from tracks;

-- 02. Sorting data
SELECT FirstName FROM employees ORDER BY FirstName;
SELECT FirstName FROM employees ORDER BY FirstName DESC;
SELECT Country, City FROM customers ORDER BY Country DESC;
SELECT Country, City FROM customers ORDER BY Country DESC City ASC;

SELECT Name, Milliseconds / 60000 AS ' 재생 시간(분)' FROM tracks ORDER BY Milliseconds DESC
-- NULL 정렬 예시
SELECT ReportsTo FROM employees ORDER BY ReportsTo DESC;
-- 03. Filtering data
SELECT DISTINCT Country FROM customers ORDER BY Country;
SELECT Country FROm customers WHERE Country LIKE 'A%';
SELECT LastName, FirstName, Company, Country From customers where Company is null AND Country = 'USA';
SELECT LastName, FirstName, Country FROM customers WHERE Country = 'Canada' OR Country = 'Germany' OR Country = 'France';
SELECT LastName, FirstName, Country FROM customers WHERE Country in ('Canada','Germany','France');
SELECT LastName, FirstName From customers where LastName like '%son';
SELECT LastName, FirstName FROM customers where FirstName LIKE '___a';
SELECT TrackId, Name, Bytes FROM tracks ORDER BY Bytes DESC LIMIT 7;
SELECT TrackId, Name, Bytes FROM tracks ORDER BY Bytes DESC LIMIT 3,4; 

-- 04. Grouping data
SELECT Country, COUNT(*) FROM customers Group BY Country;
SELECT Composer, AVG(Bytes) AS avgOFBytes FROM tracks GROUP BY Composer ORDER BY avgOFBytes DESC;
SELECT Composer, AVG(Milliseconds / 60000) as averageOFMinute From tracks Group BY Composer HAVING avgOFBytes;