def countMatches(items : list[list[str]], ruleKey : str, ruleValue : str) -> int:

    matches = 0

    for i in items:
        if ruleKey == 'type' and ruleValue == i[0]:
            matches += 1
        if ruleKey == 'color' and ruleValue == i[1]:
            matches += 1
        if ruleKey == 'name' and ruleValue == i[2]:
            matches += 1

    return matches

def main():
    print(countMatches(items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], ruleKey = "color", ruleValue = "silver"))
    print(countMatches(items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]], ruleKey = "type", ruleValue = "phone"))

if __name__ == "__main__":
    main()