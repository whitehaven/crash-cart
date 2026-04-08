from nicegui import ui

# pyright: reportUnknownMemberType = false
# pyright: reportUnusedCallResult = false


@ui.page("/gm_view")
def gm_view():
    ui.label("GM View Here")


@ui.page("/")
def page():
    ui.label("Hello NiceGUI!")
    ui.link("Visit other page", target=gm_view)


ui.run()
