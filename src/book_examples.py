from pydantic import BaseModel
from typing import List

from src.models import Author, Book

ExampleBookData = [
    Book(
        title='The Great Gatsby',
        authors=[Author(name='F. Scott Fitzgerald'), Author(name='Zweiter Autor')],
        description_short='''"The Great Gatsby" is a timeless classic written by F. Scott Fitzgerald. This novel explores the complexities of the American Dream through the captivating story of Jay Gatsby, a mysterious millionaire, and his pursuit of the elusive Daisy Buchanan. Set in the Roaring Twenties, amidst the opulence and decadence of Long Island, New York, the novel delves into themes of love, wealth, and the illusion of success. As Gatsby navigates through lavish parties and tangled relationships, the narrative unveils the fragile facade of the American Dream, revealing the emptiness that lies beneath. With its vivid portrayal of society's excesses and poignant exploration of human desires, "The Great Gatsby" continues to resonate with readers worldwide, offering a compelling glimpse into the allure and disillusionment of the Jazz Age.''',
        image_url='https://picsum.photos/id/1/500',
        isbn='9780743273565'
    ),
    Book(
        title='To Kill a Mockingbird',
        authors=[Author(name='Harper Lee')],
        description_short='A novel about racial injustice in the American South.',
        image_url='https://picsum.photos/id/2/500',
        isbn='9780061120084'
    ),
    Book(
        title='1984',
        authors=[Author(name='George Orwell')],
        description_short='A dystopian novel set in a totalitarian society.',
        image_url='https://picsum.photos/id/3/500',
        isbn='9780451524935'
    ),
    Book(
        title='Pride and Prejudice',
        authors=[Author(name='Jane Austen')],
        description_short='A romantic novel set in 19th-century England.',
        image_url='https://picsum.photos/id/4/500',
        isbn='9780141439518'
    ),
    Book(
        title='The Catcher in the Rye',
        authors=[Author(name='J.D. Salinger')],
        description_short='A coming-of-age novel featuring angst and alienation.',
        image_url='https://picsum.photos/id/5/500',
        isbn='9780316769488'
    ),
    Book(
        title="Harry Potter and the Sorcerer's Stone",
        authors=[Author(name='J.K. Rowling')],
        description_short='The first book in the Harry Potter series.',
        image_url='https://picsum.photos/id/6/500',
        isbn='9780590353427'
    ),
    Book(
        title='The Lord of the Rings',
        authors=[Author(name='J.R.R. Tolkien')],
        description_short='An epic fantasy novel about a quest to destroy a powerful ring.',
        image_url='https://picsum.photos/id/7/500',
        isbn='9780618640157'
    ),
    Book(
        title='The Hobbit',
        authors=[Author(name='J.R.R. Tolkien')],
        description_short="A fantasy novel about a hobbit's journey to reclaim treasure.",
        image_url='https://picsum.photos/id/8/500',
        isbn='9780345339683'
    ),
    Book(
        title='Moby-Dick',
        authors=[Author(name='Herman Melville')],
        description_short="A novel about a captain's obsession with hunting a whale.",
        image_url='https://picsum.photos/id/9/500',
        isbn='9780142437247'
    ),
    Book(
        title='The Adventures of Huckleberry Finn',
        authors=[Author(name='Mark Twain')],
        description_short="A novel about a boy's journey down the Mississippi River.",
        image_url='https://picsum.photos/id/10/500',
        isbn='9780142437179'
    )
    # Add more books here...
]
