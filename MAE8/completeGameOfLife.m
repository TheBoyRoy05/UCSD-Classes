clear; clc; close all;

n = 15; %number of rows of cells
m = 15; %number of columns of cells
cells = zeros(n, m); % Preallocates the cells variable which will be used to print the inputted live cells and then the evolving figure
evolving = false; % False when cells are being inputed and true when the game is running
waitTime = 0.3; % Time between evolution states
terminate = false;

figure; %open figure window
title('Click on the cells you wish to make live. Press <Enter> when done.', 'FontSize', 16, 'FontWeight', 'bold', 'Color', 'black');

% Creates title. Not used in the DrawCells function for higher optimization as the title is only generated once
drawCells(n, m, cells, evolving, waitTime, terminate) %Draw cells (all dead, i.e., white)

function drawCells(n, m, cells, evolving, waitTime, terminate)
    prevCells = ones(n, m);
    windowSize = 750;
    set(gca, 'XTick', []);
    set(gca, 'YTick', []);
    set(gcf, 'Position', [400, 50, windowSize, windowSize]);
    set(gcf, 'WindowButtonDownFcn', @inputLiveCells);
    set(gcf, 'KeyReleaseFcn', @keyReleasedCallback);
    set(gcf, 'CloseRequestFcn', @stopRunningCode);

    function stopRunningCode(src, ~)
        delete(src)
        terminate = true;
    end

    while ~isequal(cells, prevCells) && ~terminate
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

    if evolving && ~terminate
        title('Still Life');
    end

    function newVal = evolveState(cells, i, j)
        n = size(cells, 1);
        m = size(cells, 2);
        numNeighbors = sum(sum(cells(i-(i>1):i+(i<n), j-(j>1):j+(j<m)))) - (cells(i, j));
        if cells(i, j)
            newVal = numNeighbors == 2 || numNeighbors == 3;
        else
            newVal = numNeighbors == 3;
        end
    end
    
    function inputLiveCells(~, ~)
        if ~evolving
            currentPoint = get(gca, 'CurrentPoint');
            x = floor(currentPoint(1, 1)) + 1;
            y = floor(currentPoint(1, 2)) + 1;
            cells(y, x) = (cells(y, x) == 0);
            drawCells(n, m, cells, evolving, waitTime, terminate);
        end
    end

    function keyReleasedCallback(~, event)
        if ~evolving && isequal(event.Key, 'return')
            evolving = true;
            title('Game of Life');
            drawCells(n, m, cells, evolving, waitTime, terminate);
        end
    end
end

