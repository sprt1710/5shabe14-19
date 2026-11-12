


data={}
def hazf_ketab(shenase:int, )->dict:
    """_summary_

    Args:
        shenase (int): شناسه محصول
        esm (str): نام کتاب
        gheymat (int): مبلغ
        nevisande (str): نویسنده
        safhe (int): تعداد صفحه
        mozo (str): موضوع
        radebandi(str): رده بندی
        zaban(str): زبان

    Returns:
        dict: _description_
    """
    global data
    if shenase in data:
        res=data.pop(shenase)
        print(res)
        print(data)
