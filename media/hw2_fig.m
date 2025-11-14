%#ok<*CLALL>; hw2_fig.m 
clear all; close all; clc
x = linspace(-10, 10, 21);
u = (-1).^x .* exp(-abs(x));

figure('Visible', 'off');
set(gca, 'Color', 'white', 'GridColor', 'black', ...
         'XColor', '#1f1f1f', 'YColor', '#1f1f1f');
box on; grid on; hold on;
fontsize(33, "points");
plot(x, u, 'LineWidth', 3);
xlim([-10, 10]);      xticks(linspace(-10, 10, 11));
ylim([-1.25, 1.25]);  yticks([-1 -.5 0 .5 1]);
exportgraphics(gcf, 'hw2_fig.pdf', 'ContentType', 'vector', 'BackgroundColor', 'none');
close(gcf);
