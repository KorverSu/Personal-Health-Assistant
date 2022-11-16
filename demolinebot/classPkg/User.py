
class User:
    data = {
        'contents': [
            {
                'theme': '百大美女',
                'name': 'Nancy',
                'url': 'https://i.pinimg.com/originals/64/a0/16/64a01625ac17786a36cc08a6bae72c0f.jpg'
            },
            {
                'theme': '百大美女',
                'name': 'Josie Lane',
                'url': 'https://i.pinimg.com/originals/d5/0a/16/d50a16b42370131b08e19b9b57cb444b.png'
            },
            {
                'theme': '百大美女',
                'name': 'NANA',
                'url': 'https://upload.wikimedia.org/wikipedia/commons/e/e4/180503_%EB%82%98%EB%82%98.png'
            },
            {
                'theme': '百大美女',
                'name': 'Yuna',
                'url': 'https://img1.kpopmap.com/2019/08/itzy-yuna-jyp-41.jpg'
            },
            {
                'theme': '百大美女',
                'name': 'Thylane Blondeau',
                'url': 'https://imgix.bustle.com/wmag/2017/09/21/59c4217d7b31a9470fb3b40b_21576906_935057256642476_6867901006953316352_n.jpg?w=1200&fit=crop&crop=faces&auto=format%2Ccompress'
            },
            {
                'theme': '百大美女',
                'name': '周子瑜',
                'url': 'https://img.ltn.com.tw/Upload/ent/page/800/2020/08/22/3267861_1.jpg'
            },
            {
                'theme': '百大美女',
                'name': 'Meika Woollard',
                'url': 'https://az617363.vo.msecnd.net/imgmodels/models/MD50000633/meika_12d7ac7ae6673b9d888bfe8fd8b4f76a02.jpg'
            },
            {
                'theme': '百大美女',
                'name': 'Yael Shelbia',
                'url': 'https://knowinsiders.com/stores/news_dataimages/lyht/042021/19/18/5343_Yael-Shelbia-3.jpg?rt=20210419185537'
            }
        ]
    }

    __log: list
    __theme: str
    __step: str
    __pick: str
    __throw: str

    def __init__(self, user_id, msg):
        self.__user_id = user_id
        self.translate(msg)

    def get_id(self):
        return self.__user_id

    def get_data(self, index):
        return self.data['contents'][index]

    def getLog(self):
        return self.__log

    def translate(self, msg):
        self.__theme = msg[1:4]
        self.__step = msg[4:7]
        self.__pick = msg[7:12]
        self.__throw = msg[12:17]
