public class FloodFill {
    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
      if (image[sr][sc] == color)
        return image;

      int row = image.length;
      int col = image[0].length;

      dfs(image, sr, sc, image[sr][sc], row, col, color);

      return image;
    }

    public void dfs(int[][] image, int i, int j, int color, int row, int col, int newColor) {
      if (image[i][j] == color) {
        image[i][j] = newColor;

        if (i - 1 >= 0)
          dfs(image, i - 1, j, color, row, col, newColor);
        if (i + 1 < row)
          dfs(image, i + 1, j, color, row, col, newColor);
        if (j - 1 >= 0)
          dfs(image, i, j - 1, color, row, col, newColor);
        if (j + 1 < col)
          dfs(image, i, j + 1, color, row, col, newColor);
      }
    }
}
