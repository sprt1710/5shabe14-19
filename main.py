

from add import *

from hazf import hazf_ketab
from update import *

from hazf import *

data={}

while True:
    menu_ketab=input("1.add  2.edit 3.hazf 4.exit: ")
    while True:
        match menu_ketab:
            case "1":
                product=int(input("shenase mahsool ra vared kon: "))
                name_ketab=input("name ketab chie?:")
                price_ketab=int(input("gheymate ketab chande?: "))
                nevisande_ketab=input("nevisande kist?: ")
                page_ketab=int(input("ketab chand safhe ast?: "))
                mozo_ketab=input("mozo chie?: ")
                radebandi_ketab=input("ketab baraye kiast?: ")
                zaban_ketab=input("ketab be che zabanie?: ")
                add_ketab(shenase=product,esm=name_ketab,gheymat=price_ketab,nevisande=nevisande_ketab,safhe=page_ketab,mozo=mozo_ketab,radebandi=radebandi_ketab,zaban=zaban_ketab)
                continue

        match menu_ketab:
            case "2":
                product=int(input("shenase mahsool ra vared kon: "))
                name_ketab=input("name ketab chie?:")
                price_ketab=int(input("gheymate ketab chande?: "))
                nevisande_ketab=input("nevisande kist?: ")                    
                page_ketab=int(input("ketab chand safhe ast?: "))
                mozo_ketab=input("mozo chie?: ")
                radebandi_ketab=input("ketab baraye kiast?: ")
                zaban_ketab=input("ketab be che zabanie?: ")
                add_ketab(shenase=product,esm=name_ketab,gheymat=price_ketab,nevisande=nevisande_ketab,safhe=page_ketab,mozo=mozo_ketab,radebandi=radebandi_ketab,zaban=zaban_ketab)
                break
                print(data)
                continue

            case "3":
                product_id=int(input("shenase kalayi ke hazf beshe ro bezan:"))
                print(data)
                continue

            case "4":
                product_id_ketab=int(input("shenase mahsool baraye hazf:"))
                hazf_ketab(product_id)
                break

                

                
            





