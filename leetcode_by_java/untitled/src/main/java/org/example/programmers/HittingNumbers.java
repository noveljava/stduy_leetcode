package org.example.programmers;

public class HittingNumbers {
    public long getMaxY(int i, int r) {
       return (long) Math.sqrt(Math.pow(r, 2) - Math.pow(i, 2));
    }

    public long solution(int r1, int r2) {
        long count = 0;
        for (int i=1; i<=r2; ++i) {
            if (i < r1) {
                count += (getMaxY(i, r2) - getMaxY(i, r1));

                if (Math.pow(getMaxY(i, r1), 2) + Math.pow(i, 2) == Math.pow(r1, 2)) {
                    count += 1;
                }

            } else {
                count +=  getMaxY(i, r2);
            }

        }

        count += (r2-r1+1);

        return count * 4;
    }
}
