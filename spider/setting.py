# settings.py

# MYSQL
MYSQL_IP = "localhost"
MYSQL_PORT = 3306
MYSQL_DB = "feapder"
MYSQL_USER_NAME = "root"
MYSQL_USER_PASS = "123456"

#Redis
REDISDB_IP_PORTS = "localhost:6379"
REDISDB_USER_PASS = ""
REDISDB_DB = 0

# 浏览器渲染
WEBDRIVER = dict(
    pool_size=1,  # 浏览器的数量
    load_images=False,  # 是否加载图片
    user_agent=None,  # 字符串 或 无参函数，返回值为user_agent
    proxy=None,  # xxx.xxx.xxx.xxx:xxxx 或 无参函数，返回值为代理地址
    headless=False,  # 是否为无头浏览器
    driver_type="CHROME",  # CHROME、PHANTOMJS、FIREFOX
    timeout=30,  # 请求超时时间
    window_size=(1024, 800),  # 窗口大小
    executable_path=None,  # 浏览器路径，默认为默认路径
    render_time=0,  # 渲染时长，即打开网页等待指定时间后再获取源码
    custom_argument=[
        "--ignore-certificate-errors",
        "--disable-blink-features=AutomationControlled",
    ],  # 自定义浏览器渲染参数
    xhr_url_regexes=None,  # 拦截xhr接口，支持正则，数组类型
    auto_install_driver=False,  # 自动下载浏览器驱动 支持chrome 和 firefox
    download_path=None,  # 下载文件的路径
    use_stealth_js=False,  # 使用stealth.min.js隐藏浏览器特征
)
