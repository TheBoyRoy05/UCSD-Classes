/*
 * Name: Issac Roy
 * PID:  A17787465
 */

import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

/**
 * Search Engine implementation.
 * 
 * @author Issac Roy
 * @since  05/10/24
 */
public class SearchEngine {

    /**
     * Populate BSTrees from a file
     * 
     * @param movieTree  - BST to be populated with actors
     * @param studioTree - BST to be populated with studios
     * @param ratingTree - BST to be populated with ratings
     * @param fileName   - name of the input file
     * @return false if file not found, true otherwise
     */
    public static boolean populateSearchTrees(
            BSTree<String> movieTree, BSTree<String> studioTree,
            BSTree<String> ratingTree, String fileName
    ) {
        // open and read file
        File file = new File(fileName);
        try {
            Scanner scanner = new Scanner(file);
            while (scanner.hasNextLine()) {
                // read 5 lines per batch:
                // movie, cast, studios, rating, trailing hyphen
                String movie = scanner.nextLine().trim();
                String cast[] = scanner.nextLine().split(" ");
                String studios[] = scanner.nextLine().split(" ");
                String rating = scanner.nextLine().trim();
                scanner.nextLine();

                // populate three trees with the information you just read
                // hint: create a helper function and reuse it to build all three trees
                populateTree(movieTree, cast, movie);
                populateTree(studioTree, studios, movie);
                populateTree(ratingTree, cast, rating);
            }
            scanner.close();
        } catch (FileNotFoundException e) {
            return false;
        }
        return true;
    }

    /**
     * Helper method to populate a Binary Search Tree
     *
     * @param tree tree to populate
     * @param keys keys for the nodes of the tree
     * @param data data to be stored in the keys
     */
    private static void populateTree(BSTree<String> tree, String[] keys, String data){
        for (String key : keys) {
            key = key.toLowerCase();
            if (!tree.findKey(key)) tree.insert(key);
            if (!tree.findDataList(key).contains(data)) tree.insertData(key, data);
        }
    }

    /**
     * Search a query in a BST
     * 
     * @param searchTree - BST to be searched
     * @param query      - query string
     */
    public static void searchMyQuery(BSTree<String> searchTree, String query) {
        // process query
        String[] keys = query.toLowerCase().split(" ");

        // search and output intersection results
        // hint: list's addAll() and retainAll() methods could be helpful
        LinkedList<String> all = new LinkedList<>();
        if (searchTree.findKey(keys[0])) all.addAll(searchTree.findDataList(keys[0]));
        for (int i = 1; i < keys.length; i++) {
            if (searchTree.findKey(keys[i])) all.retainAll(searchTree.findDataList(keys[i]));
        }
        if (keys.length > 1) print(query, all);

        // search and output individual results
        // hint: list's addAll() and removeAll() methods could be helpful
        for(String key : keys){
            if (searchTree.findKey(key)) {
                LinkedList<String> list = new LinkedList<>(searchTree.findDataList(key));
                if (list.isEmpty()) print(key, list);
                else {
                    list.removeAll(all);
                    print(key, list);
                }
            } else print(key, null);
        }
    }

    /**
     * Print output of query
     * 
     * @param query     Query used to search tree
     * @param documents Output of documents from query
     */
    public static void print(String query, LinkedList<String> documents) {
        if (documents == null || documents.isEmpty())
            System.out.println("The search yielded no results for " + query);
        else {
            Object[] converted = documents.toArray();
            Arrays.sort(converted);
            System.out.println("Documents related to " + query
                    + " are: " + Arrays.toString(converted));
        }
    }

    /**
     * Main method that processes and query the given arguments
     * 
     * @param args command line arguments
     */
    public static void main(String[] args) {
        // initialize search trees
        BSTree<String> movieTree = new BSTree<>();
        BSTree<String> studioTree = new BSTree<>();
        BSTree<String> ratingTree = new BSTree<>();

        // process command line arguments
        String fileName = args[0];
        int searchKind = Integer.parseInt(args[1]);
        String query = String.join(" ", Arrays.copyOfRange(args, 2, args.length));

        // populate search trees
        populateSearchTrees(movieTree, studioTree, ratingTree, fileName);

        // choose the right tree to query
        if (searchKind == 0) searchMyQuery(movieTree, query);
        else if (searchKind == 1) searchMyQuery(studioTree, query);
        else if (searchKind == 2) searchMyQuery(ratingTree, query);
    }
}
