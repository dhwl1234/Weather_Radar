clear;clc;close all;

c=299792458;
f=2e9;%GHz
lambda=2;%m
type=1;%0时计算波长，1时计算雷达载频
if type==0
    lambda = c/f;
    disp(['the lambda is ' num2str(lambda) ' m = '  num2str(lambda*100) 'cm ' ]);
elseif type==1
    f = c/lambda;
    disp(['The f is ' num2str(f/1e9) ' GHz' ]);
end
