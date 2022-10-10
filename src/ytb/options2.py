import json


with open("src/ytb/yt-dlp-options4.json", "r", encoding="utf-8") as f:
    count_dict = json.load(f)

with open("src/ytb/yt-dlp-options5.json", "r", encoding="utf-8") as f:
    start_dict = json.load(f)

new_dict = {}

for ind, (key, value) in enumerate(start_dict.items()):
    new_dict[key] = value
    for value in count_dict.values():
        if value["dest"] == key:
            new_dict[key]["search_count"] = value["search_count"]
            break

with open("src/ytb/yt-dlp-options2.json", "w", encoding="utf-8") as f:
    json.dump(new_dict, f, indent=4)
