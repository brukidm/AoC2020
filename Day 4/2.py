import string

with open(r"input") as f:
    lines = f.read().split('\n')
    required_keys = {
        "byr", 
        "iyr",
        "eyr", 
        "hgt",
        "hcl",
        "ecl",
        "pid",
    }
    total = 0
    keys = []
    for line in lines:
        if line == "":
            result = all(key in keys for key in required_keys)
            if result:
                print(f"Valid: {keys}")
                total += 1
            keys = []
            valid = True
            continue
        fields = line.split(" ")
        for field in fields:
            key = field.split(":")[0]
            value = field.split(":")[1]
            if key == "byr":
                if int(value) >= 1920 and int(value) <= 2002:
                    keys.append(key)
            elif key == "iyr":
                if int(value) >= 2010 and int(value) <= 2020:
                    keys.append(key)
            elif key == "eyr":
                if int(value) >= 2020 and int(value) <= 2030:
                    keys.append(key)
            elif key == "hgt":
                if "cm" in value:
                    if int(value[:-2]) >= 150 and int(value[:-2]) <= 193:
                        keys.append(key)
                if "in" in value:
                    if int(value[:-2]) >= 59 and int(value[:-2]) <= 76:
                        keys.append(key)
            elif key == "hcl":
                if value.startswith("#") and all(c in string.hexdigits for c in value[1:]):
                    keys.append(key)
            elif key == "ecl":
                if value in ("amb", "blu", "brn", "gry","grn","hzl","oth"):
                    keys.append(key)
            elif key == "pid":
                if len(value) == 9 and value.isdigit():
                    keys.append(key)
    print(total)
