SELECT MEMBER_ID, MEMBER_NAME, GENDER, DATE_FORMAT(DATE_OF_BIRTH, "%Y-%m-%d") AS DATE_OF_BIRTH FROM MEMBER_PROFILE WHERE GENDER = 'W' AND MONTH(DATE_OF_BIRTH) = '03' AND TLNO IS NOT NULL;


-- DATE_FORMAT -> 날짜형식 맞추기
-- MONTH(DATE_OF_BIRTH) -> 특정 월로 조건 지정