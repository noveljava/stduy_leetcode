package org.example.programmers;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class NotCompleteRunnersTest {

    @Test
    public void asldjflqkjwelkrasdf() {

        NotCompleteRunners notCompleteRunners = new NotCompleteRunners();
        String[] participant = {"mislav", "stanko", "mislav", "ana"};
        String[] completion = {"stanko", "ana", "mislav"};
        assertEquals(notCompleteRunners.solution(participant, completion), "mislav");
    }

}