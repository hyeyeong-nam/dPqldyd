import sys
from PyQt5.QtGui import QCloseEvent
from PyQt5.QtWidgets import QApplication, QMessageBox, QWidget, QPushButton, QVBoxLayout, QTabWidget, QLabel, QTextEdit
from Orders import Order
from Voice_Recog import voice_recog


class kiosk_main(QWidget):

    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        self.order = Order()
        self.voice = voice_recog()
        
        
        

    def initUI(self):
        self.setWindowTitle("Jarvis Cafe")

        layout = QVBoxLayout()

        tab1 = QWidget()
        tab2 = QWidget()
        tab3 = QWidget()
        
        tabs = QTabWidget()
        tabs.addTab(tab1, "Coffee")
        coffee1 = QPushButton("아메리카노 : 2000원")
        coffee2 = QPushButton("카페 라떼 : 2700원")
        coffee3 = QPushButton("카푸치노: 2700원")
        coffee4 = QPushButton("바닐라 라떼 : 3500원")
        tab1.layout = QVBoxLayout()
        tab1.layout.addWidget(coffee1)
        tab1.layout.addWidget(coffee2)
        tab1.layout.addWidget(coffee3)
        tab1.layout.addWidget(coffee4)
        tab1.setLayout(tab1.layout)

        tabs.addTab(tab2, "Menu")
        Menu1 = QPushButton("레모네이드 : 3000원")
        Menu2 = QPushButton("초코 라떼 : 3500원")
        Menu3 = QPushButton("아이스티 : 2700원")
        Menu4 = QPushButton("딸기 스무디 : 4000원")
        tab2.layout = QVBoxLayout()
        tab2.layout.addWidget(Menu1)
        tab2.layout.addWidget(Menu2)
        tab2.layout.addWidget(Menu3)
        tab2.layout.addWidget(Menu4)
        tab2.setLayout(tab2.layout)

        tabs.addTab(tab3, "Side")
        side1 = QPushButton("초코 케이크 : 3000원")
        side2 = QPushButton("딸기 케이크 : 3200원")
        side3 = QPushButton("티라미수 : 3400원")
        side4 = QPushButton("샌드위치 : 4200원")
        tab3.layout = QVBoxLayout()
        tab3.layout.addWidget(side1)
        tab3.layout.addWidget(side2)
        tab3.layout.addWidget(side3)
        tab3.layout.addWidget(side4)
        tab3.setLayout(tab3.layout)
        result = QLabel("주문 목록:")
        total_price = QLabel("총 가격:")
        self.resultEdit = QTextEdit()
        self.resultEdit.setReadOnly(True)
        self.totalPriceEdit = QTextEdit()
        self.totalPriceEdit.setReadOnly(True)

        mike = QPushButton("음성인식 하기")
        pay = QPushButton("결제하기")
        all_return = QPushButton("모두 취소하기")

        vbox = QVBoxLayout()
        vbox.addWidget(tabs)
        vbox.addWidget(result)
        vbox.addWidget(self.resultEdit)
        vbox.addWidget(total_price)
        vbox.addWidget(self.totalPriceEdit)
        vbox.addWidget(mike)
        vbox.addWidget(all_return)
        vbox.addWidget(pay)

        coffee1.clicked.connect(self.coffee_order1)
        coffee2.clicked.connect(self.coffee_order2)
        coffee3.clicked.connect(self.coffee_order3)
        coffee4.clicked.connect(self.coffee_order4)
        Menu1.clicked.connect(self.Menu_order1)
        Menu2.clicked.connect(self.Menu_order2)
        Menu3.clicked.connect(self.Menu_order3)
        Menu4.clicked.connect(self.Menu_order4)
        side1.clicked.connect(self.side_order1)
        side2.clicked.connect(self.side_order2)
        side3.clicked.connect(self.side_order3)
        side4.clicked.connect(self.side_order4)
        mike.clicked.connect(self.Mike_order)
        all_return.clicked.connect(self.Del)
        pay.clicked.connect(self.All_price)

        self.setLayout(vbox)
        self.setLayout(layout)
        self.setGeometry(300, 300, 300, 200)
        self.show()
        
    def coffee_order1(self):
        
        
        
        # if "아메리카노" not in menu:
            # self.order_list.append({"Menu":"아메리카노", "Amount":1})
        #     self.total_price += self.coffee_price[0]
         
        self.order.add_order("아메리카노")  
        #     for p in self.order_list:
        #         if p["Menu"] == "아메리카노":
        #             if p['Amount'] >= 1:
        #                 order1_amount = p["Amount"] + 1
        #                 p['Amount'] = (order1_amount)
        #                 print(self.order_list)
        #                 self.total_price += self.coffee_price[0]
                        
        self.showListAll()
        
            
    def coffee_order2(self):
        self.order.add_order("카페 라떼")  
        self.showListAll()
                        
                
        self.showListAll()
        
    def coffee_order3(self):
        self.order.add_order("카푸치노")  
        self.showListAll()
        
        
    def coffee_order4(self):
        self.order.add_order("바닐라 라떼")  
        self.showListAll()

    def Menu_order1(self):
        self.order.add_order("레모네이드")  
        self.showListAll()
        
    def Menu_order2(self):
        self.order.add_order("초코 라떼")  
        self.showListAll()
        
    def Menu_order3(self):
        self.order.add_order("아이스티")  
        self.showListAll()
        
    def Menu_order4(self):
        self.order.add_order("딸기 스무디")  
        self.showListAll()

    def side_order1(self):
        self.order.add_order("초코 케이크")  
        self.showListAll()
        
    def side_order2(self):
        self.order.add_order("딸기 케이크")  
        self.showListAll()
        
    def side_order3(self):
        self.order.add_order("티라미수")  
        self.showListAll()
        
    def side_order4(self):
        self.order.add_order("샌드위치")  
        self.showListAll()

    def Mike_order(self):
        text = self.voice.kakao_voice()
        print(text)
        if "아메리카노" in text:
            self.coffee_order1()
        if "카페 라떼" in text:
            self.coffee_order2()
        if "카푸치노" in text:
            self.coffee_order3()
        if "바닐라 라떼" in text:
            self.coffee_order4()
        if "레모네이드" in text:
            self.Menu_order1()
        if "초코 라떼" in text:
            self.Menu_order2()
        if "아이스티" in text:
            self.Menu_order3()
        if "딸기 스무디" in text:
            self.Menu_order4()
        if "초코 케이크" in text:
            self.side_order1()
        if "딸기 케이크" in text:
            self.side_order2()
        if "티라미수" in text:
            self.side_order3()
        if "샌드위치" in text:
            self.side_order4()
            

    def Del(self):
        self.order_list.clear()
        self.order.clearTotalPrice()
        self.showListAll()

    def All_price(self):
        exit_window = QMessageBox.question(self, "Result", str(self.total_price)+"원 결제되셨습니다.", 
                             QMessageBox.Yes)
        if exit_window == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()

    def showListAll(self):
        te=[]
        self.order_list = self.order.getOrderList()
        self.total_price = self.order.getTotalPrice()
        for p in self.order_list:
            
            for attr in p:
                te.append(str(attr) + ":")
                te.append('\t')
                te.append(str(p[attr]))
                te.append("\t")
            
        self.resultEdit.setText(''.join(te))
        self.totalPriceEdit.setText(str(self.total_price)+"원")
        

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    kiosk = kiosk_main()
    kiosk.show()
    sys.exit(app.exec_())
