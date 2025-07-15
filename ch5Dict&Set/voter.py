voter = {}
def check_voter(name):
    if voter.get(name):
        print("請你離開！")
    else:
        voter[name] = True
        print("請你投票！")
# check_voter("Tom")
# check_voter("Tom")

#Web process example : Throigh Hash table(cache) can reduce server loading
# cache = {}
# def get_page(url):
#     if cache.get(url):
#         return cache[url]
#     else:
#         data = get_data_from_server(url)
#         cache[url] = data
#         return data