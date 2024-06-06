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
  
# 初始化一个标志变量，用于控制循环  
keep_going = 'y'  
  
while keep_going.lower() == 'y':  
    singer = input("请输入歌手的名字: ")  
    album = input("请输入专辑的名称: ")  
      
    # 询问用户是否要输入歌曲数
    num_songs_input = input("要输入专辑的歌曲数吗？(y/n): ")  
    if num_songs_input.lower() == 'y':  
        num_songs = int(input("请输入专辑的歌曲数: "))  
        album_info = make_album(singer, album, num_songs)  
    else:  
        album_info = make_album(singer, album)  
      
    # 打印创建的专辑字典  
    print(album_info)  
      
    # 询问用户是否继续  
    keep_going = input("是否继续输入专辑信息？(y/n): ")  
  
print("感谢使用，程序已退出。")
