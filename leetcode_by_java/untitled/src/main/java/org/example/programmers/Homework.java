package org.example.programmers;

import java.util.*;
import java.util.stream.Collectors;

public class Homework {

    class Subject {
        String name;
        int start;
        int playtime;

        Subject(String name, String start, String playtime) {
            this.name = name;
            setStart(start);
            this.playtime = Integer.parseInt(playtime);
        }

        private void setStart(String start) {
            String[] tmp = start.split(":");
            this.start = Integer.parseInt(tmp[0]) * 60 + Integer.parseInt(tmp[1]);
        }

        public int getStart() {
            return this.start;
        }

        public int getPlaytime() {
            return this.playtime;
        }

        public void setPlaytime(int playtime) {
            this.playtime = playtime;
        }

        public String getName() {
            return this.name;
        }

        @Override
        public String toString() {
            return this.name;
        }
    }

    public String[] solution(String[][] tmp) {
        Deque<Subject> plans = new ArrayDeque<>();
        Stack<Subject> temporary = new Stack<>();

        setting(tmp, plans);

        int timer = plans.peek().getStart();
        List<String> result = new ArrayList<>();

        while (!plans.isEmpty()) {
            // 진행중이던 과제를 끝냈을 때, 잠시 멈춘 과제가 있다면, 멈춰둔 과제를 이어서 진행합니다.
            Subject processingSubject = null;
            if (!temporary.isEmpty() && plans.peek().getStart() > timer) {
                processingSubject = temporary.pop();
            } else {
                processingSubject = plans.pop();
                timer = processingSubject.getStart();
            }

            int expectedEndTime = timer + processingSubject.getPlaytime();

            if (!plans.isEmpty() && expectedEndTime > plans.peek().getStart()) {
                int remindPlayTime = expectedEndTime - plans.peek().getStart();
                processingSubject.setPlaytime(remindPlayTime);
                temporary.push(processingSubject);
                timer = plans.peek().getStart();

                continue;
            }

            timer = expectedEndTime;
            result.add(processingSubject.getName());
        }

        while (!temporary.isEmpty()) {
            result.add(temporary.pop().getName());
        }

        return result.toArray(new String[0]);
    }

    void setting(String[][] plans, Deque<Subject> sortedPlans) {
        List<Subject> tempPlans = new ArrayList<>();
        for(String[] e : plans) {
            tempPlans.add(new Subject(e[0], e[1], e[2]));
        }
        tempPlans.sort(Comparator.comparingInt(Subject::getStart));

        sortedPlans.addAll(tempPlans);
    }
}
