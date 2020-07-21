class SumRootToLeafNumbers {
	int answer=0;
    public int sumNumbers1(TreeNode root) {
    	dfs(root, 0);
        return answer;
    }
    
    public void dfs(TreeNode node, int num) {
    	if(node!=null) {
    		if(node.left==null && node.right==null) {
    			answer+=num*10+node.val;
    		}
    		dfs(node.left, num*10+node.val);
    		dfs(node.right, num*10+node.val);
    	} 
    }
}