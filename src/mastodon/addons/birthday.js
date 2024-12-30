// Based on snow addon by Roni Laukkarinen
// https://github.com/ronilaukkarinen/mastodon/commit/9bf1563

import { me, reduceMotion } from 'mastodon/initial_state';
import { store } from 'mastodon/store';

const confetti_colors = [
  `rgb(228, 3, 3)`, // red
  `rgb(255, 140, 0)`, // orange
  `rgb(255, 237, 0)`, // yellow
  `rgb(0, 128, 38)`, // green
  `rgb(0, 76, 255)`, // indigo
  `rgb(115, 41, 130)`, // violet
];

function animate(ctx, confetti, canvas, maxConfetti) {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  // Add new confetto if we haven't reached the maximum
  if (confetti.length < maxConfetti && Math.random() < 0.05) {  // 5% chance each frame to add a new confetto
    confetti.push({
      x: Math.random() * canvas.width,
      y: 0,
      width: Math.random() * 2 + 5,
      angle: Math.random() * 60 - 30,
      speed: Math.random() * 1 + 1,
      rotationSpeed: Math.random() * 1.6 - 0.8,
      color: confetti_colors[Math.floor(Math.random() * confetti_colors.length)],
    });
  }
  confetti.forEach(confetto => {
    // Draw confetto
    ctx.save();
    ctx.translate(confetto.x, confetto.y);
    ctx.rotate(confetto.angle / 180 * Math.PI);
    ctx.fillStyle = confetto.color;
    ctx.fillRect(-confetto.width / 2, -confetto.width, confetto.width, confetto.width * 2);
    ctx.restore();
    // Update position with gentler movement and swaying
    const phase = confetto.rotationSpeed / Math.abs(confetto.rotationSpeed) * (confetto.y % (confetto.speed * 100)) / (confetto.speed * 100);
    confetto.x += Math.sin(phase * 2 * Math.PI) * 0.5;
    confetto.y += confetto.speed * 0.5;
    confetto.angle += confetto.rotationSpeed * 0.5;
    if (confetto.y > canvas.height) {
      confetto.y = 0;
      confetto.x = Math.random() * canvas.width;
    }
  });
  requestAnimationFrame(() => animate(ctx, confetti, canvas, maxConfetti));
}

document.addEventListener('DOMContentLoaded', () => {
  // Check if reduced motion is enabled
  if (!me || reduceMotion) {
    return; // Don't create confetti effect if not logged in or reduced motion is preferred
  }
  const account_fediday = new Date(store.getState().getIn(['accounts', me, 'created_at']));
  if (new Date().getDate() === account_fediday.getDate() && new Date().getMonth() === account_fediday.getMonth()) {
    // Set property for other addons to check
    window.fediday = true;
    const width = window.innerWidth * 2;
    const height = 140;
    const fadeDistance = '40px';
    const wrapper = document.createElement('div');
    wrapper.classList.add('confetti');
    wrapper.style.position = 'fixed';
    wrapper.style.top = '0';
    wrapper.style.left = '0';
    wrapper.style.width = '100%';
    wrapper.style.height = '80px';
    wrapper.style.pointerEvents = 'none';
    wrapper.style.zIndex = '9999';
    wrapper.style.maskImage = `linear-gradient(to top, rgba(0, 0, 0, 0), rgba(0, 0, 0, 1) ${fadeDistance})`;
    wrapper.style.webkitMaskImage = `linear-gradient(to top, rgba(0, 0, 0, 0), rgba(0, 0, 0, 1) ${fadeDistance})`;
    wrapper.style.transition = 'opacity 0.3s ease-in-out';
    const canvas = document.createElement('canvas');
    canvas.style.width = '100%';
    canvas.style.height = '100%';
    canvas.width = width;
    canvas.height = height;
    wrapper.appendChild(canvas);
    document.body.appendChild(wrapper);
    const ctx = canvas.getContext('2d');
    const confetti = [];  // Start with empty array
    // Adjust max confettos based on viewport width
    const getMaxConfetti = () => {
      return window.innerWidth <= 800 ? 25 : 50;
    };
    let maxConfetti = getMaxConfetti();
    animate(ctx, confetti, canvas, maxConfetti);
    // Update maxConfetti on resize
    window.addEventListener('resize', () => {
      canvas.width = width;
      canvas.height = height;
      maxConfetti = getMaxConfetti();
      // Remove excess confetti if viewport becomes smaller
      if (confetti.length > maxConfetti) {
        confetti.length = maxConfetti;
      }
    });
    window.addEventListener('scroll', () => {
      const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
      if (scrollTop > 100) {
        wrapper.style.opacity = Math.max(0, 1 - (scrollTop - 100) / 200);
      } else {
        wrapper.style.opacity = '1';
      }
    });
  }
});
