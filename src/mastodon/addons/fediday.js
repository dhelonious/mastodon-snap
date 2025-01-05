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

function initConfetto(canvas, confetto={}) {
  confetto.x = Math.random() * canvas.width;
  confetto.y = 0;
  confetto.length = Math.random() * 4 + 10;
  confetto.angle = Math.random() * 90 - 45;
  confetto.phase = Math.PI / 2 * Math.random();
  confetto.speed = Math.random() + 1;
  confetto.rotationSpeed = Math.random() - 0.5;
  confetto.phaseSpeed = 2 * Math.PI * Math.random() / canvas.height;
  confetto.color = confetti_colors[Math.floor(Math.random() * confetti_colors.length)];
  return confetto;
}

function animateConfetti(ctx, canvas, confetti, maxConfetti) {
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  // Add new confetto
  if (confetti.length < maxConfetti && Math.random() < 0.05) { // 5% chance each frame to add a new confetto
    confetti.push(initConfetto(canvas));
  }

  confetti.forEach(confetto => {
    const confettoWidth = Math.pow(Math.cos(confetto.phase), 2) * confetto.length / 3 + 0.3;

    // Draw confetto
    ctx.save();
    ctx.translate(confetto.x, confetto.y);
    ctx.rotate(confetto.angle / 180 * Math.PI);
    ctx.fillStyle = confetto.color;
    ctx.fillRect(-confettoWidth / 2, -confetto.length / 2, confettoWidth, confetto.length);
    ctx.restore();

    // Update position and orientation
    if (confetto.y > canvas.height) {
      confetto = initConfetto(canvas, confetto);
    } else {
      confetto.x += Math.sin(2 * Math.PI * confetto.speed * confetto.y / canvas.height) / 2;
      confetto.y += confetto.speed / 2;
      confetto.angle += confetto.rotationSpeed;
      confetto.phase += confetto.phaseSpeed;
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

    topEffect(animateConfetti, maxParticlesSmall=35, maxParticlesLarge=70);
  }
});
