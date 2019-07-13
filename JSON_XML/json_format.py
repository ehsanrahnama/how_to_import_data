import json

# using json api library to serilization and deserilization 


file_path = '/home/rahi/pycode/how_to_import_data/JSON_XML/posts-100.json'
with open(file_path, 'r') as f:
    posts_json = json.load(f)


# DECODE
# load for file 
# loads, (s) stand for string 


print(type(posts_json))
print(len(posts_json))
print(type(posts_json[0]))

print(20*'--')

json_orginal = """
{
    "Id": 5, 
    "PostTypeId": "1",
    "CreationDate": "2014-05-13T23:58:30.457", 
    "Score": 9, 
    "ViewCount": 448, 
    "LastActivityDate":"2014-05-14T00:36:31.077", 
    "Title": "How can I do simple machine learning without hard-coding behavior?", 
    "Tags": "<machine-learning>",
    "AnswerCount": 1,
    "CommentCount": 1, 
    "FavoriteCount": 1, 
    "ClosedDate": "2014-05-14T14:40:25.950"
}
"""

json_loaded = json.loads(json_orginal)
print("TYPE JSON LOADED:",type(json_loaded))

print(json.dumps(json_loaded, indent=2))

print(20*'--')

# ENCODE
# dump for file 
# dumps, (s) stand for string

this_tuple = ('one', 'two')
this_list = ['one', 'two']

json_tuple = json.dumps(this_tuple)
json_list = json.dumps(this_list)

print(json_tuple)
print(json_list)
print(type(json_tuple))
print(type(json_list))
print(json_tuple == json_list)

print(type(json.loads(json_tuple)))
print(type(json.loads(json_list)))

