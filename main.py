import arrr
from pyscript import document
global specsin
specsin = []
def Submit(event):
    if document.querySelector("#boy").checked:
        specsin.append("boy")
    if document.querySelector("#glasses").checked:
        specsin.append("glasses")
    if document.querySelector("#ng").checked:
        specsin.append("noglasses")
    if document.querySelector("#girl").checked:
        specsin.append("girl")
    if document.querySelector("#short").checked:
        specsin.append("short")  
    if document.querySelector("#avg").checked:
        specsin.append("avg")  
    if document.querySelector("#tall").checked:
        specsin.append("tall")  
    if document.querySelector("#music").checked:
        specsin.append("music")  
    if document.querySelector("#sports").checked:
        specsin.append("sports")  
    if document.querySelector("#nerd").checked:
        specsin.append("nerd")  
    if document.querySelector("#introvert").checked:
        specsin.append("introvert")  
    if document.querySelector("#extrovert").checked:
        specsin.append("extrovert")  
    if document.querySelector("#ambivert").checked:
        specsin.append("ambivert")  
    if document.querySelector("#polite").checked:
        specsin.append("polite")  
    if document.querySelector("#stirfeet").checked:
        specsin.append("stirfeet")  
    if document.querySelector("#shorthair").checked:
        specsin.append("shorthair")  
    if document.querySelector("#longhair").checked:
        specsin.append("longhair")  
    if document.querySelector("#rich").checked:
        specsin.append("rich")  
    if document.querySelector("#braces").checked:
        specsin.append("braces")  
    if !(document.querySelector("#stirfeet") and !(document.querySelector("#polite").checked):
        specsin.append("boy")
        specsin.append("girl")
    """ info={
        "boy" : document.querySelector("#boy").checked,
        "girl" : document.querySelector("#girl").checked,
        "glasses" : document.querySelector("#glasses").checked,
        "noglasses" : document.querySelector("#ng").checked,
        "short" : document.querySelector("#short").checked,
        "avg" : document.querySelector("#avg").checked,
        "tall" : document.querySelector("#tall").checked,
        "music" : document.querySelector("#music").checked,
        "sports" : document.querySelector("#sports").checked,
        "nerd" : document.querySelector("#nerd").checked,
        "introvert" : document.querySelector("#introvert").checked,
        "friendly" : document.querySelector("#friendly").checked,
        "stirfeet" : document.querySelector("#stirfeet").checked,
        "shorthair" : document.querySelector("#shorthair").checked,
        "longhair" : document.querySelector("#longhair").checked,
        "rich" : document.querySelector("#rich").checked,
        "braces" : document.querySelector("#braces").checked,
"profane" : document.querySelector("#profane").checked
    }
     """
    #for i in info.values():
     #   document.write(info.values)
       # if i == "true":
      #      specsin.append(info.get(i))
            
        ##   pass
    
    specs={
    "boy":["กฤตติ์ธามม์","กิตติพัศ","คีญ","เจณณวัฒน์","ชยุต","ญาณวุฒิ","ณพุทธ","ธนภัทร","ธีรวิษณุ์","บวรรัช","พงศภัค","พิชญภูมิ","ภทรธร","พาพัฒน์"
,"ธนดล","ธนวัสส์","ธนากฤต","บารเมษฐ์","เป็นขลุ่ย","ปภังกร(ปุณณ์)","พศิน","พาทิศ","พิชชากร","ภูมิพัฒน์","ภูริพงษ์","เมืองเอก","วิชศกร","อนุรุทธ์"
,"กันตภณ","ชยพล","บรรณสรณ์","ปภังกร(เอเจ)","พัทธดนย์","วสุ","ศุภกฤต","ศุวสิทธิ์","อชิรวิชญ์","อภิพัชร","สุรพิชญ์","นรวิชญ์"
,"ชวิชฌ์","ชินทัต","ณกร","แทนพงศ์","ไทธัญ","ธีทัต","ธีรพัฒน์","วริทธิ์นันท์","วสุ(เพนท์)","วัชรวิชย์","ศิริพงษ์","หฤษฏ","อิงธรรม"],

    "girl":["ณญากร","ณภัทร","ณัชชา(พันช์)","ณัฐปภัสร์","ณิชณัชทฐ์","ปัญญาภรณ์","พิชชาภา","ภคมน","เมืองพลอย","สิรภัทร","สิริลภัส","พาพัฒน์"
,"จิรัชญา","ชนาภา","ญาดา","ณิชชา","ทิตชญา","ธรณ์ธันย์","นิยารินทร์","พิชชานันท์","อรภิชา","ศศิณัฎฐ์","สิรินทร์"
,"กรฬษ","ฉันชนก","ฐิติวรดา","ณภัสณดา","ปัณณ์รวี","ปาริฉัตร","พรรษชล","ภรีม","เมธาพร","เมืองเพชร","สาริศา","อธิชา","ณัฐชา","ดังฝัน"
,"ชนมน","เฌอลิณญ์","ณพิชญา","ณัชชา(จีจ้า)","ณัฐรินีย์","ปุญญาภา","พรนัชชา","พรสุดา","พัทธวรรณ","รัชญ์สิภา","วาริพิณฑุ์","วิภาดา"],

    "noglasses":["กฤตติ์ธามม์","ชยุต","ญาณวุฒิ","ณพุทธ","พงศภัค","พาพัฒน์","ณญากร","ณิชณัชทฐ์","ปัญญาภรณ์","พิชชาภา","ภคมน","เมืองพลอย","สิรภัทร","สิริลภัส"
,"จิรัชญา","ชนาภา","ญาดา","ณิชชา","ธนดล","ธนวัสส์","ธนากฤต","ธรณ์ธันย์","นิยารินทร์","บารเมษฐ์","ปภังกร(ปุณณ์)","พศิน","พาทิศ","พิชชากร","พิชชานันท์","ภูมิพัฒน์","ภูริพงษ์","วิชศกร","สิรินทร์","ศศิณัฎฐ์","อรภิชา"
,"กรฬษ","กันตภณ","ฉันชนก","ฐิติวรดา","ณภัสณดา","บรรณสรณ์","ปาริฉัตร","พรรษชล","ภรีม","เมธาพร","เมืองเพชร","วสุ","ศุภกฤต","ศุวสิทธิ์","อภิพัชร","อธิชา","อชิรวิชญ์","สุรพิชญ์","นรวิชญ์","ดังฝัน"
,"ชนมน","ชวิชฌ์","ชินทัต","เฌอลิณญ์","ณกร","ณพิชญา","ณัฐรินีย์","แทนพงศ์","ไทธัญ","ธีทัต","ปุญญาภา","พรสุดา","พัทธวรรณ","รัชญ์สิภา","วริทธิ์นันท์","วัชรวิชย์","วาริพิณฑุ์","ศิริพงษ์","อิงธรรม"],

    "glasses" : ["กิตติพัศ","คีญ","เจณณวัฒน์","ณภัทร","ณัชชา(พันช์)","ณัฐปภัสร์","ธนภัทร","ธีรวิษณุ์","บวรรัช","พิชญภูมิ","ภทรธร","ภัทรพร",
"ทิตชญา","เป็นขลุ่ย","เมืองเอก","อนุรุทธ์"
,"ชยพล","ปภังกร","พัทธดนย์","อชิรวิชญ์","สุรพิชญ์","ณัฐชา"
,"ญาธิป","ณัชชา(จีจ้า)","วสุ(เพนท์)","หฤษฏ","วิภาดา","พรนัชชา"],

    "short" : ["กิตติพัศ","ธนภัทร","ธีรวิษณุ์","ภคมน","สิริลภัส",
"ธนดล","ธนากฤต","ธรณ์ธันย์","ภูริพงษ์","ภูมิพัฒน์",
"บรรณสรณ์","ปาริฉัตร","เมธาพร","วสุ","อภิพัชร","สุรพิชญ์","นรวิชญ์"
,"ชนมน","ธีรพัฒน์","พรสุดา","พัทธวรรณ"],

    "avg" : ["คีญ","เจณณวัฒน์","ชยุต","ณญากร","ณพุทธ","ณัฐปภัสร์","ณิชณัชทฐ์","บวรรัช","ปัญญาภรณ์","พิชชาภา","ภัทรพร ","เมืองพลอย"
,"จิรัชญา","ชนาภา","ญาดา","ณิชชา","ทิตชญา","ธนวัสส์","ธยาน์","นิยารินทร์","บารเมษฐ์","เป็นขลุ่ย","อรภิชา","สิรินทร์","พาทิศ","พิชชากร","พิชชานันท์","วิชศกร"
,"ชยพล","ปัณณ์รวี","พรรษชล","ศุวสิทธิ์","อชิรวิชญ์","ดังฝัน","ณภัสณดา","เมืองเพชร"
,"ชวิชฌ์","ชินทัต","เฌอลิณญ์","ญาธิป","ณพิชญา","ณัฐรินีย์","ไทธัญ","ธีทัต","ปุญญาภา","พรนัชชา","รัชญ์สิภา","วริทธิ์นันท์","วัชรวิชย์","วาริพิณฑุ์","วิภาดา","ศิริพงษ์","อิงธรรม"],

    "tall" : ["กฤตติ์ธามม์","ญาณวุฒิ","พงศภัค","ภทรธร","สิรภัทร","พาพัฒน์","พิชญภูมิ"
"ปภังกร(ปุณณ์)","พศิน","อนุรุทธ์"
,"กันตภณ","กรฬษ","ปภังกร(เอเจ)","ภรีม","ศุภกฤต","สาริศา","อธิชา","ณัฐชา","ดังฝัน"
,"ณกร","ณัชชา","แทนพงศ์","วริทธิ์นันท์","หฤษฏ"],

    "sports" : ["กฤตติ์ธามม์","เจณณวัฒน์","ญาณวุฒิ","ธีรวิษณุ์","ปัญญาภรณ์","พงศภัค","พิชชาภา","พิชญภูมิ","ภคมน","เมืองพลอย","สิรภัทร","สิริลภัส","ณพุทธ","พาพัฒน์"
,"จิรัชญา","ชนาภา","ทิตชญา","ธนดล","ธนวัสส์","ธรณ์ธันย์","เป็นขลุ่ย","พาทิศ","พิชชากร","เมืองเอก","วิชศกร","อรภิชา","ศศิณัฎฐ์","อนุรุทธ์"
,"กันตภณ","ภรีม","ศุภกฤต","เมืองเพชร","อธิชา","อชิรวิชญ์"
,"ชินทัต","ณัฐรินีย์","แทนพงศ์","หฤษฏ","ศิริพงษ์"],

    "nerd" : ["กิตติพัศ","คีญ","ณพุทธ","ดังฝัน","กันตภณ"],
    "music" : ["ณิชณัชทฐ์","พิชญภูมิ","พาพัฒน์","สิริลภัส","คีญ","ณพุทธ"
,"ชนาภา","ธนากฤต","ธรณ์ธันย์"
,"ณภัสณดา","ณัฐชา","ดังฝัน"
,"วสุ(เพนท์)","แทนพงศ์","ชวิชฌ์"],

    "polite":["ณญากร","คีญ","ณัชชา","ณัฐปภัสร์"
,"สิรินทร์","พิชชานันท์"
,"พรรษชล","อภิพัชร"
,"พัทธวรรณ","","","","","","","","","","","","","",""],
    "introvert" : ["ณญากร","บวรรัช","ภทรธร","สิรภัทร","ณิชณัชทฐ์"
,"ญาดา","ทิตชญา","นิยารินทร์","ธยาน์","พิชชานันท์"
,"อภิพัชร","ณัฐชา","สาริศา","ฉันชนก"
,"","","","","","","","","","","","","","",""],

    "ambivert":["กฤตติ์ธามม์","กิตติพัศ","คีญ","เจณณวัฒน์","ชยุต","ญาณวุฒิ","ณพุทธ","ภัทรพร","ณัชชา","เมืองพลอย","พิชชาภา"
,"ธนดล","ธนวัสส์","ธนากฤต","ธรณ์ธันย์","ปภังกร(ปุณณ์)","พศิน","พาทิศ","พิชชากร","ภูมิพัฒน์","ภูริพงษ์","เมืองเอก","วิชศกร","อรภิชา","สิรินทร์"
,"ชยพล","ณภัสณดา","บรรณสรณ์","ปัณณ์รวี","ปาริฉัตร","เมืองเพชร","วสุ","ศุวสิทธิ์","สาริศา","นรวิชญ์","ปภังกร(เอเจ)","อธิชา"
,"","","","","","","","","","","","","","",""],

    "extrovert" : ["ณภัทร","ณัฐปภัสร์","ธีรวิษณุ์","ปัญญาภรณ์","พงศภัค","พิชญภูมิ","ภคมน","ธนภัทร","พาพัฒน์"
,"จิรัชญา","ชนาภา","ณิชชา","บารเมษฐ์","เป็นขลุ่ย","อนุรุทธ์","ศศิณัฎฐ์"
"กันตภณ","ฐิติวรดา","ปัณณ์รวี","พรรษชล","เมืองเพชร","ภรีม","ดังฝัน","สุรพิชญ์"
,"","","","","","","","","","","","","","",""],

    "stirfeet" : ["กิตติพัศ","ธนภัทร","ธีรวิษณุ์","พิชญภูมิ","ณพุทธ","ชยุต","พาพัฒน์"
,"ธนากฤต","บารเมษฐ์","เป็นขลุ่ย","อนุรุทธ์","ศศิณัฎฐ์"],
    "rich"  :["กฤตติ์ธามม์","ณพุทธ","ณิชณัชทฐ์","ปัญญาภรณ์"
,"พิชชากร","ณิชชา","จิรัชญา",
"กันตภณ","ฐิติวรดา","ภรีม"],
    "braces":["เจณณวัฒน์","ธีรวิษณุ์","พิชญภูมิ","ภคมน"
,"ธนดล","เป็นขลุ่ย","อนุรุทธ์","อรภิชา",
"ฉันชนก","ปภังกร(เอเจ)","อชิรวิชญ์"],
    "shorthair":["กฤตติ์ธามม์","กิตติพัศ","คีญ","เจณณวัฒน์","ชยุต","ญาณวุฒิ","ณพุทธ","ธนภัทร","ธีรวิษณุ์","บวรรัช","พงศภัค","พิชญภูมิ","ภทรธร","พาพัฒน์"
,"ธนดล","ธนวัสส์","ธนากฤต","บารเมษฐ์","เป็นขลุ่ย","ปภังกร(ปุณณ์)","พศิน","พาทิศ","พิชชากร","ภูมิพัฒน์","ภูริพงษ์","เมืองเอก","วิชศกร","อนุรุทธ์","ธรณ์ธันย์","อรภิชา","ศศิณัฎฐ์","ทิตชญา"
,"กันตภณ","ชยพล","บรรณสรณ์","ปภังกร(เอเจ)","พัทธดนย์","วสุ","ศุภกฤต","ศุวสิทธิ์","อชิรวิชญ์","อภิพัชร","สุรพิชญ์","นรวิชญ์"],
    "longhair":["ณญากร","ณภัทร","ณัชชา(พันช์)","ณัฐปภัสร์","ณิชณัชทฐ์","ปัญญาภรณ์","พิชชาภา","ภคมน","ภัทรพร ","เมืองพลอย","สิรภัทร","สิริลภัส",
"จิรัชญา","ชนาภา","ญาดา","ณิชชา","นิยารินทร์","พิชชานันท์","อรภิชา","สิรินทร์"
,"กรฬษ","ฉันชนก","ฐิติวรดา","ณภัสณดา","ปัณณ์รวี","ปาริฉัตร","พรรษชล","ภรีม","เมธาพร","เมืองเพชร","สาริศา","อธิชา","ณัฐชา","ดังฝัน"]

    }
    output = document.querySelector("#output")
    log = document.querySelector("#log")

    list=[]
    for i in specsin:
        list.append(specs.get(i))

   
    try:
        res = set(list[0]).intersection(*map(set, list[1:]))
        #res = set(list[0]).intersection(set(list[1]))
        resfin = "จากสเปคแล้วคุณเหมาะกับ : "+" , ".join(res)
    except:
        resfin = "ไม่พบคนตามสเปค"
  
    
    print("จากสเปคแล้วคุณเหมาะกับ : "+" , ".join(res))
    
    
   
    output.innerText = resfin