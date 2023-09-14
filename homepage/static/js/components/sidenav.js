function openNav(sidenav) {
    sidenav.style.width = '15%';
    main = document.getElementsByClassName('main')[0].style.marginLeft = '15%';
    sidenav.setAttribute('open', 'open');
    apps = sidenav.getElementsByClassName('app-index');
    Array.from(apps).forEach(element => {
        element.style.opacity = '100%';
    });
}

function closeNav(sidenav) {
    sidenav.style.width = '5%';
    main = document.getElementsByClassName('main')[0].style.marginLeft = '5%';
    sidenav.removeAttribute('open');
    apps = sidenav.getElementsByClassName('app-index');
    Array.from(apps).forEach(element => {
        element.style.opacity = '0%';
    });
}

function toggleNav(sidenav) {
    is_open = sidenav.getAttribute('open') || false;
    if (is_open) {closeNav(sidenav);} else {openNav(sidenav);}
}

document.addEventListener('DOMContentLoaded', (event) => {
    sidenav = document.getElementsByClassName('sidenav')[0];
    closeNav(sidenav);
    hamburger = sidenav.getElementsByClassName('hamburger__toggle')[0];
    hamburger.addEventListener('click', event => toggleNav(sidenav));
});
