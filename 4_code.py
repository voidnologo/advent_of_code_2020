import re


with open("4_data.txt", "r") as f:
    data = f.read().splitlines()


passports = []
e = ""
for line in data:
    if line != "":
        e += f"{line} "
    else:
        passports.append(e)
        e = ""


# == PART ONE ==========================================================

REQUIRED = set(("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"))
valid_count = 0
for passport in passports:
    parts = passport.split()
    keys = set((p.split(":")[0] for p in parts))
    if REQUIRED.issubset(keys):
        valid_count += 1

print(f"Part One: {valid_count}")


# == PART TWO ==========================================================


def validate_byr(byr):
    return (len(byr) == 4) and (1920 <= int(byr) <= 2002)


def validate_iyr(iyr):
    return (len(iyr) == 4) and (2010 <= int(iyr) <= 2020)


def validate_eyr(eyr):
    return (len(eyr) == 4) and (2020 <= int(eyr) <= 2030)


def validate_hgt(hgt):
    p = re.match(r"(\d+)(cm|in)", hgt)
    if not p:
        return False
    if p.group(2) == "cm":
        return 150 <= int(p.group(1)) <= 193
    elif p.group(2) == "in":
        return 59 <= int(p.group(1)) <= 76
    else:
        return False


def validate_hcl(hcl):
    p = re.match(r"#[0-9a-f]{6}$", hcl)
    return p is not None


def validate_ecl(ecl):
    VALID = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
    return ecl in VALID


def validate_pid(pid):
    p = re.match(r"[0-9]{9}$", pid)
    return p is not None


REQUIRED = set(("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"))
valid_count = 0
for passport in passports:
    parts = passport.split()
    vals = {p.split(":")[0]: p.split(":")[1] for p in parts}
    if not REQUIRED.issubset(set(vals.keys())):
        continue
    if all(
        (
            validate_byr(vals["byr"]),
            validate_iyr(vals["iyr"]),
            validate_eyr(vals["eyr"]),
            validate_hgt(vals["hgt"]),
            validate_hcl(vals["hcl"]),
            validate_ecl(vals["ecl"]),
            validate_pid(vals["pid"]),
        )
    ):
        valid_count += 1


print(f"Part Two: {valid_count}")
