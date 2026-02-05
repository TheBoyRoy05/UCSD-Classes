clear; clc; close all;

n = 15; %number of rows of cells
m = 15; %number of columns of cells
cells = zeros(n, m); % Preallocates the cells variable which will be used to print the inputted live cells and then the evolving figure
evolving = false; % False when cells are being inputed and true when the game is running
waitTime = 0.3; % Time between evolution states

figure; %open figure window
title('Click on the cells you wish to make live. Press <Enter> when done.', 'FontSize', 16, 'FontWeight', 'bold', 'Color', 'black');
% Creates title. Not used in the DrawCells function for higher optimization as the title is only generated once
drawCells(n, m, cells, evolving, waitTime) %Draw cells (all dead, i.e., white)