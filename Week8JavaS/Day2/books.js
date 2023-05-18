let book1 = {
    'title': 'A Captain at Fifteen',
    'author': 'Jules Verne',
    'image' : 'https://avatars.dzeninfra.ru/get-zen_doc/2376594/pub_5f4b72ae25c0b248d3b38200_5f4b744c0abe973a97f27a42/scale_1200',
    'alreadyRead' : true 
    }
    
let book2 = {
        'title': 'The Jungle book',
        'author': 'Kipling',
        'image' : 'https://wallup.net/wp-content/uploads/2019/09/918116-jungle-book-disney-fantasy-family-cartoon-comedy-adventure-drama-1jbook.jpg',
        'alreadyRead' : true 
        }
    

    
let book3 = {
            'title': 'Winnie the Pooh',
            'author': 'Alan Miln',
            'image' : 'https://mobimg.b-cdn.net/v3/fetch/dc/dcf088edc24424b3a2791edb5660070f.jpeg',
            'alreadyRead' : false
            }
        
    let  allBooks =[book1, book2, book3]
    
    const bookSection = document.getElementsByClassName('listBooks')[0];
    
    
    function renderBook(book) {
      // <div> for the book
      const bookDiv = document.createElement('div');
      bookDiv.classList.add('book');
    
      //  <h2> element for  book title
      const titleElement = document.createElement('h2');
      titleElement.textContent = book.title;
    
      if (book.alreadyRead) {
                    titleElement.style.color = 'red';
                }
    
        //  <h3> element for book author
      const authElement = document.createElement('h3');
      authElement.textContent = "by "+ book.author;
    
    
      // <img> for  book image
      const imageElement = document.createElement('img');
      imageElement.src = book.image;
      imageElement.alt = book.title;
    
      // Append title, author and image  to the book div
      bookDiv.appendChild(titleElement);
      bookDiv.appendChild(authElement);
      bookDiv.appendChild(imageElement);
    
      // Append book div to  book section
      bookSection.appendChild(bookDiv);
    }
    
    // functions for each book
    renderBook(book1);
    renderBook(book2);
    renderBook(book3);