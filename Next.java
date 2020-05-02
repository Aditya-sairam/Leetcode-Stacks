//Finding the next greater element 1 problem in leetcode 
class Next {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        Map<Integer,Integer> hashing = new HashMap<Integer,Integer>();
        Stack<Integer> stack = new Stack<Integer>();
        
        int i;
        int n = nums2.length;
        int m = nums1.length;
        
        for(i=0;i<n;i++){
            while(!stack.isEmpty() && stack.peek() < nums2[i]){
                hashing.put(stack.pop(),nums2[i]);
            }
            stack.push(nums2[i]);
        }
        int[] finale = new int[m];
        for(i=0;i<m;i++){
            finale[i] = hashing.getOrDefault(nums1[i],-1);
        }
        return finale;
    }
}
