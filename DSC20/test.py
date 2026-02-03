def edge_highlight(image):
        """
        Returns a new image with the edges highlighted

        # Check output
        >>> img_proc = PremiumImageProcessing()
        >>> img = img_read_helper('img/test_image_32x32.png')
        >>> img_edge = img_proc.edge_highlight(img)
        >>> img_exp = img_read_helper('img/exp/test_image_32x32_edge.png')
        >>> img_exp.pixels == img_edge.pixels # Check edge_highlight output
        True
        >>> img_save_helper('img/out/test_image_32x32_edge.png', img_edge)
        """
        # YOUR CODE GOES HERE #
        gray = [[sum([val for val in pixel])//len(pixel) \
            for pixel in row] for row in image]
        kernel = [
            [-1, -1, -1],
            [-1,  8, -1],
            [-1, -1, -1]
        ]
        new_pixels = []
        for i, row in enumerate(gray):
            new_row = []
            for j, pixel in enumerate(row):
                new_pixel = 0
                for dy in range(-1*(i!=0), 2-1*(i==len(gray)-1)):
                    for dx in range(-1*(j!=0), 2-1*(j==len(row)-1)):
                        print(i, j, dy, dx)
                        new_pixel += kernel[dy+1][dx+1] * \
                            gray[max(0, min(i+dy, len(gray)-1))][max(0, min(j+dx, len(row)-1))]
                new_row.append([max(0, min(new_pixel, 255))]*3)
            new_pixels.append(new_row)
        return new_pixels

print(edge_highlight([
 [[215, 209, 223], [108, 185, 135], [ 54, 135,  36]],
 [[184,  20, 245], [ 32,  52, 249], [243, 155,  96]],
 [[108,  66, 116], [ 65, 200,  34], [  2, 213, 238]] 
]))