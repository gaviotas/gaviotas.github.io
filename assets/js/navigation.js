(() => {
  const navigation = document.querySelector('.navbar');
  if (!navigation) return;

  const items = Array.from(navigation.querySelectorAll('a')).map((link) => ({
    link,
    section: document.getElementById(new URL(link.href).hash.slice(1)),
  })).filter((item) => item.section);
  if (!items.length) return;

  let queued = false;
  const update = () => {
    queued = false;
    const offset = getComputedStyle(navigation).position === 'sticky'
      ? navigation.getBoundingClientRect().height + 24
      : 24;
    let current = items[0];
    for (const item of items) {
      if (item.section.getBoundingClientRect().top <= offset) current = item;
    }
    if (window.scrollY + window.innerHeight >= document.documentElement.scrollHeight - 2) {
      current = items[items.length - 1];
    }
    for (const item of items) {
      if (item === current) item.link.setAttribute('aria-current', 'location');
      else item.link.removeAttribute('aria-current');
    }
  };
  const schedule = () => {
    if (queued) return;
    queued = true;
    requestAnimationFrame(update);
  };

  window.addEventListener('scroll', schedule, { passive: true });
  window.addEventListener('resize', schedule);
  window.addEventListener('load', schedule);
  window.addEventListener('hashchange', schedule);
  update();
})();
