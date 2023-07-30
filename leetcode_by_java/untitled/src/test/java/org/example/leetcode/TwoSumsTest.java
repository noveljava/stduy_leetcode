package org.example.leetcode;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class TwoSumsTest {
    private final TwoSums twoSums = new TwoSums();

    @Test
    public void asdfaera() {
        int[] nums = {2, 7, 11, 15};
        int target = 9;
        assert twoSums.twoSum(nums, target) == new int[]{0, 1};
    }
}