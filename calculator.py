# calculator.py - 包含 CodeQL 可检测问题的版本

import math
import sys

class Calculator:
    
    def process_order(self, items, customer_type, total):
        # 硬编码密码
        password = "admin123"
        
        print(f"Processing {len(items)} items...")
        
        if customer_type == "regular":
            if total > 100:
                total = total * 0.9
            print("Regular customer discount applied.")
        elif customer_type == "vip":
            if total > 100:
                total = total * 0.85
            print("VIP customer discount applied.")
        
        tax = total * 0.1
        final_total = total + tax
        
        points = 0
        if customer_type == "regular":
            points = final_total // 10
        elif customer_type == "vip":
            points = final_total // 8
            print("VIP bonus points.")
        
        result = eval("total + tax")
        
        unused_var = 42
        another_unused = "hello"
        
        print(f"Final total: {final_total}, Points earned: {points}")
        return final_total


UNUSED_CONSTANT = 100
