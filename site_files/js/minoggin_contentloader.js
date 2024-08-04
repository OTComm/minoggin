document.addEventListener('DOMContentLoaded', function() {
    // Event delegation for navigation links
    document.body.addEventListener('click', function(e) {
        // Check if the click is within a link
        let target = e.target.closest('a');
        if (target && target.matches('nav a, .related-topics a, .breadcrumb a')) {
            e.preventDefault();
            const href = target.getAttribute('href');

            fetch(href)
                .then(response => {
                    if (response.ok) return response.text();
                    throw new Error('Network response was not ok');
                })
                .then(html => {
                    const mainContent = document.getElementById('main-content');
                    mainContent.innerHTML = html;
                    mainContent.scrollTop = 0; // Scroll the main content to the top
                })
                .catch(error => {
                    console.error('Error loading the page: ', error);
                    document.getElementById('main-content').innerHTML = 'Coming soon.';
                });
        }
    });

    // Tooltip functionality could be re-added here if needed

    // Listener for small screen auto menu close
    document.querySelectorAll('#navbarScroll .dropdown-item').forEach(function(element) {
        element.addEventListener('click', function() {
            let button = document.querySelector('.navbar-toggler');
            if (button && window.getComputedStyle(button).display !== 'none') {
                button.click(); // Simulates a click on the navbar toggler button, closing the navbar
            }
        });
    });
});
