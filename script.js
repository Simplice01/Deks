// .........Debut page
document.addEventListener('DOMContentLoaded', function () {
    const sectionIds = ['actualite', 'acceuil', 'services','avis', 'Contacts', 'fottter','experience']; 
  
    function fadeInSections() {
      sectionIds.forEach(function (sectionId) {
        const section = document.getElementById(sectionId);
  
        if (section) {
          const sectionTop = section.getBoundingClientRect().top;
          const windowHeight = window.innerHeight;
  
          if (sectionTop < windowHeight) {
            section.style.opacity = 1;
            section.style.transform = 'translateY(0)';
          }
        }
      });
    }
  

    fadeInSections();
  
  
    window.addEventListener('scroll', fadeInSections);
  });



//   .........Nav bar


// ...........Modale service



// document.addEventListener('DOMContentLoaded', function () {
//     const toggleButton = document.getElementById('toggle');
//     const menu = document.getElementById('menu');
  
//     toggleButton.addEventListener('click', function () {
//       menu.classList.toggle('active');
//       toggleButton.classList.toggle('active');
//     });
  

//     const menuLinks = document.querySelectorAll('.menu a');
//     menuLinks.forEach(function (link) {
//       link.addEventListener('click', function () {
//         menu.classList.remove('active');
//         toggleButton.classList.remove('active');
//       });
//     });
//   });
  
  




function toggleText1(){
    var text = document.getElementById("hiddenText1");
    text.style.display =(text.style.display==="none") ? "block" :"none";
}
function toggleText2(){
    var text = document.getElementById("hiddenText2");
    text.style.display =(text.style.display==="none") ? "block" :"none";
}
function toggleText3(){
    var text = document.getElementById("hiddenText3");
    text.style.display =(text.style.display==="none") ? "block" :"none";
}
function toggleText4(){
    var text = document.getElementById("hiddenText4");
    text.style.display =(text.style.display==="none") ? "block" :"none";
}
function toggleText5(){
    var text = document.getElementById("hiddenText5");
    text.style.display =(text.style.display==="none") ? "block" :"none";
}
function toggleText6(){
    var text = document.getElementById("hiddenText6");
    text.style.display =(text.style.display==="none") ? "block" :"none";
}





 

 document.addEventListener('DOMContentLoaded', function() {
  const carousel = document.getElementById('carousel5');
  const inner = carousel.querySelector('.carousel-inner');
  const items = carousel.querySelectorAll('.carousel-item');
  const totalItems = items.length;
  let currentIndex = 0;

  setInterval(function() {
      currentIndex = (currentIndex + 1) % totalItems;
      inner.style.transform = `translateX(-${currentIndex * 100}%)`;
  }, 60000);

  let touchStartX = 0;
  let touchEndX = 0;

  carousel.addEventListener('touchstart', function(event) {
      touchStartX = event.touches[0].clientX;
  });

  carousel.addEventListener('touchend', function(event) {
      touchEndX = event.changedTouches[0].clientX;
      handleSwipe();
  });

  function handleSwipe() {
      if (touchStartX - touchEndX > 50) {
          currentIndex = (currentIndex + 1) % totalItems;
          inner.style.transform = `translateX(-${currentIndex * 100}%)`;
      } else if (touchEndX - touchStartX > 50) {
          currentIndex = (currentIndex - 1 + totalItems) % totalItems;
          inner.style.transform = `translateX(-${currentIndex * 100}%)`;
      }
  }
});



//  document.addEventListener('DOMContentLoaded', function () {
//   const carousel = document.querySelector('.partie3');
//   const carouselItems = document.querySelectorAll('.carousel-item');
//   let currentIndex = 0;

//   function nextSlide() {
//       currentIndex = (currentIndex + 1) % carouselItems.length;
//       updateCarousel();
//   }

//   function updateCarousel() {
//       const newTransformValue = -currentIndex * 60 + '%';
//       carousel.style.transform = 'translateX(' + newTransformValue + ')';
//   }

