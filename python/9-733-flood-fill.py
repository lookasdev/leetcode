class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        starting_pixel = image[sr][sc]

        if image[sr][sc] == newColor:
            return image

        self.dfs(image, sr, sc, newColor, starting_pixel)

        return image

    def dfs(self, image, sr, sc, newColor, starting_pixel):
        
        if sr < 0 or sr > len(image) - 1 or sc < 0 or sc > len(image[0]) - 1:
            return
        if image[sr][sc] != starting_pixel:
            return

        image[sr][sc] = newColor
        self.dfs(image, sr + 1, sc, newColor, starting_pixel) # up
        self.dfs(image, sr, sc + 1, newColor, starting_pixel) # right
        self.dfs(image, sr, sc - 1, newColor, starting_pixel) # left
        self.dfs(image, sr - 1, sc, newColor, starting_pixel) # down
