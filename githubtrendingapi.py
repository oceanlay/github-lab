import requests
from sqlalchemy import desc, create_engine, Column, Integer, String, Text  # 降序、连接路径、列、字符串、文本
from sqlalchemy.orm import scoped_session, sessionmaker  # 代理模式、数据库连接的媒（手机）；engine号码
from sqlalchemy.ext.declarative import declarative_base  # 声明类映射类到表的关系

# 抓取URL
url = 'http://132.232.132.144:8009/api?lang=python&since=daily'
response = requests.get(url)
# 解析内容
response_dict = response.json()
print(response_dict.keys())
print('success:', response_dict['success'])
print('count:', response_dict['count'])
repositories = response_dict['msg']
print(repositories, 'msg:')
print(repositories[0]['repo'])

# 加入数据库保存数据#
# DB = {'HOST': '127.0.0.1', 'PORT': '3306', 'DB_NAME': 'oceanlay',  'USER': 'root',  'PASSWORD': '19981010',  'CHARSET': 'utf8mb4'}
# 创建连接:'数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
engine = create_engine('mysql+pymysql://root:19981010@localhost:3306/oceanlay?charset=utf8mb4')

# 连接数据库的路径。
# “mysql+mysqldb”指定了使用 MySQL-Python 来连接，
# 声明类 类到表的关系
Base = declarative_base()


# 定义python类
class Api(Base):
    __tablename__ = 'api'
    id = Column(Integer, primary_key=True)
    repo = Column(String(128))  # repository name
    language = Column(String(128))  # repository language
    user = Column(String(128))  # user
    stars = Column(String(128))
    forks = Column(String(128))
    about = Column(String(10000))
    link = Column(String(10000))

    new_stars = Column(String(10000))
    avatars = Column(String(10000))
    def __repr__(self):
        return "<Api(id='%s',repo=%s,language=%s,user=%s,stars=%d,forks=%d,about=%s,link=%s,new_stars=%s,avatars=%s)>" \
               % (self.repo, self.language, self.user, self.stars, self.forks, self.about,self.link, self.new_stars,self.avatars)


# 创建数据表
Base.metadata.create_all(engine)

# 向表中插入数据
DBSession = sessionmaker(bind=engine)
session = DBSession()
for res in repositories:
    language = res['language']
    user = res['user']
    stars = res['stars']
    repo = res['repo']
    forks = res['forks']
    about = res['about']
    link = res['link']
    new_stars = res['new_stars']
    avatars = res['avatars']

    api_info = {
        # 项目名称
        'repo': repo,
        # 语言
        'language': language,
        # 仓库拥有者
        'user': user,
        # star数
        'stars': stars,
        # fork数
        'forks': forks,
        # 描述
        'about': res['about'],
        # 链接
        'link': res['link'],
        # 新增star
        'new_stars': res['new_stars'],
        # 头像
        'avatars': res['avatars']

    }
    # 写入数据
    session.add(
        Api(repo=api_info['repo'], language=api_info['language'], user=api_info['user'], stars=api_info['stars'],
            forks=api_info['forks'], about=api_info['about'], link=api_info['link'], new_stars=api_info['new_stars'],
            avatars=str(api_info['avatars'])
            ))
    session.commit()
    session.close()
    session.flush()

for res in repositories:
    print("仓库名:{repo}\n语言:{language}\n用户:{user}\nstars:{stars}\nforks:{forks}\n项目描述about:{about}\n网址:{link}\n关注者头像:{avatars}".format(repo=res['repo'], language=res['language'],  user=res['user'], stars=res['stars'],
                  forks=res['forks'], about=res['about'], link=res['link'],avatars=res['avatars']))
