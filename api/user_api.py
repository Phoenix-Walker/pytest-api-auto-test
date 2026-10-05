class UserApi:
    """用户相关接口封装类"""
    def __init__(self, session, base_url):
        self.session = session
        self.base_url = base_url

    def get_user(self, user_id):
        """
        获取单个用户信息
        :param user_id: 用户id
        :return: response对象
        """
        url = f"{self.base_url}/users/{user_id}"
        resp = self.session.get(url)
        return resp

    def create_post(self, payload):
        """
        新建帖子（post接口）
        :param payload: 请求体，字典
        :return: response对象
        """
        url = f"{self.base_url}/posts"
        resp = self.session.post(url, json=payload)
        return resp
