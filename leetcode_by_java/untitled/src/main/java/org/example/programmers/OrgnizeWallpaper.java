package org.example.programmers;

import java.util.Arrays;

public class OrgnizeWallpaper {
    public int[] solution(String[] wallpaper) {
        int[] answer = {};
        int minX = Integer.MAX_VALUE;
        int minY = Integer.MAX_VALUE;

        int maxX = Integer.MIN_VALUE;
        int maxY = Integer.MIN_VALUE;

        for(int i=0; i<wallpaper.length; i++){
            for(int j=0; j<wallpaper[i].length(); j++){
                if(wallpaper[i].charAt(j) == '#'){
                    minX = Math.min(minX, i);
                    minY = Math.min(minY, j);
                    maxX = Math.max(maxX, i);
                    maxY = Math.max(maxY, j);
                }
            }
        }

        maxX += 1;
        maxY += 1;
        answer = Arrays.asList(minX, minY, maxX, maxY).stream().mapToInt(Integer::intValue).toArray();
        return answer;
    }
}
