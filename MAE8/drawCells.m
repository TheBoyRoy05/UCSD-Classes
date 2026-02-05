function drawCells(n, m, cells, evolving, waitTime)
    windowSize = 750;
    % Loop through rows and columns to draw cells
    prevCells = ones(n, m);
    while ~isequal(cells, prevCells)
        prevCells = cells;
        for i = 1:n
            for j = 1:m
                % Evolve the state of the current cell
                if evolving
                    cells(i, j) = evolveState(prevCells, i, j);
                end
    
                % Calculate the position of the current cell
                x = j - 1;
                y = i - 1;
                
                % Draw a rectangle for each cell
                if prevCells(i, j) == 1
                    color = 'k'; % black
                else
                    color = 'w'; % white
                end
                rectangle('Position', [x, y, 1, 1], 'EdgeColor', [0.7 0.7 0.7], 'FaceColor', color, 'LineWidth', 2);
            end
        end
        pause(waitTime);
    end

    if evolving
        title('Still Life');
    end
    
    set(gca, 'XTick', []);
    set(gca, 'YTick', []);
    set(gcf, 'Position', [400, 50, windowSize, windowSize]);
    set(gcf, 'WindowButtonDownFcn', @inputLiveCells);
    set(gcf, 'KeyReleaseFcn', @keyReleasedCallback);

    function inputLiveCells(~, ~)
        if ~evolving
            currentPoint = get(gca, 'CurrentPoint');
            x = floor(currentPoint(1, 1)) + 1;
            y = floor(currentPoint(1, 2)) + 1;
            cells(y, x) = (cells(y, x) == 0);
            drawCells(n, m, cells, evolving, waitTime);
        end
    end

    function keyReleasedCallback(~, event)
        if ~evolving && isequal(event.Key, 'return')
            evolving = true;
            title('Game of Life');
            drawCells(n, m, cells, evolving, waitTime);
        end
    end
end