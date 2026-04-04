function setTheme(theme) {
    document.documentElement.setAttribute("data-theme", theme);
    const themeToggle = document.getElementById("themeToggle");
    if (themeToggle) {
        themeToggle.textContent = theme === "light" ? "🌙" : "☀️";
    }
    localStorage.setItem("theme", theme);
}

function isInternalPage(href) {
    if (!href || href.startsWith("#") || href.startsWith("mailto:") || href.startsWith("tel:")) {
        return false;
    }
    try {
        const u = new URL(href, window.location.href);
        return u.origin === window.location.origin;
    } catch {
        return false;
    }
}

function initLinkPrefetch() {
    document.querySelectorAll("a[href]").forEach((a) => {
        const href = a.getAttribute("href");
        if (!isInternalPage(href)) return;
        a.addEventListener(
            "mouseenter",
            () => {
                const link = document.createElement("link");
                link.rel = "prefetch";
                link.href = href;
                document.head.appendChild(link);
            },
            { once: true, passive: true }
        );
    });
}

function initClassSelect() {
    const sel = document.getElementById("classSelect");
    if (!sel) return;
    sel.addEventListener("change", () => {
        if (sel.value) window.location.href = sel.value;
    });
}

function initMobileNav() {
    const header = document.querySelector(".header");
    const toggle = document.querySelector(".nav-toggle");
    const mq = window.matchMedia("(max-width: 900px)");
    if (!header || !toggle) return;

    function closeNav() {
        header.classList.remove("nav-open");
        toggle.setAttribute("aria-expanded", "false");
    }

    toggle.addEventListener("click", () => {
        const open = header.classList.toggle("nav-open");
        toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });

    document.querySelectorAll(".nav a").forEach((a) => {
        a.addEventListener("click", () => {
            if (mq.matches) closeNav();
        });
    });

    mq.addEventListener("change", (e) => {
        if (!e.matches) closeNav();
    });
}

window.addEventListener("DOMContentLoaded", () => {
    setTheme(localStorage.getItem("theme") || "light");

    const themeToggle = document.getElementById("themeToggle");
    themeToggle?.addEventListener("click", () => {
        const current = document.documentElement.getAttribute("data-theme");
        setTheme(current === "light" ? "dark" : "light");
    });

    initMobileNav();
    initClassSelect();
    initLinkPrefetch();
});
