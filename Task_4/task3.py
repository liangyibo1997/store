Friuts = {
    "苹果": 12.3,
    "草莓": 4.5,
    "香蕉": 6.3,
    "葡萄": 5.8,
    "橘子": 6.4,
    "樱桃": 15.8
}
info = {
    "小明": {
        "fruits": {"苹果": 4, "草莓": 13, "香蕉": 10}
    },
    "小刚": {
        "fruits": {"葡萄": 19, "橘子": 12, "樱桃": 30}
    }
}
info["小明"]["money"] = info["小明"]["fruits"]["苹果"] * Friuts["苹果"] + info["小明"]["fruits"]["草莓"] * Friuts["草莓"] + \
                      info["小明"]["fruits"]["香蕉"] * Friuts["香蕉"]
info["小刚"]["money"] = info["小刚"]["fruits"]["葡萄"] * Friuts["葡萄"] + info["小刚"]["fruits"]["橘子"] * Friuts["橘子"] + \
                      info["小刚"]["fruits"]["樱桃"] * Friuts["樱桃"]
print(info)
