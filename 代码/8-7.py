def make_album(singer, album, num_songs=None):  
    """  
    创建一个描述音乐专辑的字典。  
  
    参数:  
    singer (str): 歌手的名字  
    album (str): 专辑名  
    num_songs (int, optional): 专辑包含的歌曲数，默认为None  
  
    返回:  
    dict: 包含歌手名字、专辑名和歌曲数的字典  
    """  
    album_info = {  
        'singer': singer,  
        'album': album  
    }  
    if num_songs is not None:  
        album_info['num_songs'] = num_songs  
    return album_info  
  
# 使用make_album()函数创建三个专辑字典  
album1 = make_album('The Beatles', 'Abbey Road')  
album2 = make_album('Queen', 'A Night at the Opera', 12)  
album3 = make_album('Prince', 'Purple Rain')  
  
# 打印每个专辑字典以核实信息  
print(album1)  
print(album2)  
print(album3)

输出：
{'singer': 'The Beatles', 'album': 'Abbey Road'}
{'singer': 'Queen', 'album': 'A Night at the Opera', 'num_songs': 12}
{'singer': 'Prince', 'album': 'Purple Rain'}

