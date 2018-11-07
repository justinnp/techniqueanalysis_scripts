import json

with open('IMG_1359_000000000000_keypoints.json') as json_data:
    data_dict = json.load(json_data)


parts_list = [
    "Nose",
    "Neck",
    "RShoulder",
    "RElbow",
    "RWrist",
    "LShoulder",
    "LElbow",
    "LWrist",
    "MidHip",
    "RHip",
    "RKnee",
    "RAnkle",
    "LHip",
    "LKnee",
    "LAnkle",
    "REye",
    "LEye",
    "REar",
    "LEar",
    "LBigToe",
    "LSmallToe",
    "LHeel",
    "RBigToe",
    "RSmallToe",
    "RHeel",
]


partcandidates_list = data_dict['part_candidates']
part_obj = partcandidates_list[0]

partData_dictionary = []
for item in part_obj.items():
    obj = {
            "part": parts_list[int(item[0])],
            "x": item[1][0],
            "y": item[1][1],
            "confidence": item[1][2] 
        }
    partData_dictionary.append(obj)

for obj in partData_dictionary:
    print(obj)



