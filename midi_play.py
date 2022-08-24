import mido


# name is midi's name, key_change is up/down the key
# name 是 midi 文件名, key_change升降调的大小，0为原调
def print_mid_array(name, key_change):
    mid = mido.MidiFile(name + ".mid")
    for i, track in enumerate(mid.tracks):
        frequency_list = []
        time_list = []
        for msg in track:
            # print(msg)
            if msg.type == 'note_on':
                frequency_tmp = 440 * 2 ** ((msg.note - 69 + key_change * 12) / 12)
                frequency_list.append(round(frequency_tmp))
                time_list.append(msg.time)
            elif msg.type == 'note_off':
                time_list.append(msg.time)
        time_list.append(1)
        mid_table = [frequency_list[0:len(frequency_list)], time_list[1:len(time_list)+1:2], time_list[2:len(time_list)+1:2]]

        print("number = " + str(len(mid_table[0])))

        print("frequency = {", end="")
        print(*mid_table[0], sep=",", end="")
        print("},")
        # print(len(mid_table[0]))

        print("time_on = {", end="")
        print(*mid_table[1], sep=",", end="")
        print("},")
        # print(len(mid_table[1]))

        print("time_off = {", end="")
        print(*mid_table[2], sep=",", end="")
        print("}")
        # print(len(mid_table[2]))

        print("Arduino code: (just copy the end line)(直接复制最后一行到Arduino)")
        print("const int " + name + "[] = {", end="")
        print(len(mid_table[0]), end=",")
        print(*mid_table[0], sep=",", end=",")
        print(*mid_table[1], sep=",", end=",")
        print(*mid_table[2], sep=",", end="")
        print("};")


if __name__ == '__main__':
    print_mid_array("sakura", -1)
