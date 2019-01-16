# encoding=utf-8
# __author__=zhangxiang


class JsonParse():
    '''
    递归解析json
    '''

    def get_target_value(self, key, inputJson, tmp_list):

        if not isinstance(inputJson, dict) or not isinstance(tmp_list, list):
            return print('解析的数据类型不是dict或list')

        if key in inputJson.keys():
            tmp_list.append(inputJson[key])
        else:
            for value in inputJson.values():
                if isinstance(value, dict):
                    self.get_target_value(key, value, tmp_list)
                elif isinstance(value, (list, tuple)):
                    self._get_value(key, value, tmp_list)
        return tmp_list

    def _get_value(self, key, val, tmp_list):
        for val_ in val:
            if isinstance(val_, dict):
                self.get_target_value(key, val_, tmp_list)
            elif isinstance(val_, (list, tuple)):
                self._get_value(key, val_, tmp_list)
