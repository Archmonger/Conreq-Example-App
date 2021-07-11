# App configuration parameters used by Conreq
AUTO_ADD_CSS = True
AUTO_ADD_JS = True
HEAD_HTML = "<TEMP>"
BODY_HTML = "<TEMP>"
INIT_COMMANDS = [  # Executable name of any Django admin management commands to be run at Conreq first boot
    ["run_huey", "--quiet"],
    ["clean_db", "-v"],
]
