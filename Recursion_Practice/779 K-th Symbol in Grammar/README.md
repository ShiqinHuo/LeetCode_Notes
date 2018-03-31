Add the basic step for n = 1

Inductive steps:<br />
After notice: we can observe that, if the given k is less than the length of the last row<br />
it will return the kthGrammar(last_row, k); Otherwise, it will return the "ones' complement"<br />
of the (k - len_last_row)th element.


