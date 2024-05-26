class Solution {
    public String compressedString(String word) {
        if (word == null || word.isEmpty()) {
            return "";
        }
        
        StringBuilder ans = new StringBuilder();
        int count = 1;

        for (int i = 1; i < word.length(); i++) {
            if (word.charAt(i) == word.charAt(i - 1)) {
                count++;
                if (count == 9) {
                    ans.append(count).append(word.charAt(i - 1));
                    count = 0;
                }
            } else {
                if (count > 0) {
                    ans.append(count).append(word.charAt(i - 1));
                }
                count = 1;
            }
        }

        // Handle the last sequence
        if (count > 0) {
            ans.append(count).append(word.charAt(word.length() - 1));
        }

        return ans.toString();
    }
}
