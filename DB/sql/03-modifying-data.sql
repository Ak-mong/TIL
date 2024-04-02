-- 공통
SELECT * FROM articles;
DROP TABLE articles;
PRAGMA table_info('articles');

CREATE TABLE articles(
id INTEGER PRIMARY KEY AUTOINCREMENT,
title VARCHAR(100) NOT NULL,
content VARCHAR(100) NOT NULL,
createdAt DATE NOT NULL
)


-- 1. Insert data into table
INSERT INTO articles (
title,content, createdAt)
VALUES ('제목1','글 내용','2024-04-02'),
('제목2','글 내용',DATE()),
('제목3','글 내용',DATE());

-- 2. Update data in table
UPDATE articles
SET title='수정된 제목', content='수정된 내용'
WHERE id = 2;

-- 3. Delete data from table
DELETE FROM articles
WHERE id = 2;

DELETE FROM articles 
WHERE id in (
SELECT * FROM articles
ORDER by createdAt
LIMIT 2);

DELETE FROM articles;