from nicegui import ui

# pyright: reportUnknownMemberType = false
# pyright: reportUnusedCallResult = false

systolic = 120
diastolic = 80
heart_rate = 75


@ui.page("/gm_view")
def gm_view():
    ui.label("Vitals Control").classes("text-2xl font-bold")
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

        with ui.row().classes("items-center gap-4"):
            ui.label("Heart Rate:")
            hr_input = ui.number(value=heart_rate, min=20, max=250).props("outlined")
            ui.label("bpm")

        def update_display():
            global systolic, diastolic, heart_rate
            systolic = systolic_input.value
            diastolic = diastolic_input.value
            heart_rate = hr_input.value
            ui.notify(
                f"Updated: BP {round(systolic)}/{round(diastolic)}, HR {round(heart_rate)}", color="positive"
            )

        ui.button("Update Player Display", on_click=update_display).props(
            "color=primary"
        )


@ui.page("/")
def page():
    ui.label("Vitals").classes("text-2xl font-bold")
    with ui.card().classes("text-center"):
        ui.label("Blood Pressure").classes("text-lg")
        bp_label = ui.label(f"{systolic}/{diastolic}").classes("text-5xl font-bold")
        ui.label("mmHg")

    with ui.card().classes("text-center"):
        ui.label("Heart Rate").classes("text-lg")
        hr_label = ui.label(f"{heart_rate}").classes("text-5xl font-bold")
        ui.label("bpm")

    def update_vitals():
        bp_label.text = f"{round(systolic)}/{round(diastolic)}"
        hr_label.text = f"{round(heart_rate)}"

    ui.timer(0.5, update_vitals)

    ui.link("Open GM Control Panel", target=gm_view).classes("mt-4")


ui.run()
