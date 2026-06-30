class Solution {
public:
    bool isAnagram(string s, string t) {
        int seen[26] = {};
        for (int i = 0; i < s.length(); i++) {
            seen[s[i] - 97] += 1;
        }
        for (int j = 0; j < t.length(); j++) {
            seen[t[j] - 97] -= 1;
        }
        for (int k = 0; k < 26; k++) {
            if (seen[k] != 0) {
                return false;
            }
        }

        return true;
    }
};
