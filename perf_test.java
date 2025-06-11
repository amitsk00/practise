


// import java.util.ArrayList;
// import java.util.List;

public class perf_test {
    public static void main(String[] args) {
        int numMax = 100003;
        boolean isPrime = false;
        long startTime, endTime, duration;
        // List<Integer> allPrimes = new ArrayList<>();

        isPrime = false;
        startTime = System.nanoTime();
        isPrime = isPrime1(numMax);
        endTime = System.nanoTime();
        duration = endTime - startTime;
        System.out.println("1 - Time taken: " + duration + " nano seconds , and prime flag is " + isPrime);
        

        isPrime = false;
        startTime = System.nanoTime();
        isPrime = isPrime2(numMax);
        endTime = System.nanoTime();
        duration = endTime - startTime;
        System.out.println("2 - Time taken: " + duration + " nano seconds , and prime flag is " + isPrime);
        

        isPrime = false;
        startTime = System.nanoTime();
        isPrime = isPrime3(numMax);
        endTime = System.nanoTime();
        duration = endTime - startTime;
        System.out.println("3 - Time taken: " + duration + " nano seconds , and prime flag is " + isPrime);
        
    }




    public static boolean isPrime3(int num) {
        if (num < 2) {
            return false;
        }
        for (int j = 2; j <= Math.sqrt(num); j++) {
            if (num % j == 0) {
                return false;
            }
        }
        return true;
    }

    
    public static boolean isPrime2(int num) {
        if (num < 2) {
            return false;
        }
        for (int j = 2; j <= num/2 +1 ; j++) {
            if (num % j == 0) {
                return false;
            }
        }
        return true;
    }


    public static boolean isPrime1(int num) {
        if (num < 2) {
            return false;
        }
        for (int j = 2; j <= num; j++) {
            if (num % j == 0) {
                return false;
            }
        }
        return true;
    }    
}