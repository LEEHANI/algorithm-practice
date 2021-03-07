class Solution {
    // O(n), O(n)
    public int distributeCandies(int[] candyType) {
        Map<Integer, Integer> map = new HashMap<>();
        
        for(int type : candyType) {
            map.put(type, map.get(type) == null ? 1 : map.get(type)+1);    
        }
        
        if(candyType.length/2 < map.keySet().size()) {
            return candyType.length/2;
        } else {
            return map.keySet().size();
        }
    }
}