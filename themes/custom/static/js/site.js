(() => {
    'use strict';

    const toggle = document.querySelector('.nav-toggle');
    const menu = document.querySelector('.nav-menu');
    const closeMenu = () => {
        if (!toggle || !menu) return;
        menu.classList.remove('nav-menu--open');
        toggle.classList.remove('nav-toggle--open');
        toggle.setAttribute('aria-expanded', 'false');
        toggle.setAttribute('aria-label', 'Open navigation');
    };
    if (toggle && menu) {
        toggle.addEventListener('click', () => {
            const open = menu.classList.toggle('nav-menu--open');
            toggle.classList.toggle('nav-toggle--open', open);
            toggle.setAttribute('aria-expanded', String(open));
            toggle.setAttribute('aria-label', open ? 'Close navigation' : 'Open navigation');
        });
        menu.addEventListener('click', event => {
            if (event.target.closest('a')) closeMenu();
        });
        document.addEventListener('keydown', event => {
            if (event.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') {
                closeMenu();
                toggle.focus();
            }
        });
        document.addEventListener('click', event => {
            if (!event.target.closest('.site-nav')) closeMenu();
        });
        const desktop = window.matchMedia('(min-width: 641px)');
        desktop.addEventListener('change', event => { if (event.matches) closeMenu(); });
        menu.querySelectorAll('a').forEach(link => {
            const path = new URL(link.href, window.location.href).pathname;
            if (path === window.location.pathname || (path.endsWith('/projects.html') && (window.location.pathname.includes('/projects/') || window.location.pathname.endsWith('/research/'))) || (path.endsWith('/opensource.html') && window.location.pathname.includes('/opensource/')) || (path.endsWith('/blog/') && window.location.pathname.includes('/blog/'))) {
                link.setAttribute('aria-current', 'page');
            }
        });
    }

    const filters = document.querySelector('.research-filters');
    if (filters) {
        const cards = Array.from(document.querySelectorAll('#research-results [data-research-kind]'));
        const count = document.getElementById('filter-count');
        filters.hidden = false;
        filters.addEventListener('click', event => {
            const button = event.target.closest('button[data-filter]');
            if (!button) return;
            filters.querySelectorAll('button').forEach(item => item.setAttribute('aria-pressed', String(item === button)));
            let visible = 0;
            cards.forEach(card => {
                const show = button.dataset.filter === 'all' || card.dataset.researchKind === button.dataset.filter;
                card.hidden = !show;
                if (show) visible++;
            });
            count.textContent = visible + (visible === 1 ? ' study' : ' studies');
        });
    }

    const canvas = document.getElementById('automaton');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    if (!ctx) return;

    const width = 680;
    const height = 480;
    const ratio = Math.min(window.devicePixelRatio || 1, 2);
    canvas.width = width * ratio;
    canvas.height = height * ratio;
    ctx.setTransform(ratio, 0, 0, ratio, 0, 0);

    const columns = 109;
    const maxRows = 53;
    const generationLabel = document.getElementById('generation');
    const pauseButton = document.getElementById('automaton-pause');
    const resetButton = document.getElementById('automaton-reset');
    const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
    let paused = reducedMotion.matches;
    let inView = true;
    let timer = null;
    let rows = [];
    let generation = 0;
    let seedVersion = 0;

    function advance() {
        const previous = rows[rows.length - 1];
        const next = new Uint8Array(columns);
        for (let column = 0; column < columns; column++) {
            const left = previous[(column + columns - 1) % columns];
            const center = previous[column];
            const right = previous[(column + 1) % columns];
            const neighborhood = (left << 2) | (center << 1) | right;
            next[column] = (30 >> neighborhood) & 1;
        }
        rows.push(next);
        generation++;
        if (rows.length > maxRows) rows.shift();
    }

    function draw() {
        ctx.clearRect(0, 0, width, height);
        const stepX = 6;
        const stepY = 7.4;
        const xOffset = (width - columns * stepX) / 2;
        const yOffset = 36;
        rows.forEach((row, index) => {
            for (let column = 0; column < columns; column++) {
                if (!row[column]) continue;
                const age = index / Math.max(1, rows.length - 1);
                ctx.fillStyle = age > .93 ? '#f0ffc2' : age > .65 ? '#e1ff56' : age > .3 ? '#b6d247' : '#728530';
                ctx.fillRect(xOffset + column * stepX, yOffset + index * stepY, 4.8, 5.8);
            }
        });
        generationLabel.textContent = String(generation).padStart(3, '0');
    }

    function seed() {
        rows = [new Uint8Array(columns)];
        const middle = Math.floor(columns / 2);
        rows[0][middle] = 1;
        if (seedVersion > 0) {
            for (let column = middle - 8; column <= middle + 8; column++) {
                if (Math.random() > .65) rows[0][column] = 1;
            }
        }
        generation = 0;
        for (let i = 0; i < 48; i++) advance();
        draw();
        seedVersion++;
    }

    function updateTimer() {
        if (timer !== null) {
            window.clearInterval(timer);
            timer = null;
        }
        if (paused || !inView || document.hidden) return;
        timer = window.setInterval(() => {
            advance();
            draw();
        }, 200);
    }

    function updatePause() {
        pauseButton.textContent = paused ? 'Play' : 'Pause';
        pauseButton.setAttribute('aria-pressed', String(paused));
        pauseButton.setAttribute('aria-label', paused ? 'Play cellular automaton' : 'Pause cellular automaton');
        updateTimer();
    }

    pauseButton.addEventListener('click', () => {
        paused = !paused;
        updatePause();
    });
    resetButton.addEventListener('click', seed);
    reducedMotion.addEventListener('change', event => {
        paused = event.matches;
        updatePause();
    });
    document.addEventListener('visibilitychange', updateTimer);
    if ('IntersectionObserver' in window) {
        new IntersectionObserver(entries => {
            inView = entries[0].isIntersecting;
            updateTimer();
        }, { threshold: .05 }).observe(canvas);
    }
    window.addEventListener('pagehide', () => {
        if (timer !== null) window.clearInterval(timer);
    });
    window.addEventListener('pageshow', updateTimer);
    seed();
    updatePause();
})();
