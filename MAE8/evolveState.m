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