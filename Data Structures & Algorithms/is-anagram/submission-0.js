class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
            if(s.length !== t.length) return false;

            let map1 = {}
            for (let i = 0; i < s.length; i++){
                map1[s[i]] = (map1[s[i]] || 0) +1
                map1[t[i]] = (map1[t[i]] || 0) -1
 }

        return Object.values(map1).every(v=> v ===0)

        }
    }

