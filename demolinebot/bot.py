class Bot:

    def __init__(self, entry, lists, choice, result):
        """

        :param entry: 入口界面的json
        :param lists: 列表的json
        :param choice: 選擇畫面的json
        :param result: 選擇結果的json
        """
        self.entry = entry
        self.lists = lists
        self.choice = choice
        self.result = result

    def get_entry_json(self):
        return self.entry

    def get_lists_json(self):
        return self.lists

    def get_choice_json(self):
        return self.choice

    def get_result_json(self):
        return self.result

    def set_lists_theme(self, theme_list, next_button_name, next_button_action, page):
        """
        修改列表上的按鈕主題
        :param page: 列表頁數
        :param next_button_action: 按鈕按下回傳的文字
        :param next_button_name: 按鈕名稱(下一頁）
        :param theme_list: 存放每個主題的list
        """
        self.lists['body']['contents'][2]['contents'][0]['action']['text'] = theme_list[0]
        self.lists['body']['contents'][2]['contents'][0]['action']['label'] = theme_list[0]
        self.lists['body']['contents'][2]['contents'][1]['action']['text'] = theme_list[1]
        self.lists['body']['contents'][2]['contents'][1]['action']['label'] = theme_list[1]
        self.lists['body']['contents'][2]['contents'][2]['action']['text'] = theme_list[2]
        self.lists['body']['contents'][2]['contents'][2]['action']['label'] = theme_list[2]
        self.lists['body']['contents'][2]['contents'][3]['action']['text'] = theme_list[3]
        self.lists['body']['contents'][2]['contents'][3]['action']['label'] = theme_list[3]
        self.lists['body']['contents'][2]['contents'][4]['action']['text'] = theme_list[4]
        self.lists['body']['contents'][2]['contents'][4]['action']['label'] = theme_list[4]
        # 修改button theme
        self.lists['body']['contents'][2]['contents'][5]['action']['label'] = next_button_name  # 下一頁
        self.lists['body']['contents'][2]['contents'][5]['action']['text'] = next_button_action  # 主題列表 # 下一頁按鈕回傳

        self.lists['body']['contents'][4]['contents'][0]['text'] = '第' + str(page) + '頁'  # 修改頁數

    def set_choice(self, left_url, right_url, left_name, right_name, left_button_action, right_button_action):
        """
        修改選擇界面
        :param left_url: 左圖url
        :param right_url: 右圖url
        :param left_name: 左圖顯示的名稱
        :param right_name: 右圖顯示的名稱
        :param left_button_action: 左圖按鈕回傳的文字
        :param right_button_action: 右圖按鈕回傳的文字
        :return:
        """
        self.choice["header"]['contents'][0]['contents'][0]['url'] = left_url
        self.choice["header"]['contents'][0]['contents'][1]['url'] = right_url
        self.choice["body"]['contents'][0]['text'] = left_name
        self.choice["body"]['contents'][2]['text'] = right_name
        self.choice["footer"]['contents'][0]['action']['text'] = left_button_action
        self.choice["footer"]['contents'][1]['action']['text'] = right_button_action

    def set_result(self, url, description, button_action):
        """
        修改統計結果界面
        :param url: 圖片url
        :param description: 圖片下方的文字
        :param button_action: 顯示統計資訊按鈕回傳的文字(button_name_default:顯示統計結果)
        :return:
        """
        self.result["body"]['contents'][2]['contents'][0]['url'] = url
        self.result["body"]['contents'][2]['contents'][1]['text'] = description
        self.result["body"]['contents'][4]['contents'][0]['action']['text'] = button_action

