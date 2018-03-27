### work out like Q.374
to find the guarantee, we have to assume the worst case for Q.374 program
assume the mid is lower (picked number is higher), we accumulate the mid into sum
s = 0
s = 0 + (1+n)/2, left = (1+n)/2 + 1, mid = ((3+n)/2 + n)/2 =
recursion until if n - left == 4 ---> add mid
if n - left == 3 ----> add --->mid

Done!

### Recursion:
s += mid until (n - left) == 3 or (n - left) == 4