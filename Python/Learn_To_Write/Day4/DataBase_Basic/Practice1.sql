-- 문제 1번 order_items 테이블에서 구매 수량이 2개 이상인 상품 조회.
select * from order_items
where quantity >= 2;

-- 문제 2번 가격이 20,000원 이상이면서 수량이 2개 이상인 상품을 조회
select * from order_items
where price >= 20000 and quantity >= 2;

-- 문제 3번 이미 존재하는 id = 1을 사용하여 새로운 상품을 추가해서 고의로 오류를 발생하자.
-- 결과는 23505 에러가 발생해야한다.
insert into order_items (id, product_name, price, quantity)
values (1, '본체', 10000000, 1);