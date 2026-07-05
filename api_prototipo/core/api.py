from ninja import NinjaAPI
from users.router import router as users_router
from clubs.router import router as clubs_router
from manager.router import router as manager_router



nucleo = NinjaAPI()

nucleo.add_router('users/', users_router)
nucleo.add_router('clubs/', clubs_router)
nucleo.add_router('manager/', manager_router)
