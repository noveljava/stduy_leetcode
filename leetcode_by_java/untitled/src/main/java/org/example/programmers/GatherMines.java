package org.example.programmers;

import java.util.Arrays;

public class GatherMines {
    private int result = Integer.MAX_VALUE;

    private int calculate(int pick, String mineral) {
        switch (pick) {
            case 0 -> {
                return 1;
            }
            case 1 -> {
                if ("diamond".equals(mineral))
                    return 5;
                else
                    return 1;
            }
            case 2 -> {
                if ("diamond".equals(mineral))
                    return 25;
                else if ("iron".equals(mineral)) {
                    return 5;
                } else
                    return 1;
            }
        }

        return 0;
    }

    private void recursive(int[] picks, String[] minerals, int answer) {
        if (Arrays.stream(picks).sum() == 0 || minerals.length == 0) {
            result = Integer.min(result, answer);
            return ;
        }

        int originAnswer = answer;
        for (int i=0; i<3; ++i) {
            if (picks[i] == 0) {
                continue;
            }

            int loopCount = Integer.min(5, minerals.length);

            for (int j=0; j<loopCount; ++j) {
                answer += calculate(i, minerals[j]);
            }
            int[] remindPicks = Arrays.copyOf(picks, picks.length);
            remindPicks[i] -= 1;

            String [] remindMinerals = new String[]{};
            if (minerals.length > 5) {
               remindMinerals = Arrays.copyOfRange(minerals, 5, minerals.length);
            }

            recursive(remindPicks, remindMinerals, answer);
            answer = originAnswer;
        }
    }
    public int solution(int[] picks, String[] minerals) {
        int answer = 0;

        recursive(picks, minerals, answer);

        return result;
    }
}
