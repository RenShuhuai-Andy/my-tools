from typing import List

def get_yearly_tax_rate(amount):
    '''
    获取综合所得年度税率和速算扣除数
    amount: 年度综合所得
    '''
    # 综合所得年度税率和速算扣除数表（适用于年度计算）
    yearly_tax_brackets = [
        (0, 36000, 0.03, 0),
        (36000, 144000, 0.10, 2520),
        (144000, 300000, 0.20, 16920),
        (300000, 420000, 0.25, 31920),
        (420000, 660000, 0.30, 52920),
        (660000, 960000, 0.35, 85920),
        (960000, float('inf'), 0.45, 181920),
    ]

    for bracket in yearly_tax_brackets:
        min_amt, max_amt, rate, quick_deduction = bracket
        if min_amt <= amount < max_amt:
            return rate, quick_deduction
    return 0.45, 181920


def get_monthly_tax_rate(amount):
    '''
    获取综合所得月度税率和速算扣除数
    amount: 月度综合所得
    '''
    # 综合所得月度税率和速算扣除数表（适用于月度计算）
    monthly_tax_brackets = [
        (0, 3000, 0.03, 0),
        (3000, 12000, 0.10, 210),
        (12000, 25000, 0.20, 1410),
        (25000, 35000, 0.25, 2660),
        (35000, 55000, 0.30, 4410),
        (55000, 80000, 0.35, 7160),
        (80000, float('inf'), 0.45, 15160),
    ]

    for bracket in monthly_tax_brackets:
        lower, upper, rate, quick_deduction = bracket
        if lower < amount <= upper:
            return rate, quick_deduction
    return 0.45, 15160


def calculate_wuxian_yijin(x):
    '''
    计算五险一金
    '''
    x = max(min(x, 35283), 6821)  # 缴纳基数，下限6821，上限35283
    old = 0.08 * x  # 养老保险，单位16%，个人8%
    unemploy = 0.005 * x  # 失业保险，单位1.5%，个人0.5%。
    med = 0.02 * x + 3  # 医疗保险，单位8%，个人2%+3元
    house = 0.12 * x  # 住房公积金
    wuxian_yijin = old + unemploy + med + house  # 五险一金
    return wuxian_yijin


def calculate_cumulative_income(monthly_incomes: List[float], signature_fees: List[float], has_taxs: List[int],
                                special_deduction: float = 0):
    '''
    计算税后月薪
    monthly_incomes: 税前月薪。 [40000] * 12 代表12个月每月税前月薪4w; [32000] * 6 + [40000] * 6 代表前6个月每月税前3.2w，后6个月每月税前4w
    signature_fees: 签字费。[0] * 6 + [50000] + [0] * 5 代表7月获得一笔5w签字费
    has_taxs: 当月是否缴纳五险一金。[1] * 12 代表每月都需要缴纳; [0] * 6 + [1] * 6 代表前6个月不缴纳，后6个月缴纳
    special_deduction: 专项附加扣除
    '''
    assert len(monthly_incomes) == len(signature_fees) == len(has_taxs) == 12
    # 初始化累计应纳税所得额和累计已缴税款
    cumulative_taxable_income = 0
    cumulative_tax_paid = 0
    cumulative_income_after_tax = 0

    for month, monthly_income, signature_fee, has_tax in zip(range(1, 13), monthly_incomes, signature_fees, has_taxs):
        monthly_income = monthly_income + signature_fee
        if has_tax:
            wuxian_yijin = calculate_wuxian_yijin(monthly_income)
            monthly_taxable_income = monthly_income - 5000 - special_deduction - wuxian_yijin
        else:
            monthly_taxable_income = monthly_income - 5000 - special_deduction
        cumulative_taxable_income += monthly_taxable_income
        rate, quick_deduction = get_yearly_tax_rate(cumulative_taxable_income)
        cumulative_tax = cumulative_taxable_income * rate - quick_deduction
        monthly_tax = round(cumulative_tax - cumulative_tax_paid)
        monthly_income_after_tax = round(monthly_income - monthly_tax)
        print(f"第{month}月应缴纳的税款为：{monthly_tax}元，到手：{monthly_income_after_tax}元")
        cumulative_tax_paid += monthly_tax
        cumulative_income_after_tax += monthly_income_after_tax

    print(f"\n年度应缴纳的税款为：{cumulative_tax_paid}元，到手：{cumulative_income_after_tax}元\n")
    return cumulative_income_after_tax


def calculate_year_end_bonus(year_end_bonus: float):
    '''
    计算税后年终奖
    year_end_bonus: 税前年终奖
    '''
    if year_end_bonus == 0:
        return 0
    # 计算假定月收入
    monthly_income = year_end_bonus / 12
    # 获取适用税率和速算扣除数
    rate, quick_deduction = get_monthly_tax_rate(monthly_income)
    # 计算应纳税额
    tax = round(year_end_bonus * rate - quick_deduction)
    year_end_bonus_after_tax = round(year_end_bonus - tax)
    # 输出应缴纳的税款
    print(f"应缴纳的年终奖税款为：{tax}元，到手：{year_end_bonus_after_tax}元\n")
    return year_end_bonus_after_tax


def calculate_stock_income(stock_income: float):
    '''
    计算税后股票收入
    stock_income: 税前股票收入
    '''
    if stock_income == 0:
        return 0
    rate, quick_deduction = get_yearly_tax_rate(stock_income)
    stock_income_tax = round(stock_income * rate - quick_deduction)
    stock_income_after_tax = round(stock_income - stock_income_tax)
    print(f"应缴纳的股票税款为：{stock_income_tax}元，到手：{stock_income_after_tax}元\n")
    return stock_income_after_tax


if __name__ == '__main__':
    monthly_incomes = [32000] * 6 + [40000] * 6  # 代表前6个月每月税前3.2w，后6个月每月税前4w
    signature_fees = [0] * 6 + [50000] + [0] * 5  # 代表7月获得一笔5w签字费
    has_taxs = [0] * 6 + [1] * 6  # 代表前6个月不缴纳五险一金，后6个月缴纳
    year_end_bonus = 20_000  # 代表2w年终奖
    stock_income = 300_000  # 代表30w股票收入

    # 计算税后月薪
    cumulative_income_after_tax = calculate_cumulative_income(monthly_incomes, signature_fees, has_taxs)
    # 计算税后年终奖
    year_end_bonus_after_tax = calculate_year_end_bonus(year_end_bonus)
    # 计算税后股票收入
    stock_income_after_tax = calculate_stock_income(stock_income)

    all_income_after_tax = cumulative_income_after_tax + year_end_bonus_after_tax + stock_income_after_tax
    print(f"总计税后年薪：{cumulative_income_after_tax} + {year_end_bonus_after_tax} + {stock_income_after_tax} = {all_income_after_tax}")