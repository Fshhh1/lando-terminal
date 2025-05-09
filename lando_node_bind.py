from lando.lando_core import LandoCore
from lando.agent_router import AgentRouter
from lando.treaty_engine import TreatyEngine

lando = LandoCore()
lando.activate()

router = AgentRouter()
router.route_message("chips://admin", "Lando node active")

treaty = TreatyEngine()
treaty.validate_treaty({"ethics": "compliant"})