from app.views.main import register_main_views
from app.views.auth import register_auth_views


def init_view(app):
    """

    :param app:
    """
    register_main_views(app)
    register_auth_views(app)