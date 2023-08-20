package org.example.programmers;

import java.util.Arrays;
import org.junit.jupiter.api.Test;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import org.junit.jupiter.params.ParameterizedTest;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;


class HomeworkTest {
    Homework homework = new Homework();

    @Test
    void solution() {
        String[][] plans = {{"science", "12:40", "50"}, {"music", "12:20", "40"}, {"history", "14:00", "30"}, {"computer", "12:30", "100"}};

        String[] result = {"science", "history", "computer", "music"};
        homework.solution(plans);
        assertArrayEquals(result, homework.solution(plans));

    }

    @Test
    void solution2() {
        String[][] plans = {
                {"music", "12:20", "40"},
                {"computer", "12:30", "100"},
                {"science", "12:40", "50"},
                {"history", "14:00", "30"},
        };

        String[] result = {"science", "history", "computer", "music"};
        System.out.println(Arrays.toString(homework.solution(plans)));
        assertArrayEquals(result, homework.solution(plans));
    }

    @Test
    void alskdjflqwer() {
        String[][] plans = {
            {"music", "12:20", "10"},
            {"computer", "12:30", "100"},
            {"history", "14:00", "30"},
            {"science", "12:40", "50"}
        };

        String[] result = {"music", "science", "history", "computer"};
        assertArrayEquals(result, homework.solution(plans));
    }

    @Test
    void aaaa() {
        String[][] plans = {
            {"music", "12:20", "10"},
            {"computer", "12:30", "10"},
            {"science", "12:40", "10"},
            {"history", "14:00", "30"},
        };

        String[] result = {"music", "computer", "science", "history"};
        assertArrayEquals(result, homework.solution(plans));
    }
    @Test
    void asdklfjlqkr() {
        String[][] plans = {
            {"music", "12:20", "30"},
            {"computer", "12:30", "10"},
            {"science", "12:40", "10"},
            {"history", "14:00", "30"},
        };

        String[] result = {"computer", "science", "music", "history"};
        assertArrayEquals(result, homework.solution(plans));
    }
    @Test
    void alskdjflkqewrasdklfjlqkr() {
        String[][] plans = {
            {"music", "12:20", "180"},
            {"computer", "12:30", "10"},
            {"science", "12:40", "10"},
            {"history", "14:00", "30"},
        };

        String[] result = {"computer", "science", "history", "music"};
        assertArrayEquals(result, homework.solution(plans));
    }

    @Test
    void askdljflkqwjerlkjsdaf() {
        String[][] plans = {
            {"aaa", "12:00", "20"},
            {"bbb", "12:10", "30"},
            {"ccc", "12:40", "10"}
        };
        String[] result = {"bbb", "ccc", "aaa"};

        assertArrayEquals(result, homework.solution(plans));
    }

    @Test
    void alsdkjfaskdljflkqwjerlkjsdaf() {
        String[][] plans = {
            {"aaa", "12:00", "20"},
            {"bbb", "12:10", "35"},
            {"ccc", "12:40", "10"}
        };
        String[] result = {"ccc", "bbb", "aaa"};

        assertArrayEquals(result, homework.solution(plans));
    }

    @Test
    void asdkljflkqwer() {
        String[][] plans = {
            {"aaa", "00:00", "20"},
            {"bbb", "00:10", "10"},
            {"ccc", "00:20", "10"}
        };
        String[] result = {"bbb", "ccc", "aaa"};

        assertArrayEquals(result, homework.solution(plans));
    }

    @Test
    void asdkljiiiiflkqwer() {
        String[][] plans = {
            {"ddd", "00:00", "20"},
            {"aaa", "00:05", "5"},
            {"bbb", "00:10", "15"},
            {"ccc", "00:20", "10"}
        };
        String[] result = {"aaa", "ccc", "bbb", "ddd"};

        assertArrayEquals(result, homework.solution(plans));
    }

    @Test
    void alwkejrlqkjwerjlasdf() {
        String[][] plans = {
            {"science", "12:40", "50"},
            {"music", "12:20", "40"},
            {"history", "15:00", "30"},
            {"computer", "12:30", "100"}
        };

        String[] result = {"science", "computer", "history", "music"};
        assertArrayEquals(result, homework.solution(plans));
    }

    @Test
    void qlwkejrlkasjdlfkqjwre() {
        String[][] plans = {
            {"A", "11:50", "30"},
            {"B", "13:00", "20"},
            {"C", "13:10", "30"}
        };
        String[] result = {"A","C","B"};
        assertArrayEquals(result, homework.solution(plans));
    }
}
