def get_file_extension(str):
  return str[str.rfind('.')+1 : ]

def solution(S):
    music_ext_list = ['mp3', 'aac', 'flac']
    image_ext_list = ['jpg', 'bmp', 'gif']
    movie_ext_list = ['mp4', 'avi', 'mkv']
    # music_ext_arr = ['mp3', 'aac', 'flac']

    file_name_list = []
    file_size_list = []
    for row in S.split('\n'):
        temp = row.split(' ')
        file_name_list.append(temp[0])
        file_size_list.append(temp[1].replace('b', ''))

    temp_dict = {'music': 0, 'images': 0, 'movies': 0, 'other': 0}
    for i in range(len(file_name_list)):
        file_ext = get_file_extension(file_name_list[i])
        print(file_ext, file_size_list[i])
        if file_ext in music_ext_list:
            temp_dict['music'] += int(file_size_list[i])
        elif file_ext in image_ext_list:
            temp_dict['images'] += int(file_size_list[i])
        elif file_ext in movie_ext_list:
            temp_dict['movies'] += int(file_size_list[i])
        else:
            temp_dict['other'] += int(file_size_list[i])

    result = []
    for key, value in temp_dict.items():
        result.append(key + ' ' + str(value) + 'b')
    return '\n'.join(result)

solution('my.song.mp3 11b\ngreatSong.flac 1000b\nnot3.txt 5b\nvideo.mp4 200b\ngame.exe 100b\nmov!e.mkv 10000b')