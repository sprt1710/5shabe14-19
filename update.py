

data={}
data1={}
def taghir(shenase:int, esm:str, gheymat:int, nevisande:str, safhe:int, mozo:str, radebandi:str ,zaban:str )->dict:
    """_summary_

    Args:
        shenase (int): _description_
        esm (str): _description_
        gheymat (int): _description_
        nevisande (str): _description_
        safhe (int): _description_
        mozo (str): _description_
        radebandi (str): _description_
        zaban (str): _description_

    Returns:
        dict: _description_
    """
    global taghir
    data1[shenase]=data1{"name":esm,"mablagh":gheymat,"writer":nevisande,"page":safhe,"darbare":mozo, "dastebandi":radebandi,"language":zaban}
    data1.update(data)
    print(data1)