// Based on snow addon by Roni Laukkarinen
// https://github.com/ronilaukkarinen/mastodon/commit/9bf1563

import { me, reduceMotion } from 'mastodon/initial_state';
import { store } from 'mastodon/store';
import { topEffect } from './effects';

const confetti_colors = [
  `rgb(228, 3, 3)`, // red
  `rgb(255, 140, 0)`, // orange
  `rgb(255, 237, 0)`, // yellow
  `rgb(0, 128, 38)`, // green
  `rgb(0, 76, 255)`, // indigo
  `rgb(115, 41, 130)`, // violet
];

function animateConfetti(ctx, canvas, confetti, maxConfetti) {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  // Add new confetto if we haven't reached the maximum
  if (confetti.length < maxConfetti && Math.random() < 0.05) {  // 5% chance each frame to add a new confetto
    confetti.push({
      x: Math.random() * canvas.width,
      y: 0,
      length: Math.random() * 4 + 10,
      angle: Math.random() * 90 - 45,
      speed: Math.random() + 1,
      rotationSpeed: Math.random() * 2 - 1,
      color: confetti_colors[Math.floor(Math.random() * confetti_colors.length)],
    });
  }

  confetti.forEach(confetto => {
    const confettoPhase = Math.PI * confetto.y / canvas.height * confetto.rotationSpeed * confetto.speed;
    const confettoWidth = Math.pow(Math.cos(confettoPhase), 2) * confetto.length / 3 + 0.3;

    // Draw confetto
    ctx.save();
    ctx.translate(confetto.x, confetto.y);
    ctx.rotate(confetto.angle / 180 * Math.PI);
    ctx.fillStyle = confetto.color;
    ctx.fillRect(-confettoWidth / 2, -confetto.length / 2, confettoWidth, confetto.length);
    ctx.restore();

    // Update position
    confetto.x += Math.sin(2 * confettoPhase) / 2;
    confetto.y += confetto.speed / 2;
    confetto.angle += confetto.rotationSpeed / 2;
    if (confetto.y > canvas.height) {
      confetto.y = 0;
      confetto.x = Math.random() * canvas.width;
      confetto.angle = Math.random() * 90 - 45;
    }
  });

  requestAnimationFrame(() => animateConfetti(ctx, canvas, confetti, maxConfetti));
}

document.addEventListener('DOMContentLoaded', () => {
  // Don't create confetti effect if not logged in or reduced motion is preferred
  if (!me || reduceMotion) {
    return;
  }

  const account_fediday = new Date(store.getState().getIn(['accounts', me, 'created_at']));
  if (new Date().getDate() === account_fediday.getDate() && new Date().getMonth() === account_fediday.getMonth()) {
    // Set property for other addons to check
    window.fediday = true;

    topEffect(animateConfetti);
  }
});
