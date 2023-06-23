"""
自定义中间件-实现登录验证（类似路由守卫）
"""
from django.http import JsonResponse
from django.shortcuts import redirect

# 需要登录才能访问的资源路径
LOGIN_REQUIRED_URLS = {'/blog/praise/', '/blog/criticize/',
                       '/blog/excel/', '/blog/teachers_data/'}


def check_login_middleware(get_resp):

    def wrapper(request, *args, **kwargs):
        # 请求的资源路径在上面的集合中
        if request.path in LOGIN_REQUIRED_URLS:
            # 会话中包含userid则视为已经登录
            if 'userid' not in request.session:
                # 判断是不是Ajax请求
                if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
                    # Ajax请求返回JSON数据提示用户登录
                    return JsonResponse({'code': 10003, 'hint': '请先登录'})
                else:
                    backurl = request.get_full_path()
                    # 非Ajax请求直接重定向到登录页
                    return redirect(f'/blog/login/?backurl={backurl}')
        return get_resp(request, *args, **kwargs)

    return wrapper
