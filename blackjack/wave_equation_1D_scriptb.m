%% Solving the wave equation in 1D with finite difference

% spatial grid
Nx = 100;
dx = 1e-3;
x = (0:Nx-1)*dx;

% sound speed
c0 = 1500;

% time variable
Nt = 40;
dt = dx / c0;





% set the initial waveform
pulsewidth = 5*dx;
offset = dx * Nx/2;
p_n = exp(-((x-offset)/pulsewidth).^2 );

% plot the initial waveform
figure
plot(x, p_n, '-')

% set the previous pressure waveform to be the same as current
p_nm1 = p_n;

% initialise pressure waveform for next timestep
p_np1 = zeros(1, Nx);

% open figure
figure




% time loop
for n = 1:Nt
    
    % calculate new value for p^(n+1)
    p_np1(2:end-1) = 2*p_n(2:end-1) - p_nm1(2:end-1) + ...
        (c0 * dt / dx)^2 * (p_n(3:end) - 2*p_n(2:end-1) + p_n(1:end-2));
    
    % copy the pressure from n to n-1
    p_nm1 = p_n;
    
    % copy the pressure from n+1 to n
    p_n = p_np1;

    % plot
    plot(p_np1, '-');
    drawnow;
    pause(0.1);
end

