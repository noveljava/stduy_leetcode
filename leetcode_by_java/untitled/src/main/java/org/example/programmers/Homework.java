package org.example.programmers;

import java.util.*;

public class Homework {
    class Subject {
        String name;
        long startTime;
        long endTime;
        long duration;
        long remindDuration;

        public Subject(String name, String startTime, String duration) {
            this.name = name;
            this.startTime = this.totalMinutes(startTime);
            this.duration = Long.parseLong(duration);
            this.endTime = this.startTime + this.duration;
            this.remindDuration = this.duration;
        }

        private long totalMinutes(String time) {
            String[] times = time.split(":");
            return Long.parseLong(times[0]) * 60 + Long.parseLong(times[1]);
        }

        public void setRemindDuration(long finishDuration) {
            this.remindDuration = this.remindDuration - finishDuration;
        }
    }

    public String[] solution(String[][] plans) {
        String[] answer = {};
        List<Subject> subjectList = new ArrayList<>();
        Stack<Subject> stack = new Stack<>();

        for (String[] plan : plans) {
            subjectList.add(new Subject(plan[0], plan[1], plan[2]));
        }

        subjectList.sort((o1, o2) -> (int) (o1.startTime - o2.startTime));
        Queue<Subject> queue = new LinkedList<>(subjectList);

        int idx = 1;
        long currentTime = subjectList.get(0).startTime;
        List<String> result = new ArrayList<>();

        Subject subject = queue.poll();
        while (!queue.isEmpty() || !stack.empty()) {
           Subject nextSubject = queue.poll();
            if (nextSubject.startTime <= subject.endTime) {
                long remindDuration = subject.endTime - nextSubject.startTime;
                subject.setRemindDuration(remindDuration);
                currentTime = nextSubject.startTime;

                stack.push(subject);
                subject = nextSubject;
            } else {
                result.add(subject.name);
                currentTime = subject.endTime;

                queue.add(stack.pop());
            }
        }

        System.out.print(result);
        return answer;
   }
}
