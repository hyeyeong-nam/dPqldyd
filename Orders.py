class Order:
    def __init__(self):
        self.menu_list = []
        self.coffee_price = [2000, 2700, 2700, 3500]
        self.Menu_price = [3000, 3500, 2700, 4000]
        self.Side_price = [3000, 3200, 3400, 4200]
        self.coffee_menu = ["아메리카노", "카페 라떼", "카푸치노", "바닐라 라떼"]
        self.Menu_menu = ["레모네이드", "초코 라떼", "아이스티", "딸기 스무디"]
        self.side_menu = ["초코 케이크", "딸기 케이크", "티라미수", "샌드위치"]
        self.total_price = 0
        self.ordered = ''
        
    def guess_menu(self):
        
        if self.ordered in self.coffee_menu:
            menu_index = self.coffee_menu.index(self.ordered)
            menu_price = self.coffee_price[menu_index]
            
        elif self.ordered in self.Menu_menu:
            menu_index = self.Menu_menu.index(self.ordered)
            menu_price = self.Menu_price[menu_index]
            
        elif self.ordered in self.side_menu:
            menu_index = self.side_menu.index(self.ordered)
            menu_price = self.Side_price[menu_index]
            
        return menu_price
            
    def add_order(self,order):
        
        menu = [item['Menu'] for item in self.menu_list]
        self.ordered = order
        if self.ordered not in menu:
            self.menu_list.append({"Menu":self.ordered, "Amount":1})
            self.total_price += self.guess_menu()
            
        else:
            for p in self.menu_list:
                if p["Menu"] == self.ordered:
                    if p['Amount'] >= 1:
                        order_amount = p["Amount"] + 1
                        p['Amount'] = (order_amount)
                        self.total_price += self.guess_menu()
                        
    def getOrderList(self):
        return self.menu_list
    
    def getTotalPrice(self):
        return self.total_price
    
    def clearTotalPrice(self):
        self.total_price = 0
                        
