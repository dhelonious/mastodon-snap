// Based on snow addon by Roni Laukkarinen
// https://github.com/ronilaukkarinen/mastodon/commit/9bf1563

import { me, reduceMotion } from 'mastodon/initial_state';
import { store } from 'mastodon/store';

const confetti_colors = [
  {r: 228, g: 3, b: 3}, // red
  {r: 255, g: 140, b: 0}, // orange
  {r: 255, g: 237, b: 0}, // yellow
  {r: 0, g: 128, b: 38}, // green
  {r: 0, g: 76, b: 255}, // indigo
  {r: 115, g: 41, b: 130}, // violet
];

function animate(ctx, confetti, canvas, maxItems) {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  // Add new confetto if we haven't reached the maximum
  if (confetti.length < maxItems && Math.random() < 0.05) {  // 5% chance each frame to add a new confetto
    confetti.push({
      x: Math.random() * canvas.width,
      y: 0,
      width: Math.random() * 3 + 3,
      angle: Math.random() * 60 - 30,
      speed: Math.random() * 0.5 + 0.3,
      opacity: Math.random() * 0.6 + 0.4
    });
  }
  confetti.forEach(confetto => {
    // Draw confetto
    ctx.save();
    ctx.fillRect(-confetto.width / 2, -confetto.width, confetto.width, confetto.width * 2);
    ctx.translate(confetto.x, confetto.y);
    ctx.rotate(confetto.angle / 180 * Math.PI);
    // Chose random color
    const randomColor = confetti_colors[Math.floor(Math.random() * confetti_colors.length)];
    ctx.fillStyle = `rgba(${randomColor.r}, ${randomColor.g}, ${randomColor.b}, ${confetto.opacity})`;
    ctx.restore();
    // Update position with gentler movement
    confetto.x += Math.sin(confetto.y / 50) * 0.3;
    confetto.y += confetto.speed * 0.5;
    if (confetto.y > canvas.height) {
      confetto.y = 0;
      confetto.x = Math.random() * canvas.width;
    }
  });
  requestAnimationFrame(() => animate(ctx, confetti, canvas, maxItems));
}

document.addEventListener('DOMContentLoaded', () => {
  // Check if reduced motion is enabled
  if (!me || reduceMotion) {
    return; // Don't create confetti effect if not logged in or reduced motion is preferred
  }
  const account_birthday = new Date(store.getState().getIn(['accounts', me, 'created_at']));
  console.log('Day:', new Date().getDate(), account_birthday.getDate());
  console.log('Month:', new Date().getMonth(), account_birthday.getMonth());
  if (new Date().getDate() === account_birthday.getDate() && new Date().getMonth() === account_birthday.getMonth()) {
    console.log('its your birthday');
    const wrapper = document.createElement('div');
    wrapper.classList.add('confetti');
    wrapper.style.position = 'fixed';
    wrapper.style.top = '0';
    wrapper.style.left = '0';
    wrapper.style.width = '100%';
    wrapper.style.height = '80px';
    wrapper.style.pointerEvents = 'none';
    wrapper.style.zIndex = '9999';
    wrapper.style.maskImage = 'linear-gradient(to top, rgba(0, 0, 0, 0), rgba(0, 0, 0, 1) 35px)';
    wrapper.style.webkitMaskImage = 'linear-gradient(to top, rgba(0, 0, 0, 0), rgba(0, 0, 0, 1) 35px)';
    wrapper.style.transition = 'opacity 0.3s ease-in-out';
    const canvas = document.createElement('canvas');
    canvas.style.width = '100%';
    canvas.style.height = '100%';
    canvas.width = window.innerWidth * 2;
    canvas.height = 160;
    wrapper.appendChild(canvas);
    document.body.appendChild(wrapper);
    const ctx = canvas.getContext('2d');
    const confetti = [];  // Start with empty array
    // Adjust max confettos based on viewport width
    const getMaxFlakes = () => {
      return window.innerWidth <= 800 ? 25 : 50;
    };
    let maxItems = getMaxFlakes();
    animate(ctx, confetti, canvas, maxItems);
    // Update maxItems on resize
    window.addEventListener('resize', () => {
      canvas.width = window.innerWidth * 2;
      canvas.height = 160;
      maxItems = getMaxFlakes();
      // Remove excess confetti if viewport becomes smaller
      if (confetti.length > maxItems) {
        confetti.length = maxItems;
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
