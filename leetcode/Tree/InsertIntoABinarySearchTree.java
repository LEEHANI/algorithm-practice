class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

public class InsertIntoABinarySearchTree {

    public static void main(String[] args) {
        TreeNode node1 = new TreeNode(1);
        TreeNode node2 = new TreeNode(3);
        TreeNode node3 = new TreeNode(2, node1, node2);
        TreeNode node4 = new TreeNode(7);
        TreeNode root = new TreeNode(4, node3, node4);

        System.out.println(insertIntoBST(root, 5));
        System.out.println(root);
    }

    public static TreeNode insertIntoBST(TreeNode root, int val) {
        if(root == null) return new TreeNode(val);

        if(root.val<val) {
            if(root.right!=null)
                insertIntoBST(root.right, val);
            else
                root.right = new TreeNode(val);
        } else {
            if(root.left!=null)
                insertIntoBST(root.left, val);
            else
                root.left = new TreeNode(val);
        }
        return root;
    }
}
