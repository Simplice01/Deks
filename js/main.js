(function ($) {
    "use strict";

    // Spinner
    var spinner = function () {
        setTimeout(function () {
            if ($('#spinner').length > 0) {
                $('#spinner').removeClass('show');
            }
        }, 1);
    };
    spinner();

    // Initiate the wowjs
    new WOW().init();

    const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

    if (!document.querySelector(".deks-reading-progress")) {
        document.body.insertAdjacentHTML("afterbegin", '<div class="deks-reading-progress" aria-hidden="true"><span></span></div>');
    }

    const updateReadingProgress = function () {
        const progressBar = document.querySelector(".deks-reading-progress span");
        if (!progressBar) {
            return;
        }

        const scrollable = document.documentElement.scrollHeight - window.innerHeight;
        const progress = scrollable > 0 ? Math.min(window.scrollY / scrollable, 1) : 0;
        progressBar.style.transform = `scaleX(${progress})`;
    };

    // Sticky Navbar
    const updateNavbarState = function () {
        if ($(window).scrollTop() > 45) {
            $('.navbar').addClass('sticky-top shadow-sm deks-nav-compact');
        } else {
            $('.navbar').removeClass('sticky-top shadow-sm deks-nav-compact');
        }

        updateReadingProgress();
    };

    updateNavbarState();
    $(window).scroll(updateNavbarState);

    // Dropdown on mouse hover
    const $dropdown = $(".dropdown");
    const $dropdownToggle = $(".dropdown-toggle");
    const $dropdownMenu = $(".dropdown-menu");
    const showClass = "show";

    $(window).on("load resize", function() {
        if (this.matchMedia("(min-width: 992px)").matches) {
            $dropdown.hover(
                function() {
                    const $this = $(this);
                    $this.addClass(showClass);
                    $this.find($dropdownToggle).attr("aria-expanded", "true");
                    $this.find($dropdownMenu).addClass(showClass);
                },
                function() {
                    const $this = $(this);
                    $this.removeClass(showClass);
                    $this.find($dropdownToggle).attr("aria-expanded", "false");
                    $this.find($dropdownMenu).removeClass(showClass);
                }
            );
        } else {
            $dropdown.off("mouseenter mouseleave");
        }
    });

    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 100) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
        return false;
    });

    // Testimonials carousel
    $(".testimonial-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1000,
        margin: 25,
        dots: false,
        loop: true,
        center: true,
        responsive: {
            0: {
                items: 1
            },
            576: {
                items: 1
            },
            768: {
                items: 2
            },
            992: {
                items: 3
            }
        }
    });

    // Back-office ready placeholders: replace these arrays with API data when available.
    const deksStats = [
        { group: "clients", value: 15, suffix: "+", label: "clients accompagnés" },
        { group: "clients", value: 10, suffix: "+", label: "entreprises accompagnées" },
        { key: "projectsTotal", group: "projects", value: 35, suffix: "+", label: "projets réalisés" },
        { group: "projects", value: 14, suffix: "+", label: "plateformes publiques déployées" },
        { group: "quality", value: 96, suffix: "%", label: "taux de satisfaction estimé" },
        { group: "quality", value: 5, suffix: " ans", label: "d'expérience depuis 2021" }
    ];

    const deksTestimonials = [
        {
            company: "Entreprise Alpha",
            person: "Nadine A.",
            role: "Responsable opérations",
            comment: "DEKS nous a aidés à clarifier notre besoin et à transformer un processus manuel en outil simple à utiliser au quotidien.",
            rating: 5
        },
        {
            company: "Groupe Horizon",
            person: "Marcel K.",
            role: "Directeur administratif",
            comment: "L'équipe a travaillé avec méthode. Le suivi était clair et la solution livrée répond aux usages réels de nos équipes.",
            rating: 5
        },
        {
            company: "Plateforme Services Pro",
            person: "Aïcha T.",
            role: "Fondatrice",
            comment: "Nous avions besoin d'une plateforme fiable pour gérer nos utilisateurs et nos demandes. DEKS a su structurer le projet.",
            rating: 5
        }
    ];

    const escapeHTML = function (value) {
        return String(value).replace(/[&<>"']/g, function (char) {
            return {
                "&": "&amp;",
                "<": "&lt;",
                ">": "&gt;",
                '"': "&quot;",
                "'": "&#039;"
            }[char];
        });
    };

    const formatStatValue = function (stat) {
        return `${stat.value}${stat.suffix || ""}`;
    };

    const renderStatsGroup = function (targetId, groupName) {
        const target = document.getElementById(targetId);
        if (!target) {
            return;
        }

        target.innerHTML = deksStats.filter(function (stat) {
            return stat.group === groupName;
        }).map(function (stat) {
            return `
                <article class="deks-stat-card">
                    <strong data-count-to="${escapeHTML(stat.value)}" data-count-suffix="${escapeHTML(stat.suffix || "")}">0${escapeHTML(stat.suffix || "")}</strong>
                    <span>${escapeHTML(stat.label)}</span>
                </article>
            `;
        }).join("");
    };

    renderStatsGroup("deksClientStatsGrid", "clients");
    renderStatsGroup("deksProjectStatsGrid", "projects");
    renderStatsGroup("deksQualityStatsGrid", "quality");

    document.querySelectorAll("[data-deks-stat-ref]").forEach(function (element) {
        const stat = deksStats.find(function (item) {
            return item.key === element.dataset.deksStatRef;
        });

        if (stat) {
            element.textContent = `${formatStatValue(stat)} ${stat.label}`;
        }
    });

    const testimonialsGrid = document.getElementById("deksTestimonialsGrid");
    if (testimonialsGrid) {
        testimonialsGrid.innerHTML = deksTestimonials.map(function (item) {
            const initials = item.company.split(" ").map(function (word) {
                return word.charAt(0);
            }).join("").slice(0, 2);
            const stars = "★".repeat(Math.max(1, Math.min(Number(item.rating) || 5, 5)));

            return `
                <article class="deks-testimonial-card">
                    <div class="deks-testimonial-top">
                        <div class="deks-client-logo" aria-hidden="true">${escapeHTML(initials)}</div>
                        <div>
                            <strong>${escapeHTML(item.company)}</strong>
                            <span>${escapeHTML(stars)}</span>
                        </div>
                    </div>
                    <p>“${escapeHTML(item.comment)}”</p>
                    <footer>
                        <strong>${escapeHTML(item.person)}</strong>
                        <span>${escapeHTML(item.role)}</span>
                    </footer>
                </article>
            `;
        }).join("");
    }

    const revealElements = function () {
        const selectors = [
            ".deks-home-about",
            ".deks-process-cta",
            ".services-section",
            ".deks-proof-section",
            ".deks-testimonials-section",
            ".deks-method-section",
            ".deks-page-hero",
            "body > .container-xxl > .container-xxl.py-5:not(.hero-header)",
            "#actualites",
            ".footer",
            ".service-card",
            ".deks-proof-group",
            ".deks-testimonial-card",
            "#actualites .card",
            ".deks-value-panel > div",
            ".deks-process-item",
            ".experience-left",
            ".experience-right"
        ];

        document.querySelectorAll(selectors.join(",")).forEach(function (element, index) {
            element.classList.add("deks-reveal");
            element.style.setProperty("--deks-reveal-delay", `${Math.min(index % 6, 5) * 55}ms`);
        });

        if (reducedMotion || !("IntersectionObserver" in window)) {
            document.querySelectorAll(".deks-reveal").forEach(function (element) {
                element.classList.add("is-visible");
            });
            return;
        }

        const observer = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    entry.target.classList.add("is-visible");
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.12, rootMargin: "0px 0px -8% 0px" });

        document.querySelectorAll(".deks-reveal").forEach(function (element) {
            observer.observe(element);
        });
    };

    const animateCounters = function () {
        const counters = document.querySelectorAll("[data-count-to]");

        if (!counters.length) {
            return;
        }

        const setCounterValue = function (counter, value) {
            counter.textContent = `${value}${counter.dataset.countSuffix || ""}`;
        };

        if (reducedMotion || !("IntersectionObserver" in window)) {
            counters.forEach(function (counter) {
                setCounterValue(counter, counter.dataset.countTo);
            });
            return;
        }

        const countObserver = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (!entry.isIntersecting) {
                    return;
                }

                const counter = entry.target;
                const target = Number(counter.dataset.countTo) || 0;
                const duration = 850;
                const start = performance.now();

                const tick = function (now) {
                    const progress = Math.min((now - start) / duration, 1);
                    const eased = 1 - Math.pow(1 - progress, 3);
                    setCounterValue(counter, Math.round(target * eased));

                    if (progress < 1) {
                        requestAnimationFrame(tick);
                    } else {
                        setCounterValue(counter, target);
                    }
                };

                requestAnimationFrame(tick);
                countObserver.unobserve(counter);
            });
        }, { threshold: 0.55 });

        counters.forEach(function (counter) {
            countObserver.observe(counter);
        });
    };

    const updateActiveNav = function () {
        const navLinks = Array.from(document.querySelectorAll(".navbar-nav .nav-link"));
        const homeLink = navLinks.find(function (link) { return link.getAttribute("href") === "index.html"; });
        const aboutLink = navLinks.find(function (link) { return link.getAttribute("href") === "about.html"; });
        const solutionsLink = navLinks.find(function (link) { return link.getAttribute("href") === "service.html"; });
        const path = window.location.pathname.split("/").pop() || "index.html";

        navLinks.forEach(function (link) {
            link.classList.remove("active");
        });

        if (path === "about.html") {
            aboutLink && aboutLink.classList.add("active");
            return;
        }

        if (path === "service.html") {
            solutionsLink && solutionsLink.classList.add("active");
            return;
        }

        if (path !== "index.html") {
            homeLink && homeLink.classList.add("active");
            return;
        }

        const sections = [
            { el: document.querySelector(".hero-header"), link: homeLink },
            { el: document.querySelector(".deks-home-about"), link: aboutLink },
            { el: document.querySelector(".services-section"), link: solutionsLink },
            { el: document.querySelector("#actualites"), link: solutionsLink }
        ].filter(function (item) { return item.el && item.link; });

        const setActiveFromScroll = function () {
            let active = homeLink;
            const marker = window.innerHeight * 0.38;

            sections.forEach(function (item) {
                const rect = item.el.getBoundingClientRect();
                if (rect.top <= marker && rect.bottom >= marker) {
                    active = item.link;
                }
            });

            navLinks.forEach(function (link) { link.classList.remove("active"); });
            active && active.classList.add("active");
        };

        setActiveFromScroll();
        window.addEventListener("scroll", setActiveFromScroll, { passive: true });
    };

    revealElements();
    animateCounters();
    updateActiveNav();

    document.querySelectorAll(".navbar-nav .nav-link, .deks-nav-cta").forEach(function (link) {
        link.addEventListener("click", function () {
            const navbarCollapse = document.getElementById("navbarCollapse");
            if (navbarCollapse && navbarCollapse.classList.contains("show") && window.bootstrap) {
                window.bootstrap.Collapse.getOrCreateInstance(navbarCollapse).hide();
            }
        });
    });

    const mobileToggle = document.querySelector(".deks-mobile-toggle");
    const navbarCollapse = document.getElementById("navbarCollapse");
    if (mobileToggle && navbarCollapse && window.bootstrap) {
        mobileToggle.addEventListener("click", function (event) {
            event.preventDefault();
            event.stopPropagation();
            window.bootstrap.Collapse.getOrCreateInstance(navbarCollapse).toggle();
        }, true);
    }

    document.addEventListener("keydown", function (event) {
        if (event.key !== "Escape") {
            return;
        }

        const navbarCollapse = document.getElementById("navbarCollapse");
        if (navbarCollapse && navbarCollapse.classList.contains("show") && window.bootstrap) {
            window.bootstrap.Collapse.getOrCreateInstance(navbarCollapse).hide();
        }

        const serviceModal = document.getElementById("serviceModal");
        if (serviceModal && serviceModal.style.display === "flex") {
            closeModal();
        }
    });

    const serviceModal = document.getElementById("serviceModal");
    if (serviceModal) {
        serviceModal.addEventListener("click", function (event) {
            if (event.target === serviceModal) {
                closeModal();
            }
        });
    }

    const initDeksChatbot = function () {
        if (document.querySelector(".deks-chatbot")) {
            return;
        }

        const whatsappNumber = "2290194776256";
        const whatsappText = "Bonjour DEKS, je viens du chatbot de votre site. J'ai une question concernant mon projet.";
        const whatsappUrl = `https://wa.me/${whatsappNumber}?text=${encodeURIComponent(whatsappText)}`;
        const suggestions = [
            "Quels logiciels développez-vous ?",
            "Comment se déroule un projet ?",
            "Pourquoi choisir DEKS ?",
            "Je veux demander un devis"
        ];
        const answers = [
            {
                keys: ["logiciel", "application", "erp", "crm", "saas", "dashboard", "plateforme", "api", "automatisation", "outil"],
                text: "DEKS conçoit des logiciels professionnels pour les entreprises : applications métiers, ERP, CRM, plateformes SaaS, dashboards, APIs et automatisations de processus."
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
                text: "DEKS privilégie les solutions utiles, durables et adaptées aux opérations réelles. L'objectif est de livrer un outil clair, maintenable et capable d'évoluer avec votre entreprise."
            },
            {
                keys: ["maintenance", "ameliorer", "améliorer", "evolution", "évolution", "support", "corriger"],
                text: "Oui. DEKS peut maintenir, améliorer et faire évoluer une application existante afin de la rendre plus stable, plus claire et mieux adaptée à vos usages actuels."
            },
            {
                keys: ["technologie", "django", "laravel", "flask", "next", "postgresql", "mysql", "n8n"],
                text: "Nous utilisons des technologies fiables selon le besoin du projet, mais le plus important reste la solution livrée : stabilité, sécurité, facilité d'utilisation et évolutivité."
            }
        ];
        const humanTriggers = ["conseiller", "humain", "personne", "whatsapp", "appel", "devis", "prix", "budget", "rendez-vous", "rdv", "personnalise", "personnalisé", "complexe"];
        let uncertainCount = 0;
        let conversationStarted = false;
        let submitMessage;

        const normalize = function (value) {
            return value.toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g, "");
        };

        const buildFallback = function () {
            return {
                text: "Je préfère vous orienter vers le support DEKS pour une réponse plus précise. Cliquez sur le bouton WhatsApp ci-dessous pour continuer la discussion avec un conseiller.",
                whatsapp: true
            };
        };

        const getAnswer = function (message) {
            const clean = normalize(message);

            if (humanTriggers.some(function (word) { return clean.includes(normalize(word)); })) {
                return buildFallback();
            }

            let best = { score: 0, answer: null };
            answers.forEach(function (answer) {
                const score = answer.keys.reduce(function (total, key) {
                    return total + (clean.includes(normalize(key)) ? 1 : 0);
                }, 0);

                if (score > best.score) {
                    best = { score: score, answer: answer };
                }
            });

            if (best.answer && best.score > 0) {
                uncertainCount = 0;
                return { text: best.answer.text };
            }

            return buildFallback();
        };

        const addMessage = function (container, text, type, options) {
            const message = document.createElement("div");
            message.className = `deks-chat-message deks-chat-message-${type}`;
            const paragraph = document.createElement("p");
            paragraph.textContent = text;
            message.appendChild(paragraph);

            if (options && options.whatsapp) {
                const link = document.createElement("a");
                link.className = "deks-chat-whatsapp";
                link.href = whatsappUrl;
                link.target = "_blank";
                link.rel = "noopener";
                link.textContent = "Continuer sur WhatsApp";
                message.appendChild(link);
            }

            if (options && options.suggestions) {
                const list = document.createElement("div");
                list.className = "deks-chat-suggestions";
                suggestions.forEach(function (item) {
                    const button = document.createElement("button");
                    button.type = "button";
                    button.textContent = item;
                    button.addEventListener("click", function () {
                        submitMessage(item);
                    });
                    list.appendChild(button);
                });
                message.appendChild(list);
            }

            container.appendChild(message);
            container.scrollTop = container.scrollHeight;
        };

        const removeSuggestions = function () {
            messages.querySelectorAll(".deks-chat-suggestions").forEach(function (element) {
                element.remove();
            });
        };

        const chatbot = document.createElement("section");
        chatbot.className = "deks-chatbot";
        chatbot.setAttribute("aria-label", "Assistant DEKS");
        chatbot.innerHTML = `
            <button class="deks-chatbot-toggle" type="button" aria-expanded="false" aria-controls="deksChatbotPanel">
                <i class="fa fa-comment" aria-hidden="true"></i>
                <span>Assistant</span>
            </button>
            <div class="deks-chatbot-panel" id="deksChatbotPanel" hidden>
                <div class="deks-chatbot-header">
                    <div>
                        <strong>Assistant DEKS</strong>
                        <span>Réponse rapide</span>
                    </div>
                    <button class="deks-chatbot-close" type="button" aria-label="Fermer le chatbot">&times;</button>
                </div>
                <div class="deks-chatbot-messages" role="log" aria-live="polite"></div>
                <form class="deks-chatbot-form">
                    <input type="text" aria-label="Votre question" placeholder="Posez votre question..." autocomplete="off">
                    <button type="submit">Envoyer</button>
                </form>
            </div>
        `;
        document.body.appendChild(chatbot);

        const toggle = chatbot.querySelector(".deks-chatbot-toggle");
        const panel = chatbot.querySelector(".deks-chatbot-panel");
        const close = chatbot.querySelector(".deks-chatbot-close");
        const messages = chatbot.querySelector(".deks-chatbot-messages");
        const form = chatbot.querySelector(".deks-chatbot-form");
        const input = chatbot.querySelector("input");

        submitMessage = function (value) {
            const message = String(value || input.value || "").trim();
            if (!message) {
                return;
            }

            if (!conversationStarted) {
                conversationStarted = true;
                removeSuggestions();
            }

            addMessage(messages, message, "user");
            input.value = "";
            const answer = getAnswer(message);
            window.setTimeout(function () {
                addMessage(messages, answer.text, "bot", answer);
            }, reducedMotion ? 0 : 180);
        };

        const openChat = function () {
            panel.hidden = false;
            toggle.setAttribute("aria-expanded", "true");
            window.setTimeout(function () {
                input.focus();
            }, 60);
        };

        const closeChat = function () {
            panel.hidden = true;
            toggle.setAttribute("aria-expanded", "false");
        };

        toggle.addEventListener("click", function () {
            panel.hidden ? openChat() : closeChat();
        });
        close.addEventListener("click", closeChat);
        form.addEventListener("submit", function (event) {
            event.preventDefault();
            submitMessage();
        });

        addMessage(messages, "Bonjour, je peux vous orienter sur les solutions DEKS, notre méthode ou le démarrage d'un projet.", "bot", { suggestions: true });
    };

    initDeksChatbot();

    // Portfolio isotope and filter
    var portfolioIsotope = $('.portfolio-container').isotope({
        itemSelector: '.portfolio-item',
        layoutMode: 'fitRows'
    });
    $('#portfolio-flters li').on('click', function () {
        $("#portfolio-flters li").removeClass('active');
        $(this).addClass('active');

        portfolioIsotope.isotope({filter: $(this).data('filter')});
    });
})(jQuery);

