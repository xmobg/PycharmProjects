songs = input().split()
n = int(input())
for i in range(n):
    line = input()
    parts = line.split(" * ")
    command = parts[0]
    if command == "Add Song":
        song_name = parts[1]
        if song_name not in songs:
            songs.append(song_name)
            print(f"{song_name} successfully added")
    elif command == "Delete Song":
            song_to_delete = int(parts[1])
            if song_to_delete <= len(songs):
                deleted_songs = []
                for j in range(song_to_delete):
                    removed = songs.pop(0)
                    deleted_songs.append(removed)
                print(f"{', '.join(deleted_songs)} deleted")
    elif command == "Shuffle Songs":
            index_one = int(parts[1])
            index_two = int(parts[2])
            if 0 <= index_one < len(songs) and 0 <= index_two < len(songs):
                songs[index_one], songs[index_two] = songs[index_two], songs[index_one]
                print(f"{songs[index_one]} is swapped with {songs[index_two]}")
    elif command == "Insert":
            song_name = parts[1]
            index = int(parts[2])
            if index < 0 or index >= len(songs):
                print("Index out of range")
            else:
                if song_name in songs:
                    print(f"Song is already in the playlist")
                else:
                    songs.insert(index, song_name)
                    print(f"{song_name} successfully inserted")
    elif command == "Sort":
            songs.sort(reverse=True)
    elif command == "Play":
            print("Songs to Play:")
            for song in songs:
                print(song)