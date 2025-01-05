// Based on snow addon by Roni Laukkarinen
// https://github.com/ronilaukkarinen/mastodon/commit/9bf1563

import { reduceMotion } from 'mastodon/initial_state';
import { topEffect } from './effects';

function initFlake(canvas, flake={}) {
  flake.x = Math.random() * canvas.width;
  flake.y = 0;
  flake.radius = Math.random() * 7 + 3;
  flake.speed = Math.random() * 0.5 + 0.3;
  flake.opacity = Math.random() * 0.4 + 0.6;
  return flake;
}

function animateSnow(ctx, canvas, snowflakes, maxFlakes) {
  // Check for other effects
  if (window.fediday) {
    return; // Don't show snow if confetti effect is there
  }
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  // Add new snowflake
  if (snowflakes.length < maxFlakes && Math.random() < 0.05) { // 5% chance each frame to add a new flake
    snowflakes.push(initFlake(canvas));
  }

  snowflakes.forEach(flake => {
    // Draw snowflake shape
    ctx.save();
    ctx.beginPath();
    for (let i = 0; i < 6; i++) {
      ctx.moveTo(flake.x, flake.y);
      ctx.lineTo(
        flake.x + Math.cos(Math.PI * 2 * i / 6) * flake.radius,
        flake.y + Math.sin(Math.PI * 2 * i / 6) * flake.radius
      );
    }
    ctx.strokeStyle = `rgba(208, 228, 242, ${flake.opacity})`;
    ctx.lineWidth = 1.5;
    ctx.stroke();
    ctx.restore();

    // Update position
    if (flake.y > canvas.height) {
      flake = initFlake(canvas, flake);
    } else {
      flake.x += Math.sin(flake.y / 50) * 0.3;
      flake.y += flake.speed * 0.5;
    }
  });

  requestAnimationFrame(() => animateSnow(ctx, canvas, snowflakes, maxFlakes));
}

document.addEventListener('DOMContentLoaded', () => {
  // Don't create snow effect if reduced motion is preferred
  if (reduceMotion) {
    return;
  }

  if (new Date().getMonth() === 11 && new Date().getDate() >= 23 && new Date().getDate() <= 31) {
    topEffect(animateSnow, fadeLength=`40px`);
  }
});
