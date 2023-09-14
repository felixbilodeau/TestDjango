document.addEventListener('DOMContentLoaded', (event) => {
    hamburgers = document.getElementsByClassName('hamburger__toggle');
    Array.from(hamburgers).forEach(element => {
        let icon = element.getElementsByClassName('hamburger__icon')[0];
        let top_bar = icon.getElementsByClassName('top-bar')[0];
        let middle_bar = icon.getElementsByClassName('middle-bar')[0];
        let bottom_bar = icon.getElementsByClassName('bottom-bar')[0];
        element.addEventListener('click', event => {
            is_clicked = icon.getAttribute('clicked') || false;
            if (is_clicked) {
                top_bar.style.top = 'calc(50% - 11px)';
                top_bar.style.height = '2px';
                top_bar.style.transform = 'rotate(0)'
                middle_bar.style.transform = 'scale(1)'
                bottom_bar.style.top = 'calc(50% + 9px)';
                bottom_bar.style.height = '2px';
                bottom_bar.style.transform = 'rotate(0)'
                icon.removeAttribute('clicked')
            }
            else {
                top_bar.style.top = '50%';
                top_bar.style.height = '3px';
                top_bar.style.transform = 'rotate(45deg)'
                middle_bar.style.transform = 'scale(0)'
                bottom_bar.style.top = '50%';
                bottom_bar.style.height = '3px';
                bottom_bar.style.transform = 'rotate(-45deg)'
                icon.setAttribute('clicked', 'clicked')
            }
        });
    });
});
