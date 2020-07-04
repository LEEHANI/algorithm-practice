public class Binary_Tree_Level_Order_Traversal_2 {
    public List<List<Integer>> levelOrderBottom(TreeNode root) {
		List<List<Integer>> answer = new ArrayList<>();
		
		dfs(root, 0, answer);
		
		Collections.reverse(answer);
		
        return answer;
    }
	
	public void dfs(TreeNode node, int depth, List<List<Integer>> answer) {
		if(node!=null) {
			List<Integer> list = null;
			try {
				list = answer.get(depth);
				list.add(node.val);
			} catch (Exception e) {
				list = new ArrayList<>();
				list.add(node.val);
				answer.add(depth, list);
			}
			
			dfs(node.left, depth+1, answer);
			dfs(node.right, depth+1, answer);
		}
	}
}