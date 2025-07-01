
# def run_timing():
#     total_time = 0.0
#     num_of_runs = 0
#     while True:
#         run_time = input("輸入跑 10 公里的時間:")
#         if run_time == '':
#             break
#         try:
#             run_time_value = float(run_time)
#             total_time+= run_time_value
#             num_of_runs+=1
#         except Exception as e: # 如果資料轉換有問題，會攔截錯誤資訊並印出來
#             print("產生錯誤:", e)
#     if num_of_runs > 0:
#         avg_time = (total_time/num_of_runs)
#     else:
#         avg_time = 0.0
#     print("跑",num_of_runs,"次的平均時間為：",avg_time)

# run_timing()

#while True的終止條件沒有寫好，可能真的會無法跳出loop，指派式運算式可以解決

def run_time2():
    total_time = 0.0
    nums_of_run = 0
    # 指派式運算式可以解決，直接指派值給予變數
    while run_time:=input("輸入跑 10 公里的時間:(直接按Enter可以結束輸入)"):
        try:
            run_time_value = float(run_time)
            total_time+= run_time_value
            nums_of_run+=1
        except Exception as e:
            print("產生錯誤:", e)
    if nums_of_run > 0:
        avg_time = (total_time/nums_of_run)
    else:
        avg_time = 0.0
    print("跑",nums_of_run,"次的平均時間為：",avg_time)
run_time2()

        