/*
 * Name: Issac Roy
 * PID:  A17787465
 */

/**
 * One-Hot Encoding
 *
 * @author Issac Roy
 * @since 4/3/2024
 */

public class OneHot {
    /**
     * EC1
     * Returns all the unique strings in the given array in order
     * @param arr   String array
     * @return      Array of unique values in order
     */
    public static String[] getUnique(String[] arr) {
        String[] out = new String[arr.length];
        int count = 0;
        for (int i = 0; i < arr.length; i++){
            boolean found = false;
            for (int j = 0; j < out.length; j++){
                if (arr[i] == out[j]){
                    found = true;
                }
            }
            if (!found) {
                out[count] = arr[i];
                count++;
            }
        }
        return out;
    }

    /**
     * EC2
     * Returns the number of unique elements in a given array
     * @param arr   String array
     * @return      Number of unique elements
     */
    public static int getNumOfUniqueElements(String[] arr) {
        String[] unique = getUnique(arr);
        int count = 0;
        for (int i = 0; i < unique.length; i++) {
            if (unique[i] != null) {
                count++;
            }else{
                break;
            }
        }
        return count;
    }

    /**
     * EC3
     * Returns the oneHotEncoded matrix of a given array
     * @param arr   String array
     * @return      Matrix of one hot vectors for each element in given array
     */
    public static int[][] oneHotEncode(String[] arr) {
        int[][] out = new int[getNumOfUniqueElements(arr)][arr.length];
        String[] unique = getUnique(arr);
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < unique.length; j++) {
                if (arr[i] == unique[j]) {
                    out[j][i] = 1;
                }
            }
        }
        return out;
    }
}
