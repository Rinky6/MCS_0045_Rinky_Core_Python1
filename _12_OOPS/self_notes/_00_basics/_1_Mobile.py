class Mobile:

    # 1. STATE
    def __init__(self, brand_name, m_name, m_price):
        self.brand_name = brand_name
        self.m_name = m_name
        self.m_price = m_price

    # 2. BEHAVIOR
    def get_info(self):
       print("Mobile details are ", self.brand_name, self.m_name, self.m_price)

m_details = Mobile("Realme", 'Realme GT', 25000)
print(m_details)
m_details.get_info()