function toggleContent(int) {
    const content = document.querySelectorAll('.content')[int];
    const categorie = document.querySelectorAll('.categorie')[int];

    content.classList.toggle('show');
    categorie.classList.toggle('active');
  }
  