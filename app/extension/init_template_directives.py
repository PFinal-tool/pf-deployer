from flask import current_app, session
from flask_login import current_user


def init_template_directives(app):
    """

    :param app:
    :return:
    """
    @app.template_global()
    def authorize(power):
        """

        :param power:
        :return:
        """
        if current_user.username != current_app.config.get("SUPERADMIN"):
            return bool(power in session.get('permissions'))
        else:
            return True
