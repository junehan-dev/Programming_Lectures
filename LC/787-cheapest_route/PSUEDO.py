GET K
GET K ROUTES, SET ROUTES WITHOUT K

FOR k in K_ROUTES
    Q.ENQUEUE((to, k_cnt, price))

LOGS = [START= 0, 0,0,0,0,0]

WHILE Q:
    TO, K_LEFT, PRICE = Q.DEQUEUE(); 
    IF K_LEFT != -1 AND (x LOGS[TO] > PRICE OR !LOGS[TO])? #NOT CONDITION
        LOGS[TO] = PRICE
        IF TO != DEST #STOP FLIGHT
            TO_ROUTES = FILTER(to == TO, ROUTES);
            FOR r IN TO_ROUTES
                Q.ENQUEUE((r.to, k_cnt-1, PRICE+r.price));

RET LOGS[DEST];
