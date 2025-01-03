// Based on snow addon by Roni Laukkarinen
// https://github.com/ronilaukkarinen/mastodon/commit/9bf1563
export function topEffect(animate, height='70px', fadeLength='30px', maxParticlesSmall=25, maxParticlesLarge=50) {
    const wrapper = document.createElement('div');
    wrapper.classList.add('particles');
    wrapper.style.position = 'fixed';
    wrapper.style.top = '0';
    wrapper.style.left = '0';
    wrapper.style.width = '100%';
    wrapper.style.height = height;
    wrapper.style.pointerEvents = 'none';
    wrapper.style.zIndex = '9999';
    wrapper.style.maskImage = `linear-gradient(to top, rgba(0, 0, 0, 0), rgba(0, 0, 0, 1) ${fadeLength})`;
    wrapper.style.webkitMaskImage = `linear-gradient(to top, rgba(0, 0, 0, 0), rgba(0, 0, 0, 1) ${fadeLength})`;
    wrapper.style.transition = 'opacity 0.3s ease-in-out';

    const canvas = document.createElement('canvas');
    canvas.style.width = '100%';
    canvas.style.height = '100%';
    canvas.width = window.innerWidth * 2;
    canvas.height = parseInt(height, 10) * 2;

    wrapper.appendChild(canvas);
    document.body.appendChild(wrapper);

    const ctx = canvas.getContext('2d');
    const particles = [];

    // Adjust max particles based on viewport width
    const getMaxParticles = () => {
      return window.innerWidth <= 800 ? maxParticlesSmall : maxParticlesLarge;
    };
    let maxParticles = getMaxParticles();
    animate(ctx, canvas, particles, maxParticles);

    // Update maxParticles on resize
    window.addEventListener('resize', () => {
      canvas.width = window.innerWidth * 2;
      canvas.height = parseInt(height, 10) * 2;
      maxParticles = getMaxParticles();
      // Remove excess particles if viewport becomes smaller
      if (particles.length > maxParticles) {
        particles.length = maxParticles;
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
