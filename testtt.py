var precomp = {1: 1};

function collatz(n) {
    var orig = n;
    var len = 0;

    while (!(n in precomp)) {
        n = (n % 2) ? 3*n + 1 : n / 2;
        len++;
    }

    return (precomp[orig] = len + precomp[n]);
}

function maxCollatz(n) {
    var res = [1, 1];

    for (var k = 2; k <= n; k++) {
        var c = collatz(k);

        if (c > res[1]) {
            res[0] = k;
            res[1] = c;
        }
    }

    return res;
}


lookup = {}

def countTerms(n):
   arg = n
   count = 1
   while n is not 1:
      count += 1
      if not n%2:
         n /= 2
      else:
         n = (n*3 + 1)
      if n not in lookup:
         lookup[n] = count

   return lookup[n], arg

print max(countTerms(i) for i in range(500001, 1000000, 2)) 
