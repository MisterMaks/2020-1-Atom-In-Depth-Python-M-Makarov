import logging


logging.basicConfig(format=u'%(levelname)-8s [%(asctime)s] %(message)s',
                    level=logging.INFO,
                    filename=u'logs/multiplication_elements_list_without_current.log')


def multiplication_elements_list_without_current(lst):
    result_list = []
    try:
        for i in range(len(lst)):
            num = 1
            for j in range(len(lst)):
                if type(lst[j]) not in [int, float]:
                    logging.error(f"type(element) in users list input not int or float")
                    return None
                if len(lst) in [0, 1]:
                    return []
                if j != i:
                    try:
                        num *= lst[j]
                    except Exception as error:
                        logging.error(f'error in elements in users list input: {error}')
            result_list.append(num)
        return result_list
    except Exception as error:
        logging.error(f'list iteration error for users input: {error}')
