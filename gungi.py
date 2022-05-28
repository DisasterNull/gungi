# 駒の設定
# [[種類, 筋, 段, 層, 黒軍と白軍, 状態]
KOMA_infos = []
KOMA_types = ["謀", "侍", "兵", "忍", "砲", "砦", "臥", "雛", "帥", "弓"]
KOMA_holds_player = [9, 3, 2, 2, 2, 1, 1, 1, 1, 1]
KOMA_holds_enemy = [9, 3, 2, 2, 2, 1, 1, 1, 1, 1]


# 初期陣形配置関数
class Operation:

    def __init__(self, infos, types, holds, turn):
        self.infos = infos
        self.types = types
        self.holds = holds
        self.turn = turn
        self.user_choice_tegoma = 11

    def choice_tegoma(self):
        i = 1
        for h, t in zip(self.holds, self.types):
            print("%d. %s × %d" % (i, t, h))
            i += 1
        self.user_choice_tegoma = int(input('駒 : '))
        self.holds[self.user_choice_tegoma - 1] -= 1

    def InitialPosition(self):
        user_choice_deploy = [9, 9]
        user_choice_deploy[0] = int(input("筋 : "))
        user_choice_deploy[1] = int(input("段 : "))
        user_choice_deploy[2] = int(input("層 : "))
        new_data = [self.user_choice_tegoma, user_choice_deploy[0],
                    user_choice_deploy[1], user_choice_deploy[2],  0, self.turn,
                    0]
        self.infos.append(new_data)


class Image:
    def __init__(self, infos, types, player_holds, enemy_holds,):
        self.infos = infos
        self.types = types
        self.player_holds = player_holds
        self.enemy_holds = enemy_holds

    def Print(self):
        print("白軍の手駒 : ", end="")
        if len(self.player_holds) != 0:
            for h, t in zip(self.player_holds, self.types):
                print("%s×%d " % (t, h), end="")
            print("")
        else:
            print("なし")
        print("　 9　8　7　6　5　4　3　2　1　")
        print("+-------------------------+")
        i = 0
        while i < 9:
            j = 0
            while j < 11:
                if j == 0:
                    print("|", end="")
                elif j == 10:
                    k = str(i+1)
                    print(" | " + k)
                else:
                    for infos in self.infos:
                        if i == infos[0]-1 and j == infos[1]:
                            if infos[4] == 0:
                                print(" " + self.types[infos[0]-1], end="")
                            else:
                                print("v" + self.types[infos[0]-1], end="")
                        else:
                            print(" ・", end="")
                j += 1
            i += 1
        print("+-------------------------+")
        print("黒軍の手駒 : ", end="")
        if len(self.enemy_holds) != 0:
            for h, t in zip(self.enemy_holds, self.types):
                print("%s×%d " % (t, h), end="")
            print("")
        else:
            print("なし")


player = Operation(KOMA_infos, KOMA_types, KOMA_holds_player, 0)
player.choice_tegoma()
player.InitialPosition()
game = Image(KOMA_infos, KOMA_types, KOMA_holds_player, KOMA_holds_enemy)
game.Print()
