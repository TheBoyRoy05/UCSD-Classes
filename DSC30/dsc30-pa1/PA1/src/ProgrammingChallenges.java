/*
 * Name: Issac Roy
 * PID:  A17787465
 */

/**
 * Various Programming Challenges
 *
 * @author Issac Roy
 * @since 4/3/2024
 */

public class ProgrammingChallenges {

    public static final double PERCENT = 100.0;
    public static final double DIVISOR = 1000.0;
    public static final int NUM_DECREASING_ORDER = 3;

    /**
     * Problem 1
     * Returns true if item is cake, ice-cream, or sushi and you have enough money
     * @param item      The item you want to get
     * @param inWallet  The money you have
     * @param needed    The price of the item
     * @return          Boolean whether you can buy the item and if its one of the desired foods
     */
    public static boolean store(String item, float inWallet, float needed) {
        return (item.equals("cake") || item.equals("ice-cream") || item.equals("sushi"))
                && inWallet >= needed;
    }

    /**
     * Problem 2
     * Returns true if the first array is twice as long as the second and if the first and last
     * elements of the two arrays are opposites, i.e. first element of first array is opposite to
     * last element of second and vice versa
     * @param arr1  First array
     * @param arr2  Second array
     * @return      True if the above conditions are satisfied
     */
    public static boolean compareArrays(int[] arr1, int[] arr2) {
        return arr1.length == arr2.length+arr2.length && arr1[0] == -1*arr2[arr2.length-1]
                && arr2[0] == -1*arr1[arr1.length-1];
    }

    /**
     * Problem 3
     * Returns the number of odd numbers that aren't divisible by 7 in an array
     * @param arr1  Integer array
     * @return      The number of odds that aren't multiples of 7
     */
    public static int countNumbers(int[] arr1) {
        int count = 0;
        for(int i = 0; i < arr1.length; i++){
            if (arr1[i]%2 == 1 && arr1[i]%7 != 0){
                count++;
            }
        }
        return count;
    }

    /**
     * Problem 4
     * Returns the number of positive integers and the average of those positive integers
     * @param arr1  Integer array
     * @return      Array containing the number of positive ints and the average of those ints
     */
    public static float[] positiveAverage(int[] arr1) {
        int i = 0;
        float sum = 0, count = 0;
        while (i < arr1.length) {
            if(arr1[i] > 0){
                sum += (float) arr1[i];
                count++;
            }
            i++;
        }
        float[] out = {count, (float) (Math.round(sum/count*PERCENT)/PERCENT)};
        return out;
    }

    /**
     * Problem 5
     * Returns true if the first digit of the first number is the same as the last digit of
     * the second number
     * @param num1  First number
     * @param num2  Second number
     * @return      True if the condition is met
     */
    public static boolean sameDigitFirstAndLast(int num1, int num2) {
        return Integer.toString(num1).charAt(0) == Integer.toString(num2%10).charAt(0);
    }

    /**
     * Problem 6
     * Returns true if there are at least three consecutive decreasing numbers in this array
     * @param elems     Integer array
     * @return          True if the condition is met
     */
    public static boolean decreasingOrder(int[] elems) {
        int count = 1;
        for(int i = 1; i < elems.length; i++){
            if (elems[i] < elems[i-1]){
                count++;
            }else{
                count = 1;
            }
            if (count >= NUM_DECREASING_ORDER) {
                return true;
            }
        }
        return false;
    }

    /**
     * Problem 7
     * Takes a 2-D int array and replaces the diagonal with the sum of the diagonal
     * @param elems     2-D integer array
     */
    public static void replaceMainDiagonal(int[][] elems) {
        int sum = 0;
        for (int i = 0; i < elems.length; i++){
            sum += elems[i][i];
        }
        for (int i = 0; i < elems.length; i++){
            elems[i][i] = sum;
        }
    }

    /**
     * Problem 8
     * Returns the average grades of each assignment
     * @param grades    2-D int array where each row is a student and each column is an assignment
     * @return          Average grade for each assignment
     */
    public static float[] assignmentAverages (int[][] grades) {
        float[] out = new float[grades[0].length];
        for (int i = 0; i < grades[0].length; i++) {
            for (int j = 0; j < grades.length; j++) {
                out[i] += grades[j][i];
            }
            out[i] /= grades.length;
            out[i] = (float) (Math.round(out[i] * DIVISOR) / DIVISOR);
        }
        return out;
    }

    /**
     * Problem 9
     * Takes in a string and returns a new string where all the dots ('.') have been removed
     * @param str   input String
     * @return      str with all dots removed
     */
    public static String noDots(String str) {
        if (str.length() == 0) {
            return "";
        }
        if (str.charAt(0) == '.'){
            return noDots(str.substring(1));
        }else{
            return str.substring(0, 1) + noDots(str.substring(1));
        }
    }

    /**
     * Problem 10
     * Takes an int array and returns:
     * - [] if the length of the array is less than 2
     * - the middle two elements if the length of the array is even
     * - the length of the array and the min of the first and last elements if the length is odd
     * @param elems     Integer array
     * @return          Array based on the conditions above
     */
    public static int[] twoElements(int[] elems) {
        if (elems.length <= 1){
            return new int[0];
        }
        if (elems.length%2 == 0) {
            return new int[] {elems[elems.length/2]-1, elems[elems.length/2]};
        }else{
            return new int[] {elems.length, Math.min(elems[0], elems[elems.length-1])};
        }
    }
}