//   setInterval(nextSlide, 5000);
// });

function toggleMenu() {
  const menu = document.querySelector('.menu');
  menu.classList.toggle('active');
}

const nombreEl = document.getElementById("nombre");
const nombreEl2 = document.getElementById("nombre2");
const nombreEl3 = document.getElementById("nombre3");
const nombreEl4 = document.getElementById("nombre4");

let nombre = 1;
let nombre2 = 1;
let nombre3 = 1;
let nombre4 = 1;

const interval = setInterval(() => {
    if (nombre > 36) {
        clearInterval(interval);
    } else {
        nombreEl.textContent = nombre;
        nombre++;
    }
}, 50);

const interval2 = setInterval(() => {
  if (nombre2 > 21) {
      clearInterval(interval2);
  } else {
      nombreEl2.textContent = nombre2;
      nombre2++;
  }
}, 50);
const interval3 = setInterval(() => {
  if (nombre3 > 60) {
      clearInterval(interval3);
  } else {
      nombreEl3.textContent = nombre3;
      nombre3++;
  }
}, 50);
const interval4 = setInterval(() => {
  if (nombre4 > 10) {
      clearInterval(interval4);
  } else {
      nombreEl4.textContent = nombre4;
      nombre4++;
  }
}, 50);

const slider = document.querySelector('.slider');

function activate(e) {
  const items = document.querySelectorAll('.item');
  e.target.matches('.next') && slider.append(items[0])
  e.target.matches('.prev') && slider.prepend(items[items.length-1]);
}

document.addEventListener('click',activate,false);




document.addEventListener('DOMContentLoaded', function() {
  const content = document.querySelector('.contentppp');
  const imageContainer = document.querySelector('.image-containerppp');

  // Animation de la transparence et de la translation
  content.style.opacity = '0';
  imageContainer.style.opacity = '0';
  content.style.transform = 'translateY(-50px)';
  imageContainer.style.transform = 'translateY(50px)';

  setTimeout(() => {
    content.style.transition = 'opacity 1s, transform 1s';
    imageContainer.style.transition = 'opacity 1s, transform 1s';
    content.style.opacity = '1';
    imageContainer.style.opacity = '1';
    content.style.transform = 'translateY(0)';
    imageContainer.style.transform = 'translateY(0)';
  }, 100);
});

document.addEventListener('DOMContentLoaded', function() {
  const content = document.querySelector('.contentppp');
  const imageContainer = document.querySelector('.image-containerppp');

  // Afficher les divs avec une transition après un court délai
  setTimeout(() => {
    content.style.opacity = '1';
    imageContainer.style.opacity = '1';
  }, 100);
});

document.addEventListener('DOMContentLoaded', function() {
  const text = document.getElementById('textppp');
  const message = "Deks-Tic est une entreprise innovante spécialisée dans le domaine des technologies de l'information et de la communication.";
  let index = 0;

  function showNextLetter() {
    if (index < message.length) {
      text.textContent += message.charAt(index);
      index++;
      setTimeout(showNextLetter, 10); // Affiche la prochaine lettre après un délai de 100ms
    }
  }

  showNextLetter();
});

document.getElementById('contact-form').addEventListener('submit', function(event) {
  event.preventDefault(); // Empêche l'envoi du formulaire par défaut

  // Récupération des valeurs des champs du formulaire
  var name = document.getElementById('name').value;
  var email = document.getElementById('email').value;
  var message = document.getElementById('message').value;

  // Vérification si tous les champs sont remplis
  if (name && email && message) {
    // Affichage des informations envoyées
    var infoDiv = document.getElementById('info');
    infoDiv.innerHTML = '<p>Message envoyée,merci pour votre confiance.</p>' +
                        '<p> Un retour vous sera envoyé par email.</p>' ;

  } else {
    // Affichage d'un message d'erreur si des champs sont manquants
    alert('Veuillez remplir tous les champs du formulaire.');
  }
});

