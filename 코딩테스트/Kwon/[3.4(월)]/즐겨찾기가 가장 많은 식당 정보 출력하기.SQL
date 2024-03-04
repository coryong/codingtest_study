# max(FAVORITES) 하다가 결과 화면이랑 REST_NAME 다르길래 테스트 후 변경
# max(FAVORITES) 하면 첫번째 index의 REST_NAME이 출력 되기 때문에 코드 수정
select FOOD_TYPE, REST_ID, REST_NAME, FAVORITES
from REST_INFO
where (FOOD_TYPE, FAVORITES)
    IN (select FOOD_TYPE, max(FAVORITES) as FAVORITES
        from REST_INFO
        group by FOOD_TYPE)

order by FOOD_TYPE desc;
