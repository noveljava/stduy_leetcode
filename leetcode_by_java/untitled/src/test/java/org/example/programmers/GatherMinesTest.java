package org.example.programmers;

import org.junit.jupiter.api.Test;

import java.util.Arrays;

import static org.junit.jupiter.api.Assertions.*;

class GatherMinesTest {

    @Test
    void alsdkjflkqwjelrasdfjlqwer() {
        String[] minerals = new String[] {"diamond", "diamond", "iron", "stone", "iron", "stone"};
        assertEquals(6, minerals.length);
        assertArrayEquals(new String[]{"stone"}, Arrays.copyOfRange(minerals, 5, 6));
    }
    @Test
    void asdlkjflajsdlkrjlqwkjer() {
        GatherMines gatherMines = new GatherMines();
        int[] picks = new int[] {1, 3, 2};
        String[] minerals = new String[] {"diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"};
        assertEquals(12, gatherMines.solution(picks, minerals));
    }

    @Test
    void aldskjflqkjwelrjk() {
        GatherMines gatherMines = new GatherMines();
        int[] picks = new int[] {0, 1, 1};
        String[] minerals = new String[] {"diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"};
        assertEquals(50, gatherMines.solution(picks, minerals));
    }
    @Test
    void aldskjflqkjwelrjkasdjf() {
        GatherMines gatherMines = new GatherMines();
        int[] picks = new int[] {1, 1, 0};
        String[] minerals = new String[] {"stone", "stone", "iron", "stone", "diamond", "diamond", "diamond", "diamond", "diamond", "diamond"};
        assertEquals(14, gatherMines.solution(picks, minerals));
    }

}