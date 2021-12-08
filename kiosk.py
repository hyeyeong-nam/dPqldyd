import sys
from PyQt5.QtWidgets import *
import speech_recognition as sr
from STT_test import kakao_stt, KAKAO_APP_KEY

def get_speech():
        
    # 마이크에서 음성을 추출하는 객체
        recognizer = sr.Recognizer()

    # 마이크 설정
        microphone = sr.Microphone(sample_rate=16000)

    # 마이크 소음 수치 반영
        with microphone as source:
            recognizer.adjust_for_ambient_noise(source)
            

    # 음성 수집
        with microphone as source:
            result = recognizer.listen(source)
            audio = result.get_raw_data()

        return audio
class kiosk(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.coffee_price = [2000, 2700, 2700, 3500]
        self.Menu_price = [3000, 3500, 2700, 4000]
        self.total_price = 0
        self.order_list = []
        self.bev_list = []
        

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

        tabs.addTab(tab2, "Menu")
        Menu1 = QPushButton("레모네이드")
        Menu2 = QPushButton("초코라떼")
        Menu3 = QPushButton("아이스티")
        Menu4 = QPushButton("딸기 스무디")
        tab2.layout = QVBoxLayout()
        tab2.layout.addWidget(Menu1)
        tab2.layout.addWidget(Menu2)
        tab2.layout.addWidget(Menu3)
        tab2.layout.addWidget(Menu4)
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
        menu = [item['Menu'] for item in self.order_list]
        if self.order_list == []:
            self.order_list.append({"Menu":"아메리카노", "Amount":1})
        elif "아메리카노" not in menu:
            self.order_list.append({"Menu":"아메리카노", "Amount":1})
        else:    
            for p in self.order_list:
                if p["Menu"] == "아메리카노":
                    if p['Amount'] >= 1:
                        order1_amount = p["Amount"] + 1
                        p['Amount'] = (order1_amount)
                        print(self.order_list)
                        
        self.showListAll()
        
            
    def coffee_order2(self):
        menu = [item['Menu'] for item in self.order_list]
        if self.order_list == []:
            self.order_list.append({"Menu":"카페 라떼", "Amount":1})
        elif "카페 라떼" not in menu:
            self.order_list.append({"Menu":"카페 라떼", "Amount":1})
        else:    
            for p in self.order_list:
                if p["Menu"] == "카페 라떼":
                    if p['Amount'] >= 1:
                        p['Amount'] = p['Amount'] + 1
                        print(self.order_list)
                        
                
        self.showListAll()
        
    def coffee_order3(self):
        menu = [item['Menu'] for item in self.order_list]
        if self.order_list == []:
            self.order_list.append({"Menu":"카푸치노", "Amount":1})
        elif "카푸치노" not in menu:
            self.order_list.append({"Menu":"카푸치노", "Amount":1})
        else:    
            for p in self.order_list:
                if p["Menu"] == "카푸치노":
                    if p['Amount'] >= 1:
                        order1_amount = p["Amount"] + 1
                        p['Amount'] = (order1_amount)
                        print(self.order_list)
        self.showListAll()
        
    def coffee_order4(self):
        menu = [item['Menu'] for item in self.order_list]
        if self.order_list == []:
            self.order_list.append({"Menu":"바닐라 라떼", "Amount":1})
        elif "바닐라 라떼" not in menu:
            self.order_list.append({"Menu":"바닐라 라떼", "Amount":1})
        else:    
            for p in self.order_list:
                if p["Menu"] == "바닐라 라떼":
                    if p['Amount'] >= 1:
                        order1_amount = p["Amount"] + 1
                        p['Amount'] = (order1_amount)
                        print(self.order_list)
        self.showListAll()

    def Menu_order1(self):
        menu = [item['Menu'] for item in self.order_list]
        if self.order_list == []:
            self.order_list.append({"Menu":"레모네이드", "Amount":1})
        elif "레모네이드" not in menu:
            self.order_list.append({"Menu":"레모네이드", "Amount":1})
        else:    
            for p in self.order_list:
                if p["Menu"] == "레모네이드":
                    if p['Amount'] >= 1:
                        order1_amount = p["Amount"] + 1
                        p['Amount'] = (order1_amount)
                        print(self.order_list)
        self.showListAll()
    def Menu_order2(self):
        menu = [item['Menu'] for item in self.order_list]
        if self.order_list == []:
            self.order_list.append({"Menu":"초코 라떼", "Amount":1})
        elif "초코 라떼" not in menu:
            self.order_list.append({"Menu":"초코 라떼", "Amount":1})
        else:    
            for p in self.order_list:
                if p["Menu"] == "초코 라떼":
                    if p['Amount'] >= 1:
                        order1_amount = p["Amount"] + 1
                        p['Amount'] = (order1_amount)
                        print(self.order_list)
        self.showListAll()
    def Menu_order3(self):
        menu = [item['Menu'] for item in self.order_list]
        if self.order_list == []:
            self.order_list.append({"Menu":"아이스티", "Amount":1})
        elif "아이스티" not in menu:
            self.order_list.append({"Menu":"아이스티", "Amount":1})
        else:    
            for p in self.order_list:
                if p["Menu"] == "아이스티":
                    if p['Amount'] >= 1:
                        order1_amount = p["Amount"] + 1
                        p['Amount'] = (order1_amount)
                        print(self.order_list)
        self.showListAll()
    def Menu_order4(self):
        menu = [item['Menu'] for item in self.order_list]
        if self.order_list == []:
            self.order_list.append({"Menu":"딸기 스무디", "Amount":1})
        elif "딸기 스무디" not in menu:
            self.order_list.append({"Menu":"딸기 스무디", "Amount":1})
        else:    
            for p in self.order_list:
                if p["Menu"] == "딸기 스무디":
                    if p['Amount'] >= 1:
                        order1_amount = p["Amount"] + 1
                        p['Amount'] = (order1_amount)
                        print(self.order_list)
        self.showListAll()

    def side_order1(self):
        menu = [item['Menu'] for item in self.order_list]
        if self.order_list == []:
            self.order_list.append({"Menu":"초코 케이크", "Amount":1})
        elif "초코 케이크" not in menu:
            self.order_list.append({"Menu":"초코 케이크", "Amount":1})
        else:    
            for p in self.order_list:
                if p["Menu"] == "초코 케이크":
                    if p['Amount'] >= 1:
                        order1_amount = p["Amount"] + 1
                        p['Amount'] = (order1_amount)
                        print(self.order_list)
        self.showListAll()
    def side_order2(self):
        menu = [item['Menu'] for item in self.order_list]
        if self.order_list == []:
            self.order_list.append({"Menu":"딸기 케이크", "Amount":1})
        elif "딸기 케이크" not in menu:
            self.order_list.append({"Menu":"딸기 케이크", "Amount":1})
        else:    
            for p in self.order_list:
                if p["Menu"] == "딸기 케이크":
                    if p['Amount'] >= 1:
                        order1_amount = p["Amount"] + 1
                        p['Amount'] = (order1_amount)
                        print(self.order_list)
        self.showListAll()
    def side_order3(self):
        menu = [item['Menu'] for item in self.order_list]
        if self.order_list == []:
            self.order_list.append({"Menu":"티라미수", "Amount":1})
        elif "티라미수" not in menu:
            self.order_list.append({"Menu":"티라미수", "Amount":1})
        else:    
            for p in self.order_list:
                if p["Menu"] == "티라미수":
                    if p['Amount'] >= 1:
                        order1_amount = p["Amount"] + 1
                        p['Amount'] = (order1_amount)
                        print(self.order_list)
        self.showListAll()
    def side_order4(self):
        menu = [item['Menu'] for item in self.order_list]
        if self.order_list == []:
            self.order_list.append({"Menu":"샌드위치", "Amount":1})
        elif "샌드위치" not in menu:
            self.order_list.append({"Menu":"샌드위치", "Amount":1})
        else:    
            for p in self.order_list:
                if p["Menu"] == "샌드위치":
                    if p['Amount'] >= 1:
                        order1_amount = p["Amount"] + 1
                        p['Amount'] = (order1_amount)
                        print(self.order_list)
        self.showListAll()

    def Mike_order(self):
        audio = get_speech()
        text = kakao_stt(KAKAO_APP_KEY, "stream", audio)
        print(text)
        if "아메리카노" in text:
            self.coffee_order1()
        if "카페 라떼" in text:
            self.coffee_order2()
        if "카푸치노" in text:
            self.coffee_order3()
        if "바닐라 라떼" in text:
            self.coffee_order4()
            

    def Del(self):
        print("모든 걸 삭제")

    def All_price(self):
        print("결제하기 누르면 종료...?")

    def showListAll(self):
        te=[]
        
        for p in self.order_list:
            
            for attr in p:
                te.append(str(attr) + ":")
                te.append('\t')
                te.append(str(p[attr]))
                te.append("\t")
            
        self.resultEdit.setText(''.join(te))
        self.totalPriceEdit.setText(str(self.total_price))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = kiosk()
    sys.exit(app.exec_())
