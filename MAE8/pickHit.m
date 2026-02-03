function out = inputLiveCells(cells, cellSize)
    currentPoint = get(gca, 'CurrentPoint');
    x = floor(currentPoint(1, 1)/cellSize);
    y = floor(currentPoint(1, 2)/cellSize);

    out = cells;
    out(x, y) = 1;
    disp(['Clicked at X: ', num2str(x, '%.2f'), ', Y: ', num2str(y, '%.2f')]);
end