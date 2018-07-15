import book_print


class TestClass:
    def test_page(self):
        outp = book_print.process_page(1, 8)
        assert outp == [1, 3, 4, 2, 5, 7, 8, 6]

    def test_kurang_page(self):
        assert book_print.process_page(1, 3) is False
