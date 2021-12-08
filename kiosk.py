import sys
from PyQt5.QtWidgets import *

class kiosk(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Jarvis Cafe")

        layout = QVBoxLayout()

        tab1 = QWidget()
        tab2 = QWidget()
        tab3 = QWidget()

        tabs = QTabWidget()
        tabs.addTab(tab1, "Coffee")
        coffee1 = QPushButton("아메리카노")
        coffee2 = QPushButton("카페라떼")
        coffee3 = QPushButton("카푸치노")
        coffee4 = QPushButton("바닐라 라떼")
        tab1.layout = QVBoxLayout()
        tab1.layout.addWidget(coffee1)
        tab1.layout.addWidget(coffee2)
        tab1.layout.addWidget(coffee3)
        tab1.layout.addWidget(coffee4)
        tab1.setLayout(tab1.layout)

        tabs.addTab(tab2, "Beverage")
        beverage1 = QPushButton("레모네이드")
        beverage2 = QPushButton("초코라떼")
        beverage3 = QPushButton("아이스티")
        beverage4 = QPushButton("딸기 스무디")
        tab2.layout = QVBoxLayout()
        tab2.layout.addWidget(beverage1)
        tab2.layout.addWidget(beverage2)
        tab2.layout.addWidget(beverage3)
        tab2.layout.addWidget(beverage4)
        tab2.setLayout(tab2.layout)

        tabs.addTab(tab3, "Side")
        side1 = QPushButton("초코 케이크")
        side2 = QPushButton("딸기 케이크")
        side3 = QPushButton("티라미수")
        side4 = QPushButton("샌드위치")
        tab3.layout = QVBoxLayout()
        tab3.layout.addWidget(side1)
        tab3.layout.addWidget(side2)
        tab3.layout.addWidget(side3)
        tab3.layout.addWidget(side4)
        tab3.setLayout(tab3.layout)
        result = QLabel("주문 목록:")
        total_price = QLabel("총 가격:")
        self.resultEdit = QTextEdit()
        self.totalPriceEdit = QTextEdit()

        pay = QPushButton("결제하기")
        all_return = QPushButton("모두 취소하기")

        vbox = QVBoxLayout()
        vbox.addWidget(tabs)
        vbox.addWidget(result)
        vbox.addWidget(self.resultEdit)
        vbox.addWidget(total_price)
        vbox.addWidget(self.totalPriceEdit)
        vbox.addWidget(all_return)
        vbox.addWidget(pay)

        coffee1.clicked.connect(self.coffee_order)
        coffee2.clicked.connect(self.coffee_order)
        coffee3.clicked.connect(self.coffee_order)
        coffee4.clicked.connect(self.coffee_order)
        beverage1.clicked.connect(self.beverage_order)
        beverage2.clicked.connect(self.beverage_order)
        beverage3.clicked.connect(self.beverage_order)
        beverage4.clicked.connect(self.beverage_order)
        side1.clicked.connect(self.side_order)
        side2.clicked.connect(self.side_order)
        side3.clicked.connect(self.side_order)
        side4.clicked.connect(self.side_order)
        all_return.clicked.connect(self.Del)
        pay.clicked.connect(self.All_price)

        self.setLayout(vbox)
        self.setLayout(layout)
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def coffee_order(self):
        print("예시")

    def beverage_order(self):
        print("예시")

    def side_order(self):
        print("예시")

    def Del(self):
        print("모든 걸 삭제")

    def All_price(self):
        print("결제하기 누르면 종료...?")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = kiosk()
    sys.exit(app.exec_())
