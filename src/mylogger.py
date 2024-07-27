import logging

def setup_logging(log_path):
    # 配置日志记录
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_path, encoding='utf-8'),  # 日志记录到文件
            logging.StreamHandler()  # 日志记录到控制台
        ]
    )

    