# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin

class TerminalmessagingPlugin(octoprint.plugin.AssetPlugin):

    def get_assets(self):
        return dict(
            js=["js/terminalmessaging.js"],
            css=["css/terminalmessaging.css"]
        )

    def get_update_information(self):
        return dict(
            terminalmessaging=dict(
                displayName="Terminal Messaging",
                displayVersion=self._plugin_version,

                # version check: github repository
                type="github_release",
                user="jeffeb3",
                repo="OctoPrint-TerminalMessaging",
                current=self._plugin_version,

                # update method: pip
                pip="https://github.com/jeffeb3/OctoPrint-TerminalMessaging/archive/{target_version}.zip"
            )
        )


__plugin_name__ = "Terminal Messaging"
__plugin_pythoncompat__ = ">=2.7,<4" # python 2 and 3


def __plugin_load__():
    global __plugin_implementation__
    __plugin_implementation__ = TerminalmessagingPlugin()

    global __plugin_hooks__
    __plugin_hooks__ = {
        "octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
    }

