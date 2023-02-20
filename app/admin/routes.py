import typing

from app.admin.views import AdminCurrentView

if typing.TYPE_CHECKING:
    from app.web.app import Application


def setup_routes(app: "Application"):
    from app.admin.views import AdminLoginView
    from app.admin.views import AdminCurrentView
    
    from app.admin.views import IndexView
    
    app.router.add_view("/index", IndexView)

    app.router.add_view("/admin.login", AdminLoginView)
    app.router.add_view("/admin.current", AdminCurrentView)