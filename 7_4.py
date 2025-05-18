class QuadraticPolynomial:
    def __init__(self, a, b, c):
        """Khởi tạo tam thức bậc hai với các hệ số a, b, c"""
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)

    def __str__(self):
        """In tam thức dưới dạng ax² + bx + c"""
        # Xử lý dấu và định dạng các hệ số
        a_term = f"{self.a}x²" if self.a != 0 else ""
        b_term = f"{'-' if self.b < 0 else '+' if a_term else ''} {abs(self.b)}x" if self.b != 0 else ""
        c_term = f"{'-' if self.c < 0 else '+' if (a_term or b_term) else ''} {abs(self.c)}" if self.c != 0 else ""

        # Trường hợp tam thức bằng 0
        if not (a_term or b_term or c_term):
            return "0"

        return f"{a_term} {b_term} {c_term}".strip()

    def __neg__(self):
        """Đổi dấu tam thức: -a, -b, -c"""
        return QuadraticPolynomial(-self.a, -self.b, -self.c)

    def __add__(self, other):
        """Cộng hai tam thức: cộng các hệ số tương ứng"""
        return QuadraticPolynomial(self.a + other.a, self.b + other.b, self.c + other.c)

    def __sub__(self, other):
        """Trừ hai tam thức: trừ các hệ số tương ứng"""
        return QuadraticPolynomial(self.a - other.a, self.b - other.b, self.c - other.c)


def main():
    # Khởi tạo hai tam thức
    poly1 = QuadraticPolynomial(2, -3, 4)
    poly2 = QuadraticPolynomial(-1, 5, -2)

    # In hai tam thức ban đầu
    print("Tam thức 1:", poly1)
    print("Tam thức 2:", poly2)

    # Đảo dấu hai tam thức
    neg_poly1 = -poly1
    neg_poly2 = -poly2

    # In các tam thức đã đảo dấu
    print("\nTam thức 1 sau khi đảo dấu:", neg_poly1)
    print("Tam thức 2 sau khi đảo dấu:", neg_poly2)

    # Tính tổng và hiệu của hai tam thức đã đảo dấu
    sum_poly = neg_poly1 + neg_poly2
    diff_poly = neg_poly1 - neg_poly2

    # In kết quả tổng và hiệu
    print("\nTổng của hai tam thức đã đảo dấu:", sum_poly)
    print("Hiệu của hai tam thức đã đảo dấu:", diff_poly)


if __name__ == "__main__":
    main()