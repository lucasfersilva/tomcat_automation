// Create a canvas
const canvas = document.createElement('canvas');
document.body.appendChild(canvas);

// Set canvas size
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

// Get canvas context
const ctx = canvas.getContext('2d');

// Create particles
const particles = [];
for (let i = 0; i < 100; i++) {
    particles.push({
        x: Math.random() * canvas.width,
        y: Math.random() * canvas.height,
        size: Math.random() * 5 + 1,
        speedX: Math.random() * 3 - 1.5,
        speedY: Math.random() * 3 - 1.5
    });
}

// Animate particles
function animateParticles() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    for (let i = 0; i < particles.length; i++) {
        const p = particles[i];

        ctx.beginPath();
        ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
        ctx.fill();

        p.x += p.speedX;
        p.y += p.speedY;

        if (p.x < 0) p.x = canvas.width;
        if (p.y < 0) p.y = canvas.height;
        if (p.x > canvas.width) p.x = 0;
        if (p.y > canvas.height) p.y = 0;
    }

    requestAnimationFrame(animateParticles);
}

animateParticles();
