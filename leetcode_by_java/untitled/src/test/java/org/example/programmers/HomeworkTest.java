package org.example.programmers;

import org.junit.jupiter.api.Test;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;

class HomeworkTest {
    Homework homework = new Homework();

    @Test
    void solution() {
//        String[][] plans = {{"korean", "11:40", "30"}, {"english", "12:10", "20"}, {"math", "12:30", "40"}};
        String[][] plans = {{"science", "12:40", "50"}, {"music", "12:20", "40"}, {"history", "14:00", "30"}, {"computer", "12:30", "100"}};

        String[] result = {"science", "history", "computer", "music"};
        homework.solution(plans);
    }

    @Test
    void convertStringToDate() throws ParseException {
        String time = "11:40";
        long duration = 30;

        SimpleDateFormat format = new SimpleDateFormat("HH:mm");
        Date date = format.parse(time);
        Date result = new Date(date.getTime() + duration * 60 * 1000);
        System.out.println(result);
    }
}