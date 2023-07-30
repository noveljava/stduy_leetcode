package org.example.leetcode;

import java.util.ArrayList;
import java.util.List;

public class ValidParentheses {
    public boolean isValid(String s) {
        List<String> stack = new ArrayList<>();

        for (int i=0; i<s.length(); ++i) {
            if (List.of("(", "[", "{").contains(String.valueOf(s.charAt(i))) ) {
                stack.add(String.valueOf(s.charAt(i)));
            } else {
                if (stack.size() == 0) {
                    return false;
                }

                String pop = stack.get(stack.size()-1);
                if (pop.equals("(") && String.valueOf(s.charAt(i)).equals(")")) {
                    stack.remove(stack.size()-1);
                } else if (pop.equals("[") && String.valueOf(s.charAt(i)).equals("]")) {
                    stack.remove(stack.size()-1);
                } else if (pop.equals("{") && String.valueOf(s.charAt(i)).equals("}")) {
                    stack.remove(stack.size()-1);
                } else {
                    return false;
                }
            }

        }

        return stack.size() == 0;
    }

}
