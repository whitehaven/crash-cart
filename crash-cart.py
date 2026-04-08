from nicegui import ui

# pyright: reportUnknownMemberType = false
# pyright: reportUnusedCallResult = false

systolic = 120
diastolic = 80


@ui.page("/gm_view")
def gm_view():
    ui.label("Blood Pressure Control").classes("text-2xl font-bold")
    with ui.card():
        with ui.row().classes("items-center gap-4"):
            ui.label("Systolic:")
            systolic_input = ui.number(value=systolic, min=60, max=250).props(
                "outlined"
            )
            ui.label("mmHg")

        with ui.row().classes("items-center gap-4"):
            ui.label("Diastolic:")
            diastolic_input = ui.number(value=diastolic, min=30, max=150).props(
                "outlined"
            )
            ui.label("mmHg")

        def update_display():
            global systolic, diastolic
            systolic = systolic_input.value
            diastolic = diastolic_input.value
            ui.notify(f"Updated to {systolic}/{diastolic} mmHg", color="positive")

        ui.button("Update Player Display", on_click=update_display).props(
            "color=primary"
        )


@ui.page("/")
def page():
    ui.label("Patient Vitals Display").classes("text-2xl font-bold")
    with ui.card().classes("text-center"):
        ui.label("Blood Pressure").classes("text-lg")
        bp_label = ui.label(f"{systolic}/{diastolic}").classes("text-5xl font-bold")
        ui.label("mmHg")

    def update_bp():
        bp_label.text = f"{systolic}/{diastolic}"

    ui.timer(0.5, update_bp)

    ui.link("Open GM Control Panel", target=gm_view).classes("mt-4")


ui.run()
