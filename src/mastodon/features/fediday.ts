// Based on snow addon by Roni Laukkarinen
// https://github.com/ronilaukkarinen/mastodon/commit/9bf1563

import { me, owner, reduceMotion } from 'mastodon/initial_state';
import { store } from 'mastodon/store';

const CONFETTI_COLORS = [
  `rgb(228, 3, 3)`, // red
  `rgb(255, 140, 0)`, // orange
  `rgb(255, 237, 0)`, // yellow
  `rgb(0, 128, 38)`, // green
  `rgb(0, 76, 255)`, // indigo
  `rgb(115, 41, 130)`, // violet
];

let maxParticles = window.innerWidth <= 800 ? 50 : 100;
let particles = [];
let wrapper = null;
let canvas = null;
let animationFrame = null;

function isFediday() {
  const state = store.getState();
  const account_created_at = new Date(state.getIn(['accounts', me, 'created_at']));
  const today = new Date()

  return (
    account_created_at
    && account_created_at.getMonth() === today.getMonth()
    && account_created_at.getDate() === today.getDate()
  );
}

function cleanup() {
  if (animationFrame !== null) {
    cancelAnimationFrame(animationFrame);
    animationFrame = null;
  }

  wrapper?.remove();
  wrapper = null;
  canvas = null;

  window.removeEventListener('scroll', fadeout);
}

function fadeout() {
  if (!canvas) return;
  const scrollTop = window.pageYOffset || document.documentElement.scrollTop;

  if (scrollTop > 40) {
    canvas.style.opacity = Math.max(0, 1 - (scrollTop - 40) / 40);
  } else {
    canvas.style.opacity = '1';
  }
}

function animate() {
  if (!canvas) return;

  const ctx = canvas.getContext('2d');
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  // Add new particle
  if (particles.length < maxParticles) {
    particles.push({
      x: Math.random() * canvas.width,
      y: 0,
      length: Math.random() * 4 + 10,
      angle: Math.random() * 90 - 45,
      phase: Math.PI / 4 * Math.random(),
      speed: 3 * Math.random() + 2,
      rotationSpeed: Math.random() - 0.5,
      phaseSpeed: (2 * Math.PI * (Math.random() - 0.5) + 0.3) / canvas.height,
      color: CONFETTI_COLORS[Math.floor(Math.random() * CONFETTI_COLORS.length)],
    });
  }


  for (let i = particles.length - 1; i >= 0; i--) {
    const confetto = particles[i];
    const confettoWidth = Math.pow(Math.cos(confetto.phase * confetto.speed), 2) * (confetto.length / 1.6 - 1) + 1;

    if (confetto.y > canvas.height) {
      // Remove particle
      particles.splice(i, 1);
      maxParticles -= 1;
    } else {
      // Update particle
      confetto.x += 2 * Math.sin(Math.PI * confetto.speed * confetto.y / canvas.height) / confetto.speed;
      confetto.y += confetto.speed / 2;
      confetto.angle += confetto.rotationSpeed;
      confetto.phase += confetto.phaseSpeed;

      // Draw particle
      ctx.save();
      ctx.translate(confetto.x, confetto.y);
      ctx.rotate(confetto.angle / 180 * Math.PI);
      ctx.fillStyle = confetto.color;
      ctx.fillRect(-confettoWidth / 2, -confetto.length / 2, confettoWidth, confetto.length);
      ctx.restore();
    }

  }

  if (particles.length > 0) {
    animationFrame = requestAnimationFrame(animate);
  } else {
    cleanup();
  }
}

document.addEventListener('DOMContentLoaded', () => {
  if (!me || !isFediday() || reduceMotion) {
    return;
  }

  console.log("🎊 It's your Fediday! 🎊");

  wrapper = document.createElement('div');
  wrapper.classList.add('fediday');
  wrapper.style.position = 'fixed';
  wrapper.style.top = '0';
  wrapper.style.left = '0';
  wrapper.style.width = '100%';
  wrapper.style.height = '80px';
  wrapper.style.pointerEvents = 'none';
  wrapper.style.zIndex = '9999';

  canvas = document.createElement('canvas');
  canvas.classList.add('confetti');
  canvas.style.width = '100%';
  canvas.style.height = '100%';
  canvas.width = window.innerWidth * 2;
  canvas.height = 140;
  canvas.style.opacity = '1';
  canvas.style.maskImage = 'linear-gradient(to top, rgba(0, 0, 0, 0), rgba(0, 0, 0, 1) 30px)';
  canvas.style.webkitMaskImage = canvas.style.maskImage;
  canvas.style.transition = 'opacity 0.3s ease-in-out';

  wrapper.appendChild(canvas);
  document.body.appendChild(wrapper);
  window.addEventListener('scroll', fadeout);

  animate();
});
