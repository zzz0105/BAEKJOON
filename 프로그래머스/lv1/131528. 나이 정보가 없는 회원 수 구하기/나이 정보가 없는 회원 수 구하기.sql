# COUNT(*): NULL 포함     COUNT(AGE): NULL 포함X
# SUM(AGE IS NULL): 조건을 충족하는 경우(참, 나이 정보가 없는 회원)에는 1로, 나머지는 0으로 바뀌어 더해짐
SELECT COUNT(*) AS USERS FROM USER_INFO WHERE AGE IS NULL