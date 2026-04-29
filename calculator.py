# calculator.py - 充满坏味道的初始版本

class Calculator:
    # 坏味道1：过长的函数 (Long Method)
    # 这个函数做了太多事情：计算、折扣、税费、积分
    def process_order(self, items, customer_type, total):
        # 1. 原始逻辑
        print(f"Processing {len(items)} items...")
        
        # 2. 过多的条件判断，且逻辑重复（坏味道2的源头）
        if customer_type == "regular":
            if total > 100:
                total = total * 0.9  # 打9折
            print("Regular customer discount applied.")
        elif customer_type == "vip":
            if total > 100:
                total = total * 0.85  # 打8.5折
            print("VIP customer discount applied.")
        
        # 3. 计算税费 (这部分逻辑与折扣逻辑混杂在一起)
        tax = total * 0.1
        final_total = total + tax
        
        # 4. 计算积分 (坏味道2：重复代码。下面的if结构和上面的折扣逻辑非常相似)
        points = 0
        if customer_type == "regular":
            points = final_total // 10
        elif customer_type == "vip":
            points = final_total // 8
            print("VIP bonus points.")
        
        print(f"Final total: {final_total}, Points earned: {points}")
        return final_total


# 坏味道3：未使用的变量和导入 (Unused variable)
unused_variable = 42
