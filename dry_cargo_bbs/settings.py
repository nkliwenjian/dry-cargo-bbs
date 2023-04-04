from dry_cargo_bbs.project_settings.django_settings import * # noqa isort:skip

try:
    from dry_cargo_bbs.local_settings import *
except:
    import traceback; traceback.print_exc()
