h_indices = [3,0,6,1,55,5,5];
ret = build(h_indices)
i = 1;
h_idx = del_max(ret);
while (len(ret) > 0) and i < h_idx:
    h_idx = del_max(ret);
    i += 1;

return h_idx if i >= h_idx else 0;

