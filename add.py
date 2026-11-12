


data={}
def add_ketab(shenase:int, esm:str, gheymat:int, nevisande:str, safhe:int, mozo:str, radebandi:str ,zaban:str )->dict:
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
    data[shenase]=data{"name":esm,"mablagh":gheymat,"writer":nevisande,"page":safhe,"darbare":mozo, "dastebandi":radebandi,"language":zaban}
    print(data)