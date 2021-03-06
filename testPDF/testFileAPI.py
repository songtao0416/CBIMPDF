from flask import request, Flask, jsonify

from matplotlib import pyplot as plt
import sys
sys.path.append(r"F:\项目代码\Python代码\CBIM设计说明文档识别")
from flask import Flask, request, jsonify
import json
from PDFCollect.serverPDF.apiJson import apiJson

app = Flask(__name__)


# 只接受get方法访问
@app.route("/test_01", methods=["POST"])
def check():
    # 默认返回内容
    return_dict = {'return_code': '200', 'return_info': '处理成功', 'result': False}
    # 判断入参是否为空
    if request.form is None:
        return_dict['return_code'] = '5004'
        return_dict['return_info'] = '请求参数为空'
        return json.dumps(return_dict, ensure_ascii=False)

    ff = request.files.get('pdfPath')
    # fname = request.files.get('pdfName')
    # 获取传入的params参数
    # get_data = request.args.to_dict()

    # get_data = request.form.to_dict()
    # get_data = eval(requestJsonString.k)
    # print(get_data)
    # pdfPath = get_data.get('pdfPath')
    # pdfName = get_data.get('pdfName')
    # pdfType = get_data.get('pdfType')
    # pdfMajor = get_data.get('pdfMajor')
    # print(pdfMajor, pdfName, pdfType)
    # 对参数进行操作
    # if pdfMajor == "建筑":
    #     if pdfType == "1":
    #         return_dict['result'] = tt(pdfPath, pdfName)
    # else:
    #     return_dict['return_code'] = '5001'
    #     return_dict['return_info'] = 'PDF类型无法识别'
    return_dict['result'] = tt(ff, pdfName=1)
    return json.dumps(return_dict, ensure_ascii=False)



# 功能函数
def tt(pdfPath, pdfName):
    print(pdfPath)
    result_str = apiJson(pdfPath, pdfName).apiJson
    # result_str = "ok"
    return result_str


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9200, debug=True)
