function out = drawCells(n, m, cells, cellSize)
    window_size = 750;
    % Loop through rows and columns to draw cells
    for i = 1:n
        for j = 1:m
            % Calculate the position of the current cell
            x = (j - 1) * cellSize;
            y = (i - 1) * cellSize;
            
            % Draw a rectangle for each cell
            if cells(i, j) == 1
                rectangle('Position', [x, y, cellSize, cellSize], 'EdgeColor', [0.7 0.7 0.7], 'FaceColor', 'k', LineWidth', 2);
            else
                rectangle('Position', [x, y, cellSize, cellSize], 'EdgeColor', [0.7 0.7 0.7], 'LineWidth', 2);
            end
        end
    end
    
    set(gca, 'XTick', []);
    set(gca, 'YTick', []);
    set(gcf, 'Position', [400, 50, window_size, window_size]);
end