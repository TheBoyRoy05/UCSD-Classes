/**
 * Manual BST methods
 */

import java.util.*;

public class BSTManual {

/**
 * Tracing BST algorithms by hand
 *
 * @author Issac Roy
 * @since  05/10/24
 */

// No style for this file.	

public static ArrayList<String>  insertElements() {

	ArrayList<String> answer_pr1 = new ArrayList<>(11);

	/*
	 * make sure you add your answers in the following format:
	 * 
	 * answer_pr1.add("1"); --> level 1 (root level) of the output BST
	 * answer_pr1.add("2, X"); --> level 2 of the output BST
	 * answer_pr1.add("3, X, X, X"); --> level 3 of the output BST 
	 * 
	 * the above example is the same as the second pictoral example on your
	 * worksheet
	 */

	answer_pr1.add("50");
	answer_pr1.add("15, 61");
	answer_pr1.add("13, 37, X, 65");
	answer_pr1.add("X, X, 25, 38, X, X, X, 92");
	answer_pr1.add("X, X, X, X, 21, X, X, X, X, X, X, X, X, X, X, X");
	return answer_pr1;
}

public static ArrayList<String>  deleteElements() {

	ArrayList<String> answer_pr2 = new ArrayList<>(11);
	
	/*
	 * Please refer to the example in insertElements() if you lose track
	 * of how to properly enter your answers
	 */

	answer_pr2.add("57");
	answer_pr2.add("47, 60");
	answer_pr2.add("20, X, X, 94");
	answer_pr2.add("X, 21, X, X, X, X, X, X");
	return answer_pr2;
}

public static ArrayList<String>  traversals() {

	ArrayList<String> answer_pr3 = new ArrayList<>(11);
	
	/*
	 * In this one, you will add ONLY and EXACTLY 3 strings to answer_pr3
	 * 
	 * here's how you do it:
	 * 
	 * answer_pr3.add("1, 2, 3, 4, 5") --> in-order traversal result
	 * answer_pr3.add("1, 2, 3, 4, 5") --> pre-order traversal result
	 * answer_pr3.add("1, 2, 3, 4, 5") --> post-order traversal result
	 * 
	 * replace "1, 2, 3, 4, 5" with your actual answers
	 */
	answer_pr3.add("4, 19, 22, 28, 39, 56, 64, 68, 93, 95, 96, 97, 98");
	answer_pr3.add("39, 19, 4, 22, 28, 93, 64, 56, 68, 96, 95, 98, 97");
	answer_pr3.add("4, 28, 22, 19, 56, 68, 64, 95, 97, 98, 96, 93, 39");
	return answer_pr3;
}
}
