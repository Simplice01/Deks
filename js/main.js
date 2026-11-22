/* Deks Nexa — navigation, retour en haut, barre de lecture et assistant.
   JavaScript natif, sans bibliothèque (plus de jQuery ni de Bootstrap). */
(function () {
    "use strict";

    var root = document.documentElement;
    var reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

    /* --- Barre de lecture --- */
    var progress = document.createElement("div");
    progress.className = "deks-reading-progress";
    progress.setAttribute("aria-hidden", "true");
    progress.appendChild(document.createElement("span"));
    document.body.insertBefore(progress, document.body.firstChild);
    var progressBar = progress.firstChild;

    var nav = document.querySelector(".dn-nav");
    var topButton = document.querySelector(".dn-top");

    /* --- Lien actif de la page d'accueil selon la section visible --- */
    var navLinks = Array.prototype.slice.call(document.querySelectorAll(".dn-nav-link"));
    var findLink = function (href) {
        return navLinks.filter(function (link) {
            return link.getAttribute("href") === href;
        })[0];
    };
    var homeLink = findLink("index.html");
    var solutionsLink = findLink("service.html");
    var solutionsSection = document.querySelector(".dn-hero") ? document.getElementById("solutions") : null;

    var updateActive = function () {
        if (!solutionsSection || !homeLink || !solutionsLink) {
            return;
        }
        var marker = window.innerHeight * 0.38;
        var rect = solutionsSection.getBoundingClientRect();
        var inSolutions = rect.top <= marker && rect.bottom >= marker;
        homeLink.classList.toggle("is-active", !inSolutions);
        solutionsLink.classList.toggle("is-active", inSolutions);
    };

    /* --- Défilement : bordure de la barre, bouton retour, progression --- */
    var ticking = false;
    var onScroll = function () {
        if (ticking) {
            return;
        }
        ticking = true;
        window.requestAnimationFrame(function () {
            ticking = false;
            var y = window.pageYOffset || root.scrollTop;
            var max = root.scrollHeight - window.innerHeight;

            if (nav) {
                nav.classList.toggle("is-scrolled", y > 8);
            }
            if (topButton) {
                topButton.classList.toggle("is-shown", y > 800);
            }
            progressBar.style.transform = "scaleX(" + (max > 0 ? Math.min(y / max, 1) : 0) + ")";
            updateActive();
        });
    };

    window.addEventListener("scroll", onScroll, { passive: true });
    window.addEventListener("resize", onScroll);
    onScroll();

    if (topButton) {
        topButton.addEventListener("click", function (event) {
            event.preventDefault();
            window.scrollTo({ top: 0, behavior: reducedMotion ? "auto" : "smooth" });
            var brand = document.querySelector(".dn-nav-brand");
            if (brand) {
                brand.focus({ preventScroll: true });
            }
        });
    }

    /* --- Menu mobile plein écran --- */
    var menuButton = document.querySelector(".dn-menu-btn");
    var menu = document.getElementById("dn-menu");
    var desktop = window.matchMedia("(min-width: 992px)");
    var outside = Array.prototype.slice.call(document.querySelectorAll("main, footer, .dn-top"));

    var isOpen = function () {
        return root.classList.contains("dn-menu-open");
    };

    var setMenu = function (open) {
        if (!menuButton || !menu) {
            return;
        }
        root.classList.toggle("dn-menu-open", open);
        menuButton.setAttribute("aria-expanded", String(open));
        menuButton.setAttribute("aria-label", open ? "Fermer le menu" : "Ouvrir le menu");
        outside.forEach(function (el) {
            if (open) {
                el.setAttribute("inert", "");
            } else {
                el.removeAttribute("inert");
            }
        });
        var chatbot = document.querySelector(".deks-chatbot");
        if (chatbot) {
            chatbot.hidden = open;
        }
        if (open) {
            var first = menu.querySelector("a");
            if (first) {
                window.setTimeout(function () {
                    first.focus();
                }, 50);
            }
        }
    };

    if (menuButton && menu) {
        menuButton.addEventListener("click", function () {
            setMenu(!isOpen());
        });

        menu.addEventListener("click", function (event) {
            if (event.target.closest("a") && isOpen()) {
                setMenu(false);
            }
        });

        document.addEventListener("keydown", function (event) {
            if (!isOpen()) {
                return;
            }
            if (event.key === "Escape") {
                setMenu(false);
                menuButton.focus();
                return;
            }
            if (event.key !== "Tab") {
                return;
            }
            // Garde le focus dans le menu ouvert (bouton + liens).
            var focusables = [menuButton].concat(Array.prototype.slice.call(menu.querySelectorAll("a")));
            var firstEl = focusables[0];
            var lastEl = focusables[focusables.length - 1];
            if (event.shiftKey && document.activeElement === firstEl) {
                event.preventDefault();
                lastEl.focus();
            } else if (!event.shiftKey && document.activeElement === lastEl) {
                event.preventDefault();
                firstEl.focus();
            }
        });

        var onDesktop = function (event) {
            if (event.matches && isOpen()) {
                setMenu(false);
            }
        };
        if (desktop.addEventListener) {
            desktop.addEventListener("change", onDesktop);
        } else if (desktop.addListener) {
            desktop.addListener(onDesktop);
        }
    }

    /* --- Assistant --- */
    var svg = function (path, filled) {
        return '<svg viewBox="0 0 24 24" fill="' + (filled ? "currentColor" : "none") + '" stroke="' + (filled ? "none" : "currentColor") + '" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="' + path + '"/></svg>';
    };

    var initDeksChatbot = function () {
        if (document.querySelector(".deks-chatbot")) {
            return;
        }

        var whatsappNumber = "2290194776256";
        var whatsappText = "Bonjour Deks Nexa, je viens du chatbot de votre site. J'ai une question concernant mon projet.";
        var whatsappUrl = "https://wa.me/" + whatsappNumber + "?text=" + encodeURIComponent(whatsappText);
        var suggestions = [
            "Quels logiciels développez-vous ?",
            "Comment se déroule un projet ?",
            "Pourquoi choisir Deks Nexa ?",
            "Je veux demander un devis"
        ];
        var answers = [
            {
                keys: ["logiciel", "application", "erp", "crm", "saas", "dashboard", "plateforme", "api", "automatisation", "outil"],
                text: "Deks Nexa conçoit des logiciels professionnels pour les entreprises : applications métiers, ERP, CRM, plateformes SaaS, dashboards, APIs et automatisations de processus."
            },
            {
                keys: ["probleme", "problème", "besoin", "processus", "manuel", "erreur", "lent", "suivi", "collaboration", "centraliser"],
                text: "Nous aidons les entreprises à transformer leurs processus dispersés en outils fiables : moins de ressaisie, plus de visibilité, des validations plus claires et une meilleure collaboration."
            },
            {
                keys: ["methode", "méthode", "etape", "étape", "deroule", "déroule", "projet", "travail", "livraison"],
                text: "Un projet commence par la clarification du besoin, puis nous définissons le périmètre, concevons la solution, développons par étapes et accompagnons la mise en service."
            },
            {
                keys: ["pourquoi", "choisir", "confiance", "expertise", "serieux", "sérieux", "qualite", "qualité"],
                text: "Deks Nexa privilégie les solutions utiles, durables et adaptées aux opérations réelles. L'objectif est de livrer un outil clair, maintenable et capable d'évoluer avec votre entreprise."
            },
            {
                keys: ["maintenance", "ameliorer", "améliorer", "evolution", "évolution", "support", "corriger"],
                text: "Oui. Deks Nexa peut maintenir, améliorer et faire évoluer une application existante afin de la rendre plus stable, plus claire et mieux adaptée à vos usages actuels."
            },
            {
                keys: ["technologie", "django", "laravel", "flask", "next", "postgresql", "mysql", "n8n"],
                text: "Nous utilisons des technologies fiables selon le besoin du projet, mais le plus important reste la solution livrée : stabilité, sécurité, facilité d'utilisation et évolutivité."
            }
        ];
        var humanTriggers = ["conseiller", "humain", "personne", "whatsapp", "appel", "devis", "prix", "budget", "rendez-vous", "rdv", "personnalise", "personnalisé", "complexe"];
        var conversationStarted = false;

        var normalize = function (value) {
            return value.toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "");
        };

        var buildFallback = function () {
            return {
                text: "Je préfère vous orienter vers le support Deks Nexa pour une réponse plus précise. Cliquez sur le bouton WhatsApp ci-dessous pour continuer la discussion avec un conseiller.",
                whatsapp: true
            };
        };

        var getAnswer = function (message) {
            var clean = normalize(message);

            if (humanTriggers.some(function (word) { return clean.indexOf(normalize(word)) !== -1; })) {
                return buildFallback();
            }

            var best = { score: 0, answer: null };
            answers.forEach(function (answer) {
                var score = answer.keys.reduce(function (total, key) {
                    return total + (clean.indexOf(normalize(key)) !== -1 ? 1 : 0);
                }, 0);
                if (score > best.score) {
                    best = { score: score, answer: answer };
                }
            });

            if (best.answer && best.score > 0) {
                return { text: best.answer.text };
            }

            return buildFallback();
        };

        var chatbot = document.createElement("section");
        chatbot.className = "deks-chatbot";
        chatbot.setAttribute("aria-label", "Assistant Deks Nexa");
        chatbot.innerHTML =
            '<button class="deks-chatbot-toggle" type="button" aria-expanded="false" aria-controls="deksChatbotPanel">' +
                svg("M21 11.5a8.4 8.4 0 0 1-9 8.4 9 9 0 0 1-3.9-.9L3 20l1.1-4.4A8 8 0 0 1 3 11.5 8.4 8.4 0 0 1 12 3a8.4 8.4 0 0 1 9 8.5z") +
                "<span>Assistant</span>" +
            "</button>" +
            '<div class="deks-chatbot-panel" id="deksChatbotPanel" hidden>' +
                '<div class="deks-chatbot-header">' +
                    "<div><strong>Assistant Deks Nexa</strong><span>Réponse rapide</span></div>" +
                    '<button class="deks-chatbot-close" type="button" aria-label="Fermer le chatbot">' + svg("M6 6l12 12M18 6L6 18") + "</button>" +
                "</div>" +
                '<div class="deks-chatbot-messages" role="log" aria-live="polite"></div>' +
                '<form class="deks-chatbot-form">' +
                    '<input type="text" aria-label="Votre question" placeholder="Posez votre question..." autocomplete="off">' +
                    '<button type="submit">Envoyer</button>' +
                "</form>" +
            "</div>";
        document.body.appendChild(chatbot);

        var toggle = chatbot.querySelector(".deks-chatbot-toggle");
        var panel = chatbot.querySelector(".deks-chatbot-panel");
        var close = chatbot.querySelector(".deks-chatbot-close");
        var messages = chatbot.querySelector(".deks-chatbot-messages");
        var form = chatbot.querySelector(".deks-chatbot-form");
        var input = chatbot.querySelector("input");
        var submitMessage;

        var addMessage = function (text, type, options) {
            var message = document.createElement("div");
            message.className = "deks-chat-message deks-chat-message-" + type;
            var paragraph = document.createElement("p");
            paragraph.textContent = text;
            message.appendChild(paragraph);

            if (options && options.whatsapp) {
                var link = document.createElement("a");
                link.className = "deks-chat-whatsapp";
                link.href = whatsappUrl;
                link.target = "_blank";
                link.rel = "noopener";
                link.textContent = "Continuer sur WhatsApp";
                message.appendChild(link);
            }

            if (options && options.suggestions) {
                var list = document.createElement("div");
                list.className = "deks-chat-suggestions";
                suggestions.forEach(function (item) {
                    var button = document.createElement("button");
                    button.type = "button";
                    button.textContent = item;
                    button.addEventListener("click", function () {
                        submitMessage(item);
                    });
                    list.appendChild(button);
                });
                message.appendChild(list);
            }

            messages.appendChild(message);
            messages.scrollTop = messages.scrollHeight;
        };

        submitMessage = function (value) {
            var message = String(value || input.value || "").trim();
            if (!message) {
                return;
            }

            if (!conversationStarted) {
                conversationStarted = true;
                Array.prototype.forEach.call(messages.querySelectorAll(".deks-chat-suggestions"), function (element) {
                    element.parentNode.removeChild(element);
                });
            }

            addMessage(message, "user");
            input.value = "";
            var answer = getAnswer(message);
            window.setTimeout(function () {
                addMessage(answer.text, "bot", answer);
            }, reducedMotion ? 0 : 180);
        };

        var openChat = function () {
            panel.hidden = false;
            toggle.setAttribute("aria-expanded", "true");
            window.setTimeout(function () {
                input.focus();
            }, 60);
        };

        var closeChat = function () {
            panel.hidden = true;
            toggle.setAttribute("aria-expanded", "false");
        };

        toggle.addEventListener("click", function () {
            if (panel.hidden) {
                openChat();
            } else {
                closeChat();
            }
        });
        close.addEventListener("click", function () {
            closeChat();
            toggle.focus();
        });
        chatbot.addEventListener("keydown", function (event) {
            if (event.key === "Escape" && !panel.hidden) {
                closeChat();
                toggle.focus();
            }
        });
        form.addEventListener("submit", function (event) {
            event.preventDefault();
            submitMessage();
        });

        addMessage("Bonjour, je peux vous orienter sur les solutions Deks Nexa, notre méthode ou le démarrage d'un projet.", "bot", { suggestions: true });
    };

    initDeksChatbot();
})();
