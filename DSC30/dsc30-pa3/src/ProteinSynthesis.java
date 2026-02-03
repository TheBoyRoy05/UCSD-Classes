/*
    Name: Issac Roy
    PID:  A17787465
 */

/**
 * Translates DNA to mRNA and then a protein sequence
 *
 * @author Issac Roy
 * @since 4/16/2024
 */
class ProteinSynthesis {
    private static final int CODON_LENGTH = 3;
    /**
     * Creates an RNA by replacing each occurrence of ‘T’ with ‘U’,
     * saves the result in a queue and returns it\
     * @throws IllegalArgumentException if the length of the input is not divisible by 3
     * @param dna   String of DNA
     * @return      Queue of nucleotides that make up the mRNA
     */
    public CharQueue transcribeDNA(String dna) {
        if (dna.length()%CODON_LENGTH  != 0) throw new IllegalArgumentException();
        dna = dna.replace('T', 'U');
        CharQueue rna = new CharQueue(dna.length());
        for(int i = 0; i < dna.length(); i++){
            rna.enqueue(dna.charAt(i));
        }
        return rna;
    }

    /**
     * Translates the given RNA to a protein
     * @param rna   RNA that gets translated
     * @return      Protein sequence as CharQueue
     */
    public CharQueue translateRNA(CharQueue rna) {
        CharQueue sequence = new CharQueue();
        int rnaSize = rna.size();
        boolean running = false;

        for (int i = 0; i < rnaSize; i+=CODON_LENGTH){
            String codon = "" + rna.dequeue() + rna.dequeue() + rna.dequeue();

            if (codon.equals("AUG")) running = true;
            if (running) sequence.enqueue(CodonMap.getAminoAcid(codon));
            if (codon.equals("UAA") || codon.equals("UAG") || codon.equals("UGA")) break;
        }
        return sequence;
    }
}
