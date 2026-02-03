import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class ProteinSynthesisTest {
    @Test
    void synthesisTest1(){
        ProteinSynthesis synthesis = new ProteinSynthesis();
        String dna = "ATGATCTCGTAA";
        String expectedRNA = "AUGAUCUCGUAA";
        String expectedSequence = "MIS*";
        CharQueue rna = synthesis.transcribeDNA(dna);
        CharQueue rnaCopy = synthesis.transcribeDNA(dna);

        assertEquals(expectedRNA.length(), rna.size());
        for (int i = 0; i < dna.length(); i++) {
            assertEquals(rna.dequeue(), expectedRNA.charAt(i));
        }
        CharQueue sequence = synthesis.translateRNA(rnaCopy);
        assertEquals(expectedSequence.length(), sequence.size());
        for (int i = 0; i < sequence.size(); i++) {
            assertEquals(sequence.dequeue(), expectedSequence.charAt(i));
        }
    }

    @Test
    void synthesisTest2(){
        ProteinSynthesis synthesis = new ProteinSynthesis();
        String dna = "CCCCTGTCATAA";
        String expectedRNA = "CCCCUGUCAUAA";
        String expectedSequence = "";
        CharQueue rna = synthesis.transcribeDNA(dna);
        CharQueue rnaCopy = synthesis.transcribeDNA(dna);

        assertEquals(expectedRNA.length(), rna.size());
        for (int i = 0; i < dna.length(); i++) {
            assertEquals(rna.dequeue(), expectedRNA.charAt(i));
        }

        CharQueue sequence = synthesis.translateRNA(rnaCopy);
        assertEquals(expectedSequence.length(), sequence.size());
        for (int i = 0; i < sequence.size(); i++) {
            assertEquals(sequence.dequeue(), expectedSequence.charAt(i));
        }
    }

    @Test
    void synthesisTest3(){
        ProteinSynthesis synthesis = new ProteinSynthesis();
        String dna = "ATGCTATGT";
        String expectedRNA = "AUGCUAUGU";
        String expectedSequence = "MLC";
        CharQueue rna = synthesis.transcribeDNA(dna);
        CharQueue rnaCopy = synthesis.transcribeDNA(dna);

        assertEquals(expectedRNA.length(), rna.size());
        for (int i = 0; i < dna.length(); i++) {
            assertEquals(rna.dequeue(), expectedRNA.charAt(i));
        }

        CharQueue sequence = synthesis.translateRNA(rnaCopy);
        assertEquals(expectedSequence.length(), sequence.size());
        for (int i = 0; i < sequence.size(); i++) {
            assertEquals(sequence.dequeue(), expectedSequence.charAt(i));
        }
    }

    @Test
    void synthesisTest4(){
        ProteinSynthesis synthesis = new ProteinSynthesis();
        String dna = "TGTCTAATGCTATGT";
        String expectedRNA = "UGUCUAAUGCUAUGU";
        String expectedSequence = "MLC";
        CharQueue rna = synthesis.transcribeDNA(dna);
        CharQueue rnaCopy = synthesis.transcribeDNA(dna);

        assertEquals(expectedRNA.length(), rna.size());
        for (int i = 0; i < dna.length(); i++) {
            assertEquals(rna.dequeue(), expectedRNA.charAt(i));
        }

        CharQueue sequence = synthesis.translateRNA(rnaCopy);
        assertEquals(expectedSequence.length(), sequence.size());
        for (int i = 0; i < sequence.size(); i++) {
            assertEquals(sequence.dequeue(), expectedSequence.charAt(i));
        }
    }

    @Test
    void synthesisTest5(){
        ProteinSynthesis synthesis = new ProteinSynthesis();
        String dna = "ATGTCGTAATGT";
        String expectedRNA = "AUGUCGUAAUGU";
        String expectedSequence = "MS*";
        CharQueue rna = synthesis.transcribeDNA(dna);
        CharQueue rnaCopy = synthesis.transcribeDNA(dna);

        assertEquals(expectedRNA.length(), rna.size());
        for (int i = 0; i < dna.length(); i++) {
            assertEquals(rna.dequeue(), expectedRNA.charAt(i));
        }

        CharQueue sequence = synthesis.translateRNA(rnaCopy);
        assertEquals(expectedSequence.length(), sequence.size());
        for (int i = 0; i < sequence.size(); i++) {
            assertEquals(sequence.dequeue(), expectedSequence.charAt(i));
        }
    }

    @Test
    void synthesisTest6(){
        ProteinSynthesis synthesis = new ProteinSynthesis();
        String dna = "CTAATGTCGTAATGT";
        String expectedRNA = "CUAAUGUCGUAAUGU";
        String expectedSequence = "MS*";
        CharQueue rna = synthesis.transcribeDNA(dna);
        CharQueue rnaCopy = synthesis.transcribeDNA(dna);

        assertEquals(expectedRNA.length(), rna.size());
        for (int i = 0; i < dna.length(); i++) {
            assertEquals(rna.dequeue(), expectedRNA.charAt(i));
        }

        CharQueue sequence = synthesis.translateRNA(rnaCopy);
        assertEquals(expectedSequence.length(), sequence.size());
        for (int i = 0; i < sequence.size(); i++) {
            assertEquals(sequence.dequeue(), expectedSequence.charAt(i));
        }
    }

    @Test
    void badInput(){
        ProteinSynthesis synthesis = new ProteinSynthesis();
        String dna = "TACAT";
        assertThrows(IllegalArgumentException.class, () -> {
            CharQueue rna = synthesis.transcribeDNA(dna);
        });
    }
}
