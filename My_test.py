class BooksCollector:

    def collector(self):
        return BooksCollector()

    def test_add_new_book_valid_name(self, collector):
        collector.add_new_book("Гарри Поттер")
        assert "Гарри Поттер" in collector.books_genre
        assert collector.books_genre["Гарри Поттер"] == ""  

    def test_add_new_book_name_too_long(self, collector):
        name = "О" * 40
        collector.add_new_book(name)
        assert name in collector.books_genre
        assert collector.books_genre[name] == ""


    def test_add_new_book_duplicate(self, collector):
        collector.add_new_book("Книга")
        collector.add_new_book("Книга")
        assert len(collector.books_genre) == 1

    def test_set_book_genre_book_not_exists(self, collector):
        collector.set_book_genre("Неправильная", "Фантастика")
        assert "Неправильная" not in collector.books_genre

    def test_set_book_genre_invalid_genre(self, collector):
        collector.add_new_book("Книга")
        collector.set_book_genre("Книга", "Неправильный жанр")
        assert collector.books_genre["Книга"] == ""

    def test_get_book_genre_exists(self, collector):
        collector.add_new_book("Книга")
        collector.set_book_genre("Книга", "Комедии")
        assert collector.get_book_genre("Книга") == "Комедии"

    def test_get_book_genre_not_exists(self, collector):
        assert collector.get_book_genre("Неправильная") is None

    def test_get_books_with_specific_genre(self, collector):
        collector.add_new_book("Книга1")
        collector.add_new_book("Книга2")
        collector.set_book_genre("Книга1", "Фантастика")
        collector.set_book_genre("Книга2", "Фантастика")
        
        result = collector.get_books_with_specific_genre("Фантастика")
        assert len(result) == 2
        assert "Книга1" in result
        assert "Книга2" in result

    def test_get_books_with_specific_genre_no_matches(self, collector):
        collector.add_new_book("Книга")
        collector.set_book_genre("Книга", "Комедии")
        result = collector.get_books_with_specific_genre("Фантастика")
        assert result == []

    def test_get_books_with_specific_genre_invalid_genre(self, collector):
        collector.add_new_book("Книга")
        result = collector.get_books_with_specific_genre("Неправильная")
        assert result == []

    def test_get_books_genre(self, collector):
        collector.add_new_book("Книга1")
        collector.add_new_book("Книга2")
        assert collector.get_books_genre() == {"Книга1": "", "Книга2": ""}

    def test_get_books_for_children(self, collector):
        collector.add_new_book("Детская книга")
        collector.add_new_book("Взрослая книга")
        collector.set_book_genre("Детская книга", "Мультфильмы")
        collector.set_book_genre("Взрослая книга", "Ужасы")
        result = collector.get_books_for_children()
        assert result == ["Детская книга"]

    def test_get_books_for_children_no_genre(self, collector):
        collector.add_new_book("Книга без жанра")
        result = collector.get_books_for_children()
        assert result == []

    def test_add_book_in_favorites_valid(self, collector):
        collector.add_new_book("Книга")
        collector.add_book_in_favorites("Книга")
        assert "Книга" in collector.favorites

    def test_add_book_in_favorites_book_not_in_genre(self, collector):
        collector.add_book_in_favorites("Неправильная")
        assert "Неправильная" not in collector.favorites

    def test_add_book_in_favorites_duplicate(self, collector):
        collector.add_new_book("Книга")
        collector.add_book_in_favorites("Книга")
        collector.add_book_in_favorites("Книга")
        assert collector.favorites.count("Книга") == 1

    def test_delete_book_from_favorites(self, collector):
        collector.add_new_book("Книга")
        collector.add_book_in_favorites("Книга")
        collector.delete_book_from_favorites("Книга")
        assert "Книга" not in collector.favorites

    def test_delete_book_from_favorites_not_in_list(self, collector):
       collector.delete_book_from_favorites("Неправильная")
       assert collector.favorites == []

    def test_get_list_of_favorites_books(self, collector):
        collector.add_new_book("Книга1")
        collector.add_new_book("Книга2")
        collector.add_book_in_favorites("Книга1")
        collector.add_book_in_favorites("Книга2")
        
        favorites = collector.get_list_of_favorites_books()
        assert len(favorites) == 2
        assert "Книга1" in favorites
        assert "Книга2" in favorites# qa_python