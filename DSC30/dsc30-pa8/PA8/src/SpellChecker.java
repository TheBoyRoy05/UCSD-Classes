/*
 * Name: Issac Roy
 * PID: A17787465
 */

import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Scanner;

/**
 * Spell Checker Implementation
 *
 * @author Issac Roy
 * @since 05/27/2024
 */

public class SpellChecker {

    public KeyedSet dictWords;
    private static final int DEFAULT_CAPACITY = 100;
    private static final int ASCII_START = 97;
    private static final int ALPHABET_LENGTH = 26;

    /**
     * Reads the given dictionary into the implementation of choice (hash table / bloom filter)
     * @param reader reader for the dictionary
     * @param useHashTable use hash table if true, bloom filter otherwise
     */
    public void readDictionary(Reader reader, boolean useHashTable) {
        if (useHashTable) dictWords = new MyHashTable(DEFAULT_CAPACITY);
        else dictWords = new MyBloomFilter();
        Scanner scanner = new Scanner(reader);
        while (scanner.hasNext()){
            dictWords.insert(scanner.nextLine());
        }
        scanner.close();
    }

    /**
     * Checks the given word by switching each letter against the words in dictionary
     * @param word to be checked
     * @return linked list with all words that are one letter switch away
     */
    private LinkedList<String> checkWrongLetter(String word) {
        LinkedList<String> out = new LinkedList<>();
        for (int i = 0; i < word.length(); i++) {
            String copy = word.toLowerCase();
            for (int j = ASCII_START; j < ASCII_START + ALPHABET_LENGTH; j++) {
                String candidate = copy.substring(0, i) + (char) j;
                if (i + 1 != word.length()) candidate += copy.substring(i + 1);
                if (dictWords.lookup(candidate)) out.add(candidate);
            }
        }
        return out;
    }

    /**
     * Checks given word with all possible one letter insertions against the words in dictionary
     * @param word to be checked
     * @return linked list with all words that are one insertion away
     */
    private LinkedList<String> checkInsertedLetter(String word) {
        LinkedList<String> out = new LinkedList<>();
        for (int i = 0; i < word.length() + 1; i++) {
            String copy = word.toLowerCase();
            for (int j = ASCII_START; j < ASCII_START + ALPHABET_LENGTH; j++) {
                String candidate = copy.substring(0, i) + (char) j;
                if (i != word.length()) candidate += copy.substring(i);
                if (dictWords.lookup(candidate)) out.add(candidate);
            }
        }
        return out;
    }

    /**
     * Checks the given word with each letter deleted against all words in the dictionary
     * @param word to be checked
     * @return linked list with all suggested words that are one deletion away
     */
    private LinkedList<String> checkDeleted(String word) {
        LinkedList<String> out = new LinkedList<>();
        for (int i = 0; i < word.length(); i++) {
            String copy = word.toLowerCase();
            String candidate = copy.substring(0, i);
            if (i + 1 != word.length()) candidate += copy.substring(i + 1);
            if (dictWords.lookup(candidate)) out.add(candidate);
        }
        return out;
    }

    /**
     * Checks word with adjacent letters switched against words in the dictionary
     * @param word to be checked
     * @return linked list with all suggested words that is one transposition away
     */
    private LinkedList<String> checkTransposedLetter(String word) {
        LinkedList<String> out = new LinkedList<>();
        for (int i = 0; i < word.length() - 1; i++) {
            String copy = word.toLowerCase();
            String candidate = copy.substring(0, i) + copy.substring(i + 1, i + 2) +
                    copy.substring(i, i + 1);
            if (i + 2 != word.length()) candidate += copy.substring(i + 2);
            if (dictWords.lookup(candidate)) out.add(candidate);
        }
        return out;
    }

    /**
     * Checks the given word with spaces in all possible locations against words in the dictionary
     * @param word to be checked
     * @return linked list of suggested word pairs
     */
    private LinkedList<String> checkInsertSpace(String word) {
        LinkedList<String> out = new LinkedList<>();
        for (int i = 1; i < word.length(); i++) {
            String copy = word.toLowerCase();
            String candidate1 = copy.substring(0, i);
            String candidate2 = copy.substring(i);
            if (dictWords.lookup(candidate1) && dictWords.lookup(candidate2)) {
                out.add(candidate1 + " " + candidate2);
            }
        }
        return out;
    }

    /**
     * Checks a given word against the words in the dictionary using modifications
     * @param word to be checked
     * @return string array of all the suggested correction words
     */
    private String[] checkWord(String word) {
        ArrayList<String> list = new ArrayList<>();

        LinkedList<String> wrongLetter = checkWrongLetter(word);
        while (!wrongLetter.isEmpty()){
            String candidate = wrongLetter.remove();
            if (!list.contains(candidate)) list.add(candidate);
        }

        LinkedList<String> insertLetter = checkInsertedLetter(word);
        while (!insertLetter.isEmpty()){
            String candidate = insertLetter.remove();
            if (!list.contains(candidate)) list.add(candidate);
        }

        LinkedList<String> deleteLetter = checkDeleted(word);
        while (!deleteLetter.isEmpty()){
            String candidate = deleteLetter.remove();
            if (!list.contains(candidate)) list.add(candidate);
        }

        LinkedList<String> transposeLetter = checkTransposedLetter(word);
        while (!transposeLetter.isEmpty()){
            String candidate = transposeLetter.remove();
            if (!list.contains(candidate)) list.add(candidate);
        }

        LinkedList<String> insertSpace = checkInsertSpace(word);
        while (!insertSpace.isEmpty()){
            String candidate = insertSpace.remove();
            if (!list.contains(candidate)) list.add(candidate);
        }

        String[] out = new String[list.size()];
        return list.toArray(out);
    }

    /**
     * Main method to run spell checker
     * @param args 0 - hash table/bloom filter, 1 - dictionary file, 2 - input file
     */
    public static void main(String[] args) {
        // args[0]: 0 if we should use a MyHashTable and 1 for a MyBloomFilter
        // args[1]: path to dict file
        // args[2]: path to input file

        SpellChecker checker = new SpellChecker();

        File dictionary = new File(args[1]);
        try {
            Reader reader = new FileReader(dictionary);
            checker.readDictionary(reader, args[0] == "0");
        } catch (FileNotFoundException e) {
            System.err.println("Failed to open " + dictionary);
            System.exit(1);
        }

        File inputFile = new File(args[2]);
        try {
            Scanner input = new Scanner(inputFile); // Reads list of words
            while (input.hasNext()){
                String word = input.nextLine();
                if (checker.dictWords.lookup(word)) System.out.println(word + ": ok");
                else {
                    String candidates = Arrays.toString(checker.checkWord(word));
                    if (candidates == "[]") System.out.println(word + ": not found");
                    else {
                        System.out.println(word + ": " +
                                candidates.substring(1, candidates.length() - 1));
                    }
                }
            }
            input.close();
        } catch (FileNotFoundException e) {
            System.err.println("Failed to open " + inputFile);
            System.exit(1);
        }
    }
}
