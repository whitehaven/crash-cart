from nicegui import ui
from math import exp

# pyright: reportUnknownMemberType = false
# pyright: reportUnusedCallResult = false

E_es = 2.0
HR = 60
P_ed = 10
k_Rhy = 1.0
E_ed = 0.1
E_a = 2.0
C_a = 1.5
SVR = 20
T_d = 0.3

sbp = 120
dbp = 80
hr = 75

prev_E_es = E_es
prev_HR = HR
prev_P_ed = P_ed
prev_k_Rhy = k_Rhy
prev_E_ed = E_ed
prev_E_a = E_a
prev_C_a = C_a
prev_SVR = SVR
prev_T_d = T_d


@ui.page("/gm_view")
def gm_view():
    ui.label("Vitals Control").classes("text-2xl font-bold")

    with ui.card():
        ui.label("Model Parameters (Internal)").classes("font-bold")
        with ui.row().classes("items-center gap-4"):
            ui.label("E_es:")
            e_es_input = ui.number(value=E_es, min=0.1, max=10, step=0.1).props(
                "outlined"
            )
        with ui.row().classes("items-center gap-4"):
            ui.label("HR:")
            hr_param_input = ui.number(value=HR, min=20, max=250).props("outlined")
        with ui.row().classes("items-center gap-4"):
            ui.label("P_ed:")
            p_ed_input = ui.number(value=P_ed, min=0, max=50).props("outlined")
        with ui.row().classes("items-center gap-4"):
            ui.label("k_Rhy:")
            k_rhy_input = ui.number(value=k_Rhy, min=0.1, max=5, step=0.1).props(
                "outlined"
            )
        with ui.row().classes("items-center gap-4"):
            ui.label("E_ed:")
            e_ed_input = ui.number(value=E_ed, min=0.01, max=5, step=0.01).props(
                "outlined"
            )
        with ui.row().classes("items-center gap-4"):
            ui.label("E_a:")
            e_a_input = ui.number(value=E_a, min=0.1, max=10, step=0.1).props(
                "outlined"
            )
        with ui.row().classes("items-center gap-4"):
            ui.label("C_a:")
            c_a_input = ui.number(value=C_a, min=0.1, max=5, step=0.1).props("outlined")
        with ui.row().classes("items-center gap-4"):
            ui.label("SVR:")
            svr_input = ui.number(value=SVR, min=5, max=50).props("outlined")
        with ui.row().classes("items-center gap-4"):
            ui.label("T_d:")
            t_d_input = ui.number(value=T_d, min=0.01, max=2, step=0.01).props(
                "outlined"
            )

        with ui.column().classes("gap-2 mt-4"):
            ui.label("Calculated Values:").classes("font-bold")
            with ui.row().classes("items-center gap-4"):
                ui.label("tau:")
                tau_label = ui.label("0.00")
            with ui.row().classes("items-center gap-4"):
                ui.label("SV:")
                sv_label = ui.label("0.00")
            with ui.row().classes("items-center gap-4"):
                ui.label("CO:")
                co_label = ui.label("0.00")
            with ui.row().classes("items-center gap-4"):
                ui.label("SBP:")
                sbp_label = ui.label("0.00")
            with ui.row().classes("items-center gap-4"):
                ui.label("DBP:")
                dbp_label = ui.label("0.00")

        def recalculate():
            tau = c_a_input.value * svr_input.value
            sv = (
                e_es_input.value
                * p_ed_input.value
                * k_rhy_input.value
                / (e_ed_input.value * (e_a_input.value + e_es_input.value))
            )
            co = sv * hr_param_input.value
            sbp = e_a_input.value * sv
            dbp = sbp * exp(-t_d_input.value / tau)
            tau_label.text = f"{tau:.2f}"
            sv_label.text = f"{sv:.2f}"
            co_label.text = f"{co:.2f}"
            sbp_label.text = f"{sbp:.2f}"
            dbp_label.text = f"{dbp:.2f}"

        e_es_input.on_value_change(recalculate)
        hr_param_input.on_value_change(recalculate)
        p_ed_input.on_value_change(recalculate)
        k_rhy_input.on_value_change(recalculate)
        e_ed_input.on_value_change(recalculate)
        e_a_input.on_value_change(recalculate)
        c_a_input.on_value_change(recalculate)
        svr_input.on_value_change(recalculate)
        t_d_input.on_value_change(recalculate)

        recalculate()

    with ui.card():

        def update_display():
            global \
                sbp, \
                dbp, \
                hr, \
                prev_E_es, \
                prev_HR, \
                prev_P_ed, \
                prev_k_Rhy, \
                prev_E_ed, \
                prev_E_a, \
                prev_C_a, \
                prev_SVR, \
                prev_T_d
            changed = []
            if e_es_input.value != prev_E_es:
                changed.append(f"E_es: {prev_E_es:.2f} -> {e_es_input.value:.2f}")
            if hr_param_input.value != prev_HR:
                changed.append(f"HR: {prev_HR} -> {hr_param_input.value}")
            if p_ed_input.value != prev_P_ed:
                changed.append(f"P_ed: {prev_P_ed:.2f} -> {p_ed_input.value:.2f}")
            if k_rhy_input.value != prev_k_Rhy:
                changed.append(f"k_Rhy: {prev_k_Rhy:.2f} -> {k_rhy_input.value:.2f}")
            if e_ed_input.value != prev_E_ed:
                changed.append(f"E_ed: {prev_E_ed:.2f} -> {e_ed_input.value:.2f}")
            if e_a_input.value != prev_E_a:
                changed.append(f"E_a: {prev_E_a:.2f} -> {e_a_input.value:.2f}")
            if c_a_input.value != prev_C_a:
                changed.append(f"C_a: {prev_C_a:.2f} -> {c_a_input.value:.2f}")
            if svr_input.value != prev_SVR:
                changed.append(f"SVR: {prev_SVR:.2f} -> {svr_input.value:.2f}")
            if t_d_input.value != prev_T_d:
                changed.append(f"T_d: {prev_T_d:.2f} -> {t_d_input.value:.2f}")

            tau = c_a_input.value * svr_input.value
            sv = (
                e_es_input.value
                * p_ed_input.value
                * k_rhy_input.value
                / (e_ed_input.value * (e_a_input.value + e_es_input.value))
            )
            sbp = e_a_input.value * sv
            dbp = sbp * exp(-t_d_input.value / tau)
            hr = hr_param_input.value

            prev_E_es = e_es_input.value
            prev_HR = hr_param_input.value
            prev_P_ed = p_ed_input.value
            prev_k_Rhy = k_rhy_input.value
            prev_E_ed = e_ed_input.value
            prev_E_a = e_a_input.value
            prev_C_a = c_a_input.value
            prev_SVR = svr_input.value
            prev_T_d = t_d_input.value

            if changed:
                ui.notify(
                    f"Updated: {', '.join(changed)}",
                    color="positive",
                )
            else:
                ui.notify("No changes detected", color="warning")

        ui.button("Update Player Display", on_click=update_display).props(
            "color=primary"
        )


@ui.page("/")
def page():
    ui.label("Vitals").classes("text-2xl font-bold")
    with ui.card().classes("text-center"):
        ui.label("Blood Pressure").classes("text-lg")
        bp_label = ui.label(f"{round(sbp)}/{round(dbp)}").classes("text-5xl font-bold")
        ui.label("mmHg")

    with ui.card().classes("text-center"):
        ui.label("Heart Rate").classes("text-lg")
        hr_label = ui.label(f"{round(hr)}").classes("text-5xl font-bold")
        ui.label("bpm")

    def update_vitals():
        bp_label.text = f"{round(sbp)}/{round(dbp)}"
        hr_label.text = f"{round(hr)}"

    ui.timer(0.5, update_vitals)

    ui.link("Open GM Control Panel", target=gm_view).classes("mt-4")


ui.run()
