package org.example.programmers;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class HittingNumbersTest {

    @Test
    void aslkdjfqlkwerljasdf() {
        HittingNumbers hittingNumbers = new HittingNumbers();
//        assertEquals(20, hittingNumbers.solution(2, 3));
//        assertEquals(28, hittingNumbers.solution(1, 3));
//        assertEquals(80, hittingNumbers.solution(1, 5));
//        assertEquals(56, hittingNumbers.solution(3, 5));
//        assertEquals(40, hittingNumbers.solution(2, 4));
//
//        assertEquals(1008, hittingNumbers.solution(9, 20));
        assertEquals(952, hittingNumbers.solution(10, 20));
    }

    @Test
    void adslkfjlqwkjeraF() {
        for (int i=0; i<=10; ++i) {
            for (int j=0; j<=10; ++j) {
                if (i*i + j*j == 100) {
                    System.out.println(i + ", " + j);
                }
            }
        }
    }

    @Test
    void alskdjflqjwelrkadf() {
        int r1 = 10;
        int r2 = 20;

        int count = 0;
        for (int i=1; i<=r2; ++i) {
            int row_count = 0;

            for (int j=1; j<=r2; ++j) {
                double tmp = Math.pow(i, 2) + Math.pow(j, 2);
                if (Math.pow(r1, 2) <= tmp && tmp <= Math.pow(r2, 2)) {
                    count += 1;
                    row_count += 1;
                }
            }

            System.out.println(i + ": " + row_count);
        }

        count += (r2-r1+1);
        System.out.println(count * 4);
    }

    @Test
    void asdlkjflqwkejrljasdlfjk123() {
        int r = 20;
        int i = 12;
        System.out.println((long) Math.sqrt(Math.pow(r, 2) - Math.pow(i, 2)));
    }
}