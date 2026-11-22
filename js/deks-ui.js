/* Deks Nexa — apparition douce des blocs au défilement (toutes les pages).
   Les blocs sont visibles par défaut : l'animation ne s'applique que si
   <html> porte la classe « js » (ajoutée dans le <head>). Ce script
   ajoute « dn-ready » ; sans lui, une sécurité CSS affiche tout. */
(function () {
    "use strict";

    var root = document.documentElement;
    var items = Array.prototype.slice.call(document.querySelectorAll(".dn-reveal"));
    var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

    var showAll = function () {
        items.forEach(function (el) {
            el.classList.add("is-visible");
        });
    };

    root.classList.add("dn-ready");

    if (!items.length) {
        return;
    }

    if (reduceMotion || !("IntersectionObserver" in window)) {
        showAll();
        return;
    }

    // Petit décalage en cascade entre les éléments d'une même liste.
    items.forEach(function (el) {
        var parent = el.parentElement;
        var siblings = parent ? Array.prototype.filter.call(parent.children, function (child) {
            return child.classList.contains("dn-reveal");
        }) : [el];
        el.style.setProperty("--rd", Math.min(siblings.indexOf(el), 5) * 80 + "ms");
    });

    var observer = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
            if (entry.isIntersecting) {
                entry.target.classList.add("is-visible");
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1, rootMargin: "0px 0px -10% 0px" });

    items.forEach(function (el) {
        observer.observe(el);
    });

    // Impression : tout doit être visible.
    window.addEventListener("beforeprint", showAll);
})();
