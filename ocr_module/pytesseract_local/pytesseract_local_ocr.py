 
from . import ocr


def is_need_keys():
    return False

#def set_keys(ak, sk):
    #ocr.set_key(ak, sk)


def get_result(img) -> str:
    result = ocr.tesseract_ocr(img)
    if len(result) != 4:
        raise Exception("error: can not reco ocr data")
    else:
        return result
    #TODO
    #if res.__contains__('error_msg'):
        #raise Exception(res['error_msg'])
    #else:
        #return res['words_result'][0]['words']
