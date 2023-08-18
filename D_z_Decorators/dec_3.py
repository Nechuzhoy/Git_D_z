import logging
import json
def logger(path):
    def _logger(old_function):
        def new_function(*args, **kwargs):
            logger = logging.getLogger(__name__)
            logger.setLevel(logging.INFO)
            log_file = path
            log_format = "%(asctime)s %(levelname)s %(message)s"
            formatter = logging.Formatter(log_format)

            file_handler = logging.FileHandler(log_file)
            file_handler.setFormatter(formatter)

            logger.addHandler(file_handler)

            result = old_function(*args, **kwargs)
            logger.info(f'{old_function}, with arguments {args} and {kwargs}, Result = {result}')
            return result
        return new_function
    return _logger
@logger('new.log')
def read_json(file_path):
    from operator import itemgetter
    with open(file_path, encoding="utf-8", newline="") as f:
        data = json.load(f)
    b = data["rss"]["channel"]["items"]
    list = [word for items in b for word in items["description"].split() if len(word) > 6]
    list2 = []
    list3 = []
    for i in list:
        if i not in list2:
            list2.append(i)
            list3.append([i, list.count(i)])

    res = (sorted(list3, key=itemgetter(1), reverse = True))
    del res[-10]
    del res[-10]

    c = [i[0] for i in res[:10]]
    return (list)


if __name__ == '__main__':
    print(read_json('newsafr.json'))