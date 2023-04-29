from app.common.utils.rights import authorize
from app.views.auth import register_auth_views
from app.views.main import register_main_views


def init_view(app):
    @app.context_processor
    def inject_authorize():
        """
            注册一个检测权限的函数
        :return:
        """
        return dict(authorize=authorize)

    """
    :param app:
    """
    register_main_views(app)
    register_auth_views(app)
