from dictfilter import query


def _middleware(request, response):
    fields_param = request.GET.get("fields")

    if 200 <= response.status_code < 300:
        if not fields_param or fields_param == "*":
            query_fields = None
        else:
            query_fields = fields_param.split(",")

        if query_fields is not None:
            filtered_data = query(response.data, query_fields)

            # re-render the response
            response.data = filtered_data
            response._is_rendered = False
            response.render()

    return response


def dictfilter_middleware(get_response):
    def middleware(request):
        response = get_response(request)
        return _middleware(request, response)

    return middleware


class DictFilterMiddleware(object):
    def __init__(self, get_response=None):
        self.get_response = get_response
        super().__init__()

    def __call__(self, request):
        response = self.get_response(request)
        return _middleware(request, response)
