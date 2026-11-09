public class ComplexityDemo {
    static int constant(int[] a) { int x = a[0]; return 1; }          // O(1)

    static int logarithmic(int n) {                                    // O(log n)
        int steps = 0;
        while (n > 1) { n /= 2; steps++; }
        return steps;
    }

    static int linear(int n) {                                         // O(n)
        int steps = 0;
        for (int i = 0; i < n; i++) steps++;
        return steps;
    }

    static int linearithmic(int n) {                                   // O(n log n)
        int steps = 0;
        for (int i = 0; i < n; i++)
            for (int m = n; m > 1; m /= 2) steps++;
        return steps;
    }

    static int quadratic(int n) {                                      // O(n^2)
        int steps = 0;
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++) steps++;
        return steps;
    }

    static int exponential(int n) {                                    // O(2^n)
        if (n == 0) return 1;
        return exponential(n - 1) + exponential(n - 1);
    }

    static int factorialTime(int n) {                                  // O(n!)
        if (n == 0) return 1;
        int total = 0;
        for (int i = 0; i < n; i++) total += factorialTime(n - 1);
        return total;
    }

    // ---- space ----
    static int copySpace(int n) { return new int[n].length; }          // O(n)
    static int gridSpace(int n) { return new int[n][n].length * n; }   // O(n^2)
    static int depth(int n) { return n == 0 ? 1 : 1 + depth(n - 1); }  // O(n) stack

    public static void main(String[] args) {
        System.out.println("O(1)       " + constant(new int[]{5, 6, 7}));
        System.out.println("O(log n)   " + logarithmic(16));
        System.out.println("O(n)       " + linear(16));
        System.out.println("O(n log n) " + linearithmic(16));
        System.out.println("O(n^2)     " + quadratic(16));
        System.out.println("O(2^n)     " + exponential(10));
        System.out.println("O(n!)      " + factorialTime(5));
        System.out.println("space O(n) copy       " + copySpace(16));
        System.out.println("space O(n^2) grid     " + gridSpace(16));
        System.out.println("space O(n) recursion  " + depth(15));
    }
}
