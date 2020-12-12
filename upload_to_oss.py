import time
import sys
import oss2


def get_file_type(file_path):
    if file_path.endswith('jpg') or file_path.endswith('jpeg') or file_path.endswith('png') \
            or file_path.endswith('webp'):
        return 'pic'
    if file_path.endswith('md') or file_path.endswith('txt') or file_path.endswith('pages'):
        return 'document'
    if file_path.endswith('mp3'):
        return 'audio'
    if file_path.endswith('mp4') or file_path.endswith('avi') or file_path.endswith('mkv'):
        return 'video'
    if file_path.endswith('zip') or file_path.endswith('7z'):
        return 'com'
    return 'other'


def now():
    return time.strftime("%Y%m%d%H%M%S", time.localtime())


def get_file_name(file_path):
    return file_path[file_path.rindex('/') + 1:] if file_path.__contains__('/') else file_path


def gen_oss_file_name(file_path):
    return get_file_type(file_path) + '-' + now() + '-' + get_file_name(file_path)


file_path = sys.argv[1]

auth = oss2.Auth('<access_key_id>', '<access_key_secret>')
bucket = oss2.Bucket(auth, '<endpoint>', '<bucket_name>')

file = bucket.put_object_from_file(gen_oss_file_name(file_path), file_path)
print(file.resp.response.url)
