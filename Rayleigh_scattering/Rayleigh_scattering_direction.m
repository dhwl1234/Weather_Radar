% 设置参数
lambda = 1;     % 波长
d = lambda/2;   % 天线间距
k = 2*pi/lambda;% 波数
theta = 0:pi/180:2*pi; % 方位角
phi = 0:pi/180:pi;     % 俯仰角

% 计算方向性图
[X,Y] = meshgrid(theta,phi);
theta_i = pi/2;
phi_i = pi/4;
f = (cos(k*d*(cos(X).*sin(Y)*sin(phi_i)*sin(theta_i)+cos(Y)*cos(phi_i))) .* ...
     sin(Y) .* sin(phi_i)) .^ 2;

% 画图
figure;
patternCustom(f,theta*180/pi,phi*180/pi);
title('三维瑞利散射方向性图');
xlabel('方位角（度）');
ylabel('俯仰角（度）');
zlabel('增益（dB）');