class Solution {
    /**
     * @param {number[]} arr
     * @return {number[]}
     */
    replaceElements(arr) {
        let maximumnum = -1
        
        for(let i = arr.length -1 ; i >= 0; i--){
            let currentvalue = arr[i]
            arr[i] = maximumnum

            maximumnum = Math.max(maximumnum, currentvalue)



        }
        return arr
    }
}
