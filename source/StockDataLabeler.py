import pandas as pd

def GetBankuai(input: pd.Series) -> pd.Series:
    bankuaiDct = {
        "电子":"TMT",
        "传媒":"TMT",
        "计算机":"TMT",
        "通信":"TMT",
        "传媒(SW港股)":"TMT",
        "电子(SW港股)":"TMT",
        "通信(SW港股)":"TMT",
        "计算机(SW港股)":"TMT",
        "机械设备":"制造",
        "国防军工":"制造",
        "电气设备":"制造",
        "公用事业":"制造",
        "综合":"制造",
        "交通运输":"制造",
        "电气设备(SW港股)":"制造",
        "交通运输(SW港股)":"制造",
        "公用事业(SW港股)":"制造",
        "机械设备(SW港股)":"制造",
        "综合(SW港股)":"制造",
        "国防军工(SW港股)":"制造",
        "医药生物":"医药",
        "医药生物(SW港股)":"医药",
        "化工":"周期",
        "建筑装饰":"周期",
        "有色金属":"周期",
        "建筑材料":"周期",
        "钢铁":"周期",
        "采掘":"周期",
        "有色金属(SW港股)":"周期",
        "建筑材料(SW港股)":"周期",
        "采掘(SW港股)":"周期",
        "建筑装饰(SW港股)":"周期",
        "钢铁(SW港股)":"周期",
        "化工(SW港股)":"周期",
        "食品饮料":"消费",
        "休闲服务":"消费",
        "家用电器":"消费",
        "轻工制造":"消费",
        "纺织服装":"消费",
        "汽车":"消费",
        "农林牧渔":"消费",
        "商业贸易":"消费",
        "汽车(SW港股)":"消费",
        "纺织服装(SW港股)":"消费",
        "休闲服务(SW港股)":"消费",
        "食品饮料(SW港股)":"消费",
        "家用电器(SW港股)":"消费",
        "轻工制造(SW港股)":"消费",
        "商业贸易(SW港股)":"消费",
        "银行":"金融地产",
        "非银金融":"金融地产",
        "房地产":"金融地产",
        "非银金融(SW港股)":"金融地产",
        "房地产(SW港股)":"金融地产",
        "银行(SW港股)":"金融地产"
    }
    ls = []

    print(f"数据总长度为{len(input)}")
    for n in input:
        #print(f"当前数据为：{n}")
        if n in bankuaiDct:
            #print(f"{n} 可以被归类")
            ls.append(bankuaiDct[n])
        else:
            #print(f"{n} 不能被归类")
            ls.append("#NoData!")
    #print(ls)
    ss = pd.Series(ls)
    return ss

def LabelDFrame(input: pd.DataFrame) -> pd.DataFrame:
    ss = GetBankuai(input["申万行业"])
    #print(ss)
    input["申万板块"] = ss.values

    print(input)
    return input