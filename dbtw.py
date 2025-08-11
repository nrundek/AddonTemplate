# -*- coding: UTF-8 -*-
import appModuleHandler
import ui
import api
from logHandler import log
import globalCommands

class AppModule(appModuleHandler.AppModule):
    """
    Duxbury (dbtw.exe) AppModule — Alt+9 Read status bar.
    1) Calls NVDA’s built-in “report status line” script (like Insert+End).
    2) Fallback: api.getStatusBarText().
    """

    __gestures = {
        "kb:alt+9": "reportDuxburyStatus",
        "kb(laptop):alt+9": "reportDuxburyStatus",
        "kb:alt+numpad9": "reportDuxburyStatus",
    }

    def script_reportDuxburyStatus(self, gesture):
        # 1) Try NVDA's built-in script (speaks the status bar directly)
        try:
            globalCommands.commands.script_reportStatusLine(None)
            return
        except Exception as e:
            log.debug(f"dbtw_alt9_statusline: globalCommands.script_reportStatusLine failed: {e!r}")

        # 2) Fallback: NVDA API
        try:
            t = api.getStatusBarText()
            if t:
                ui.message(t.strip())
                return
        except Exception as e:
            log.debug(f"dbtw_alt9_statusline: api.getStatusBarText failed: {e!r}")

        ui.message("Status bar not available.")

    script_reportDuxburyStatus.__doc__ = "Read status bar (Alt+9)."
