import java.util.ArrayList;

public class SortsTracing {

    //Note: Style is not required for this file

    //for reference
    public ArrayList<int[]> SelectionSortExampleList() {
        ArrayList<int[]> answer = new ArrayList<int[]>();
        answer.add(new int[]{-1, 20, 18, 17, 9, 4, 2, 0, 40});
        answer.add(new int[]{-1, 0, 18, 17, 9, 4, 2, 20, 40});
        answer.add(new int[]{-1, 0, 2, 17, 9, 4, 18, 20, 40});
        answer.add(new int[]{-1, 0, 2, 4, 9, 17, 18, 20, 40});
        answer.add(new int[]{-1, 0, 2, 4, 9, 17, 18, 20, 40});
        answer.add(new int[]{-1, 0, 2, 4, 9, 17, 18, 20, 40});
        // etc... (the rest of the iterations)
        return answer;
    }

    //for reference
    public ArrayList<int[]> CountSortExampleList() {
        ArrayList<int[]> answer = new ArrayList<int[]>();
        //After Counting Step
        answer.add(new int[]{0, 1, 1, 0, 1});
        //After "Running Total" Step
        answer.add(new int[]{0, 1, 2, 2, 3});
        //Rest of iterations to assemble output array
        answer.add(new int[]{0, 0, 2, 2, 3});
        answer.add(new int[]{0, 0, 2, 2, 2});
        answer.add(new int[]{0, 0, 1, 2, 2});
        return answer;
    }

    public ArrayList<int[]> InsertionSortRandomList() {
        ArrayList<int[]> answer = new ArrayList<int[]>();
        answer.add(new int[]{0, 7, 9, 4, 1, 3, 6});
        answer.add(new int[]{0, 7, 9, 4, 1, 3, 6});
        answer.add(new int[]{0, 4, 7, 9, 1, 3, 6});
        answer.add(new int[]{0, 1, 4, 7, 9, 3, 6});
        answer.add(new int[]{0, 1, 3, 4, 7, 9, 6});
        answer.add(new int[]{0, 1, 3, 4, 6, 7, 9});
        return answer;
    }

    public ArrayList<int[]> InsertionSortSortedList() {
        ArrayList<int[]> answer = new ArrayList<int[]>();
        answer.add(new int[]{0, 1, 3, 4, 6, 7, 9});
        answer.add(new int[]{0, 1, 3, 4, 6, 7, 9});
        answer.add(new int[]{0, 1, 3, 4, 6, 7, 9});
        answer.add(new int[]{0, 1, 3, 4, 6, 7, 9});
        answer.add(new int[]{0, 1, 3, 4, 6, 7, 9});
        answer.add(new int[]{0, 1, 3, 4, 6, 7, 9});
        return answer;
    }

    public ArrayList<int[]> InsertionSortReversedList() {
        ArrayList<int[]> answer = new ArrayList<int[]>();
        answer.add(new int[]{7, 9, 6, 4, 3, 1, 0});
        answer.add(new int[]{6, 7, 9, 4, 3, 1, 0});
        answer.add(new int[]{4, 6, 7, 9, 3, 1, 0});
        answer.add(new int[]{3, 4, 6, 7, 9, 1, 0});
        answer.add(new int[]{1, 3, 4, 6, 7, 9, 0});
        answer.add(new int[]{0, 1, 3, 4, 6, 7, 9});
        return answer;
    }
    
    public ArrayList<int[]> CountSortRandomList() {
        ArrayList<int[]> answer = new ArrayList<int[]>();
        //After Counting Step
        answer.add(new int[]{1, 1, 0, 1, 1, 0, 1, 1, 0, 1});
        //After "Running Total" Step
        answer.add(new int[]{1, 2, 2, 3, 4, 4, 5, 6, 6, 7});
        //Rest of iterations to assemble output array
        answer.add(new int[]{1, 2, 2, 3, 4, 4, 5, 5, 6, 7});
        answer.add(new int[]{0, 2, 2, 3, 4, 4, 5, 5, 6, 7});
        answer.add(new int[]{0, 2, 2, 3, 4, 4, 5, 5, 6, 6});
        answer.add(new int[]{0, 2, 2, 3, 3, 4, 5, 5, 6, 6});
        answer.add(new int[]{0, 1, 2, 3, 3, 4, 5, 5, 6, 6});
        answer.add(new int[]{0, 1, 2, 2, 3, 4, 5, 5, 6, 6});
        answer.add(new int[]{0, 1, 2, 2, 3, 4, 4, 5, 6, 6});
        return answer;
    }

