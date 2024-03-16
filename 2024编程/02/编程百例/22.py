# 两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。有人向队员打听比赛的名单。
# a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。(巧用集合)

team_A = {'a', 'b', 'c'}  # 建立队伍甲
team_B = {'x', 'y', 'z'}  # 建立队伍乙

# 尝试组合
for a_opponent in team_B:
    for b_opponent in team_B - {a_opponent}:
        for c_opponent in team_B - {a_opponent, b_opponent}:
            # 检查是否满足条件
            if a_opponent != 'x' and c_opponent not in {'x', 'z'}:
                # 如果满足条件，输出
                print(f"甲队vs乙队: a vs {a_opponent}, b vs {b_opponent}, c vs {c_opponent}")
                # 离开循环
                break
