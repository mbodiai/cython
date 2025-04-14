# SPDX-FileCopyrightText: 2024-present Sebastian Peralta <sebastian@mbodi.ai>
#
# SPDX-License-Identifier: apache-2.0
# Define the variable '__version__':

import asyncio
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning, module="rich_click")
warnings.filterwarnings("ignore", category=DeprecationWarning, module="click")
from mbcore.import_utils import smart_import

log = smart_import("mbcore.log")
try:
    log.setup_logging()
except:
    pass
try:
    log.setup_traceback()
except:
    pass
try:
    import uvloop

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
except ImportError:
    pass



LIGHT_CYAN_BOLD = "#87d7ff"
CYAN_BOLD = "#00ffff"
PINK_BOLD = "#ffafd7"
LIGHT_BLUE = "#afd7ff"
LIGHT_BLUE_BOLD = "#afd7ff"
RESET = ""  # Resetting the color, no hex value
PINK = "#ffafd7"
PINK_BOLD = "bold #ffd7e5"
GOLD_BOLD = "bold #ffd7af"
WHITE_BOLD = "bold white"
PINK = "#ffd7e5"
GOLD = "#ffd7af"
THEME = {
    "info": f"{LIGHT_CYAN_BOLD}",
    "success": f"{LIGHT_BLUE}",
    "light_blue": f"{LIGHT_BLUE_BOLD}",
    "reset": RESET,
    "pink": f"{PINK}",
}
