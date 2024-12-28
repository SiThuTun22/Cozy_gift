function toggleFilter(filterId, header) {
    const content = document.getElementById(filterId);
    content.classList.toggle('visible');
    header.classList.toggle('open');
}
function toggleFilter(filterId) {
    const content = document.getElementById(filterId);
    content.classList.toggle('visible');
}