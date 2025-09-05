cutoffs = [
    ("Pilani", "Chemical", 247),
    ("Pilani", "Civil", 238),
    ("Pilani", "EEE", 292),
    ("Pilani", "Mech", 266),
    ("Pilani", "CS", 327),
    ("Pilani", "E&I", 282),
    ("Pilani", "ECE", 314),
    ("Pilani", "Manufacturing", 243),
    ("Pilani", "Math & Computing", 318),
    ("Pilani", "Pharm", 165),
    ("Pilani", "MSc Bio", 236),
    ("Pilani", "MSc Chem", 241),
    ("Pilani", "MSc Eco", 271),
    ("Pilani", "MSc Math", 256),
    ("Pilani", "MSc Physics", 254),

    ("Goa", "Chemical", 239),
    ("Goa", "EEE", 278),
    ("Goa", "Mech", 254),
    ("Goa", "CS", 301),
    ("Goa", "E&I", 270),
    ("Goa", "ECE", 287),
    ("Goa", "Math & Computing", 295),
    ("Goa", "MSc Bio", 234),
    ("Goa", "MSc Chem", 236),
    ("Goa", "MSc Eco", 263),
    ("Goa", "MSc Math", 249),
    ("Goa", "MSc Physics", 248),

    ("Hyd", "Chemical", 238),
    ("Hyd", "Civil", 235),
    ("Hyd", "EEE", 275),
    ("Hyd", "Mech", 251),
    ("Hyd", "CS", 298),
    ("Hyd", "E&I", 270),
    ("Hyd", "ECE", 284),
    ("Hyd", "Math & Computing", 293),
    ("Hyd", "Pharm", 161),
    ("Hyd", "MSc Bio", 234),
    ("Hyd", "MSc Chem", 235),
    ("Hyd", "MSc Eco", 261),
    ("Hyd", "MSc Math", 247),
    ("Hyd", "MSc Physics", 245)
]


#For extractig the above data , i copied the data from website to chatgptr and asked it to make it into dict. SOrry but i didnt know how to extract it , i could do manually but its the same thing. I domt know if we were supposed to do it with code (logic/alogrithm) as it wasnt mentioned.
# dict = {}
dict = { "Pilani" : {}, "Goa" : {}, "Hyderabad":{}} # Making dict of dicts then first dealing with each dict (pilani , goa, huderabad) and then at last putting them at their place in "dict"
Pilani  = {}
Goa = {}
Hyderabad = {}
for i in range(len(cutoffs)):
    if cutoffs[i][0] == "Pilani":
        Pilani[cutoffs[i][1]] = cutoffs[i][2]
    elif cutoffs[i][0] == "Goa":
        Goa[cutoffs[i][1]] = cutoffs[i][2]
    else:
        Hyderabad[cutoffs[i][1]] = cutoffs[i][2]
    
dict["Pilani"] = Pilani
dict["Goa"] = Goa
dict["Hyderabad"] = Hyderabad

dict