    public ArrayList<int[]> CountSortSortedList() {
        // array is [1, 1, 2, 4, 4, 5, 7, 8]
        ArrayList<int[]> answer = new ArrayList<int[]>();
        //After Counting Step
        answer.add(new int[]{1, 1, 0, 1, 1, 0, 1, 1, 0, 1});
        //After "Running Total" Step
        answer.add(new int[]{1, 2, 2, 3, 4, 4, 5, 6, 6, 7});
        //Rest of iterations to assemble output array
        answer.add(new int[]{0, 2, 2, 3, 4, 4, 5, 6, 6, 7});
        answer.add(new int[]{0, 1, 2, 3, 4, 4, 5, 6, 6, 7});
        answer.add(new int[]{0, 1, 2, 2, 4, 4, 5, 6, 6, 7});
        answer.add(new int[]{0, 1, 2, 2, 3, 4, 5, 6, 6, 7});
        answer.add(new int[]{0, 1, 2, 2, 3, 4, 4, 6, 6, 7});
        answer.add(new int[]{0, 1, 2, 2, 3, 4, 4, 5, 6, 7});
        answer.add(new int[]{0, 1, 2, 2, 3, 4, 4, 5, 6, 6});
        return answer;
    }

    public ArrayList<int[]> CountSortReversedList() {
        // array is [8, 7, 5, 4, 4, 2, 1, 1]
        ArrayList<int[]> answer = new ArrayList<int[]>();
        //After Counting Step
        answer.add(new int[]{1, 1, 0, 1, 1, 0, 1, 1, 0, 1});
        //After "Running Total" Step
        answer.add(new int[]{1, 2, 2, 3, 4, 4, 5, 6, 6, 7});
        //Rest of iterations to assemble output array
        answer.add(new int[]{1, 2, 2, 3, 4, 4, 5, 6, 6, 6});
        answer.add(new int[]{1, 2, 2, 3, 4, 4, 5, 5, 6, 6});
        answer.add(new int[]{1, 2, 2, 3, 4, 4, 4, 5, 6, 6});
        answer.add(new int[]{1, 2, 2, 3, 3, 4, 4, 5, 6, 6});
        answer.add(new int[]{1, 2, 2, 2, 3, 4, 4, 5, 6, 6});
        answer.add(new int[]{1, 1, 2, 2, 3, 4, 4, 5, 6, 6});
        answer.add(new int[]{0, 1, 2, 2, 3, 4, 4, 5, 6, 6});
        return answer;
    }

    public ArrayList<int[]> QuickSortRandomList() {
        ArrayList<int[]> answer = new ArrayList<int[]>();
        answer.add(new int[]{2, 1, 3, 6, 9});
        answer.add(new int[]{1, 2, 3, 6, 9});
        return answer;
    }

    public ArrayList<int[]> QuickSortSortedList() {
        ArrayList<int[]> answer = new ArrayList<int[]>();
        answer.add(new int[]{1, 2, 3, 6, 9});
        answer.add(new int[]{1, 2, 3, 6, 9});
        answer.add(new int[]{1, 2, 3, 6, 9});
        answer.add(new int[]{1, 2, 3, 6, 9});
        return answer;
    }

    public ArrayList<int[]> QuickSortReversedList() {
        ArrayList<int[]> answer = new ArrayList<int[]>();
        answer.add(new int[]{1, 6, 3, 2, 9});
        answer.add(new int[]{1, 6, 3, 2, 9});
        answer.add(new int[]{1, 2, 3, 6, 9});
        answer.add(new int[]{1, 2, 3, 6, 9});
        return answer;
    }

}