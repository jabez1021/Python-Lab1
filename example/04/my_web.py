class Web():
    def get_result(self, keyword):
        result = []
        for t in range(10):
            result.append(keyword + " result: " + str(t))

        return result