function toggleDetails(button) {
    const content = button.closest('.service').querySelector('.service-content');
    const isVisible = content.style.display === 'block';
    content.style.display = isVisible ? 'none' : 'block';
    button.textContent = isVisible ? '▼' : '▲';
}

function openModal(service) {
    const details = {
        web: `
            <h3>Applications métiers</h3>
            <p>Nous concevons des outils internes adaptés à vos processus : suivi, validation, gestion d'activité et tableaux de bord.</p>
            <ul>
                <li>Gestion des demandes et validations</li>
                <li>Espaces utilisateurs sécurisés</li>
                <li>Tableaux de bord opérationnels</li>
                <li>Traçabilité des actions</li>
                <li>Évolutions selon vos besoins métier</li>
            </ul>
        `,
        mobile: `
            <h3>Applications mobiles métier</h3>
            <p>Nous créons des applications mobiles utiles aux équipes terrain, connectées aux données de l'entreprise.</p>
            <ul>
                <li>Collecte de données sur le terrain</li>
                <li>Notifications et alertes métier</li>
                <li>Synchronisation avec le système central</li>
                <li>Accès sécurisé par profil utilisateur</li>
                <li>Expérience simple pour les équipes</li>
            </ul>
        `,
        software: `
            <h3>ERP & CRM</h3>
            <p>Nous structurons vos données clients, ventes, stocks et finances dans un outil clair et exploitable.</p>
            <ul>
                <li>Gestion clients et prospects</li>
                <li>Suivi commercial et facturation</li>
                <li>Gestion de stock et opérations</li>
                <li>Rapports et indicateurs clés</li>
                <li>Maintenance et amélioration continue</li>
            </ul>
        `,
        saas: `
            <h3>Plateformes SaaS</h3>
            <p>Nous développons des plateformes en ligne prêtes à accueillir des utilisateurs, des abonnements et des processus métier.</p>
            <ul>
                <li>Comptes et rôles utilisateurs</li>
                <li>Espaces clients et administration</li>
                <li>Abonnements ou paiements intégrés</li>
                <li>Suivi des usages et indicateurs</li>
                <li>Architecture pensée pour évoluer</li>
            </ul>
        `,
        automation: `
            <h3>Automatisation des processus</h3>
            <p>Nous réduisons les tâches répétitives en connectant les étapes clés de votre activité.</p>
            <ul>
                <li>Relances automatiques</li>
                <li>Notifications internes</li>
                <li>Validation et affectation des demandes</li>
                <li>Génération de documents ou factures</li>
                <li>Suivi des actions en temps réel</li>
            </ul>
        `,
        api: `
            <h3>Intégrations API</h3>
            <p>Nous connectons vos outils pour que les données circulent entre vos logiciels sans ressaisie manuelle.</p>
            <ul>
                <li>Connexion aux solutions de paiement</li>
                <li>Synchronisation entre applications</li>
                <li>APIs REST pour vos services</li>
                <li>Automatisation des échanges de données</li>
                <li>Supervision et maintenance des intégrations</li>
            </ul>
        `
    };

    document.getElementById('modalDetails').innerHTML = details[service];
    document.getElementById('serviceModal').style.display = 'flex';
}

function closeModal() {
    document.getElementById('serviceModal').style.display = 'none';
}
