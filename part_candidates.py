import json

# Open passed in input file. 
with open('video_000000000000_keypoints.json') as input_file:

    # Load the JSON data from the input file into json_data. 
    json_data = json.load(input_file)

# We extract the part_canditates from json_data and assign it to a dictionary known as part_candidates.
part_candidates = json_data['part_candidates'][0]

print(type(part_candidates))

# This will be our official dictionary holding all of our necessary body parts and their associated values. 
part_candidates_dict = {}

# We assign all of the body parts that are accounted for in part_candidates and assign it to body_parts. 
body_parts = ["Nose",  "Neck", "RShoulder", "RElbow",  "RWrist", "LShoulder", "LElbow", "LWrist", "MidHip",  
"RHip","RKnee","RAnkle", "LHip", "LKnee", "LAnkle", "REye", "LEye", "REar", "LEar", "LBigToe","LSmallToe", "LHeel", "RBigToe", "RSmallToe", "RHeel"]

# We go through all 25 keys in part_candidates. 
for key in part_candidates:

    # Each key in part_candidates is a string 0-25, i.e '0'.
    # In order to access body_parts our index must be an integer.
    # We call the int function to turn our key into an integer and return the body_part associated with that index. 
    # E.g body_parts[0] is "Nose". 
    body_part = body_parts[int(key)]

    # Each key in part_candidates has a value, this value is actually a list containing all the values associated with a specific body part.
    # E.g part_candidates['0'] = [1215.12, 5.39515,0.0619309, 384.47, 67.0455, 0.477553, 261.123, 100.45, 0.195454].
    body_part_values = part_candidates[key]

    # The keys in our dict are the body parts in part_candidates. Each body part will have its own dictionary filled with keys and values.
    part_candidates_dict[body_part] = {}

    # This will keep track of what we need to concatenate to form our new key. E.g x1, y3, c4, etc.
    counter = 0

    # We go through all of our values in body_part_values.
    # We go in steps of 3, every 3 values is an x and y coordinant, and a detection confidence.
    for i in range(0, len(body_part_values), 3):

        # We assign an appropriate key to our body part, e.g x0.
        # Our key will be assigned a value, the value in index i in body_part_values is assigned to the current key (x-coordinant) to the current body part.
        # E.g part_candidates['Nose']['x0'] = 1215.12
        part_candidates_dict[body_part]['x' + str(counter)] = body_part_values[i]

        # Our key will be assigned a value, the value in index i + 1 in body_part_values is assigned to the current key (y-coordinant) to the current body part.
        # E.g part_candidates['Nose']['y0'] = 5.39515
        part_candidates_dict[body_part]['y' + str(counter)] = body_part_values[i + 1]

        # Our key will be assigned a value, the value in index i + 2 in body_part_values is assigned to the current key (detection confidance) to the current body part.
        # E.g part_candidates['Nose']['c0'] = 0.0619309
        part_candidates_dict[body_part]['c' + str(counter)] = body_part_values[i + 2]

        # We increment counter by one to keep track of what needs to be concatenated to x, y, and c.
        counter += 1

# We output a JSON string in pretty format of indentation 4.
print(json.dumps(part_candidates_dict, indent = 4))

print(part_candidates_dict['Nose']['x1'])

