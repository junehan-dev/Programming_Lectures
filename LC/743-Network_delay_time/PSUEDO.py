"""
- N INT:
    Node counts with number start with 1 to N
- times [timespec[]]:
    list of timespecs
        timespec [src:int, dest:int, times:int] : stat for route of one. from src to dest take times time.
- K INT:
    label_number of node, specifies the entry point which sends a signal.

"""

#K_routes <- list of timepect src of K
#sig_Q <- signals wait for sends

#1. GREP K routes
#2. PUT K routes to sig_Q
#3. RUN WHILE sig_q not Empty:

sig = pop()
if sig.dest not in routes:
    SAVE sig.dest as route + cur
    PUSH sig.dest.routes INTO routes
    if not sig:
        ret = cur;
elif: cur_time + sig.delay < routes[sig.dest]:
    RESET sig.dest as route + cur

return ret;
