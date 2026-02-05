import java.util.*;

/**
 * Node class to answer problem 1 -  huffman tree
 */
class HuffmanNode{
    char c;
    int freq;
    String path;

    public HuffmanNode(char c, int freq, String path){
        this.c = c;
        this.freq = freq;
        this.path = path;
    }
}

/**
 * Node class for B-tree
 */
class BNode{
    List data;
    List<BNode> children;

    public BNode(List data){
        this.data = data;
        this.children = new ArrayList<BNode>();
    }
    public void setChildren(List<BNode> children){
        this.children = children;
    }

    public void addChildren(BNode node){
        this.children.add(node);
    }
}

/**
 * Java file that stores answers to problem 1(huffman encoding) and problem 2(B-tree)
 */
public class Worksheet {


    /**
     * Answer to q1(a)
     * @return arrayList consisting HuffmanNodes, where each node stores info about an encoded character
     */
    public static ArrayList<HuffmanNode> q1aEncodeChar(){
        ArrayList<HuffmanNode> nodeList = new ArrayList<HuffmanNode>();
        nodeList.add(new HuffmanNode('s', 1, "1000"));
        nodeList.add(new HuffmanNode('3', 1, "1011"));
        nodeList.add(new HuffmanNode('0', 2, "10010"));
        nodeList.add(new HuffmanNode('1', 1, "10011"));
        nodeList.add(new HuffmanNode('2', 1, "10100"));
        nodeList.add(new HuffmanNode('4', 1, "10101"));
        nodeList.add(new HuffmanNode('5', 1, "11000"));
        nodeList.add(new HuffmanNode('6', 1, "11001"));
        nodeList.add(new HuffmanNode('c', 1, "11010"));
        nodeList.add(new HuffmanNode('d', 1, "11011"));
        nodeList.add(new HuffmanNode('\n', 5, "111"));
        nodeList.add(new HuffmanNode('A', 6, "00"));
        nodeList.add(new HuffmanNode('P', 6, "01"));
        return nodeList;
    }

    /**
     * Answer to q1(b)
     * @return arrayList consisting HuffmanNodes, where each node stores info about an encoded character
     */
    public static ArrayList<HuffmanNode> q1bEncodeChar(){
        ArrayList<HuffmanNode> nodeList = new ArrayList<HuffmanNode>();
        nodeList.add(new HuffmanNode('T', 1, "0110"));
        nodeList.add(new HuffmanNode('d', 1, "0111"));
        nodeList.add(new HuffmanNode('e', 1, "1000"));
        nodeList.add(new HuffmanNode('i', 1, "1001"));
        nodeList.add(new HuffmanNode('m', 1, "1010"));
        nodeList.add(new HuffmanNode('o', 1, "1011"));
        nodeList.add(new HuffmanNode('s', 1, "1100"));
        nodeList.add(new HuffmanNode('u', 1, "1101"));
        nodeList.add(new HuffmanNode('y', 1, "000"));
        nodeList.add(new HuffmanNode(' ', 2, "001"));
        nodeList.add(new HuffmanNode('!', 2, "010"));
        nodeList.add(new HuffmanNode('t', 2, "111"));
        return nodeList;
    }

    /**
     * Answer to 2(a)
     * @return a list of BNodes
     */
    public static ArrayList<BNode> q2EncodeTree(){
        ArrayList<BNode> nodeList = new ArrayList<BNode>();

        // add leaf nodes
        nodeList.add(new BNode(Arrays.asList(12,23,26)));
        nodeList.add(new BNode(Arrays.asList(41,44,50)));
        nodeList.add(new BNode(Arrays.asList(65)));
        nodeList.add(new BNode(Arrays.asList(69)));
        nodeList.add(new BNode(Arrays.asList(93,95,98)));
        // add internal nodes
        nodeList.add(new BNode(Arrays.asList(34,51)));
        nodeList.add(new BNode(Arrays.asList(88)));
        nodeList.add(new BNode(Arrays.asList(67)));

        // assign children
        nodeList.get(7).addChildren(nodeList.get(5));
        nodeList.get(7).addChildren(nodeList.get(6));
        nodeList.get(5).addChildren(nodeList.get(0));
        nodeList.get(5).addChildren(nodeList.get(1));
        nodeList.get(5).addChildren(nodeList.get(2));
        nodeList.get(6).addChildren(nodeList.get(3));
        nodeList.get(6).addChildren(nodeList.get(4));
        return nodeList;
    }

    public static void main(String[] args) {
        ArrayList<BNode> nodes = q2EncodeTree();
        System.out.println("number of nodes  = "+nodes.size());
        for(int i = nodes.size()-1;i>=0;i--){
            List<BNode> children = nodes.get(i).children;
            String output = "";
            output+="current data = "+nodes.get(i).data+"\n";
            output+="children = ";
            if(children.size()==0){
                output+="None";
            }
            for(int j=0;j<children.size();j++){
                output+=children.get(j).data;
            }
            System.out.println(output);
            System.out.println("____________________");
        }
    }
}
