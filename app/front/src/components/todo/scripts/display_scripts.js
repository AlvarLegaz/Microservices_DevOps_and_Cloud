function toggleDescription(card) {
    const description = card.querySelector('.description');
    const title = card.querySelector('.title');

    if (description.style.display === 'none') {
        description.style.display = 'block';
    } else {
        description.style.display = 'none';
    }
}