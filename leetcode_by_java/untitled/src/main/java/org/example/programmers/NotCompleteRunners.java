package org.example.programmers;

import java.util.HashMap;
import java.util.Map;

public class NotCompleteRunners {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        Map<String, Integer> count = new HashMap<>();
        for(String e : participant) {
            count.put(e, count.getOrDefault(e, 0) + 1);
        }

        for(String e : completion) {
            count.put(e, count.get(e) - 1);
        }

        for(Map.Entry<String, Integer> e : count.entrySet()) {
            if (e.getValue() != 0) {
                answer = e.getKey();
                break;
            }
        }

        return answer;
    }
}
