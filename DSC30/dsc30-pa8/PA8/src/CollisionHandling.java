/**
 * PA8 Part 1 worksheet (style not required)
 */
public class CollisionHandling {

    /**
     * method that stores the result of Q1 in PA8 worksheet
     * 4 insertions and then all of them
     * @return hashtable representation after insertions
     */
    public static int[][] linearProbingResult(){
        int[][] output = new int[][]{{0, 56, 0, 42, 0, 28, 0, 14}, {70, 56, 112, 42, 98, 28, 84, 14}};
        return output;
    }

    /**
     * method that stores the result of Q2 in PA8 worksheet
     * 4 insertions and then all of them
     * @return hashtable representation after insertions
     */
    public static int[][] quadraticProbingResult(){
        int[][] output = new int[][]{{0, 6, 0, 16, 1, 0, 11, 0}, {21, 6, 27, 16, 1, 9, 11, 3}};
        return output;
    }

    /**
     * method that stores the result of Q3 in PA8 worksheet
     * 4 insertions and then all of them
     * @return hashtable representation after insertions
     */
    public static int[][] doubleHashingResult(){
        int [][] output = {{}, {}};
        output[0] = new int[]{0, 0, 10, 17, 0, 23, 2, 0};
        output[1] = new int[]{0, 51, 38, 17, 44, 23, 2, 0, 0, 31, 10, 0, 0, 0, 0, 0};
        return output;
    }
}
