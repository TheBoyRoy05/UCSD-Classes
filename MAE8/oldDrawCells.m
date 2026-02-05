function oldDrawCells(fig, n, m, cells, cellSize)
    window_size = 750;
    % Loop through rows and columns to draw cells
    for i = 1:n
        for j = 1:m
            % Calculate the position of the current cell
            x = (j - 1) * cellSize;
            y = (i - 1) * cellSize;
            
            % Draw a rectangle for each cell
            if cells(i, j) == 1
                rectangle('Position', [x, y, cellSize, cellSize], 'EdgeColor', [0.7 0.7 0.7], 'FaceColor', 'k', 'LineWidth', 2);
            else
                rectangle('Position', [x, y, cellSize, cellSize], 'EdgeColor', [0.7 0.7 0.7], 'FaceColor', 'w', 'LineWidth', 2);
            end
        end
    end
    
    set(gca, 'XTick', []);
    set(gca, 'YTick', []);
    set(gcf, 'Position', [400, 50, window_size, window_size]);

    set(gcf, 'WindowButtonDownFcn', @inputLiveCells);
    set(fig, 'KeyReleaseFcn', @keyReleasedCallback);

    function inputLiveCells(~, ~)
        currentPoint = get(gca, 'CurrentPoint');
        x = floor(currentPoint(1, 1)/cellSize) + 1;
        y = floor(currentPoint(1, 2)/cellSize) + 1;
        cells(y, x) = 1;
        oldDrawCells(fig, n, m, cells, cellSize);
    end

    function evolveState(cells)
        title('');
        nextcells = zeros(size(cells));
        while ~isequal(cells,nextcells)
            tic
            live_neighbors = zeros(size(cells));
            for i = 1:n
                for j = 1:m
                    % Check the neighboring cells (both horizontally/vertically and diagonally)
                    for u = -1:1
                        for v = -1:1
                            % Skip the central cell itself
                            if u == 0 && v == 0
                                continue;
                            end
                            
                            % Calculate the indices of the neighboring cell
                            neighborRow = i + u;
                            neighborCol = j + v;
                            
                            % Check if the indices are within bounds
                            if neighborRow >= 1 && neighborRow <= n && neighborCol >= 1 && neighborCol <= m
                                % Increment the count if the neighboring cell is alive
                                live_neighbors(i, j) = live_neighbors(i, j) + cells(neighborRow, neighborCol);
                            end
                        end
                    end
                end
            end

            for i = 1:n
                for j = 1:m
                    if cells(i,j) == 1
                        if live_neighbors(i,j) == 2 
                            nextcells(i,j) = 1;
                        elseif live_neighbors(i,j) == 3
                            nextcells(i,j) = 1;
                        else
                            nextcells(i,j) = 0;
                        end
                    else
                        if live_neighbors(i,j) == 3
                            nextcells(i,j) = 1;
                        else
                            nextcells(i,j) = 0;
                        end
                    end
                end
            end
            if cells == nextcells
               break
            end
            cells = nextcells;
            oldDrawCells(fig, n, m, cells, cellSize);
            toc
            pause(0.3)
            evolveState(cells)
        end
        title('Still Life')
    end

    function keyReleasedCallback(~, event)
         key = event.Key;
         if isequal(key, 'return')
             evolveState(cells)
             set(gcf,'WindowButtonDownFcn',[]);
         end
    end
end