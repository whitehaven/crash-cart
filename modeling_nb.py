import marimo

__generated_with = "0.23.0"
app = marimo.App(width="medium")

with app.setup:
    import sympy as sy
    import marimo as mo

    (
        SV,
        E_es,
        EDV,
        P_es,
        V_0,
        P_ed,
        E_ed,
        k_Rhy,
        k_Rhy_NSR,
        k_Rhy_Afib,
        k_Rhy_VF,
        CO,
        HR,
        E_a,
        SBP,
        DBP,
        PP,
        C_a,
        T_d,
        tau,
        SVR,
    ) = sy.symbols(
        "SV E_es EDV P_es V_0 P_ed E_ed k_Rhy k_Rhy_NSR k_Rhy_Afib k_Rhy_VF CO HR E_a SBP DBP PP C_a T_d tau SVR"
    )


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    |Parameter           |Symbol              |Typical Value       |Units               |
    |--------------------|--------------------|--------------------|--------------------|
    |Inotropy            |$E_{es}$​                |2\.0 – 2\.5         |mmHg/mL             |
    |Arterial Afterload  |$E_a$​                 |1\.5 – 2\.2         |mmHg/mL             |
    |End\-Diastolic Volume|$EDV$                |120 – 140           |mL                  |
    |Preload \(LVEDP\)   |$P_{ed}$​                |5 – 12              |mmHg                |
    |Diastolic Stiffness |$E_{ed}$​                |0\.1 – 0\.2         |mmHg/mL             |
    |Unstressed Volume   |$V_0$​                 |0 – 20              |mL                  |
    |Heart Rate          |$HR$                  |60 – 80             |bpm                 |
    | End-Systolic Pressure | $P_{es}$ | 90-120 | mmHg|
    | Arterial Compliance | $C_a$ | 1.5-2.0 | mL/mmHg |
    | Time of diastole | $T_d$ | s |
    | Fall constant tau | $\tau$ | ? |
    """)
    return


@app.cell
def _():
    sy.Eq(SV,E_es*(EDV-V_0)/(E_es+E_a))
    return


@app.cell
def _():
    sy.Eq(SV,E_es*(EDV-V_0)/(E_es+E_a)).subs({EDV:V_0+P_ed/E_ed,V_0:20,E_es:2.0,E_a:1.5})
    return


@app.cell
def _():
    sy.Eq(SV,E_es*(EDV-V_0)/(E_es+E_a))
    return


@app.cell
def _():
    sy.Eq(EDV,V_0+P_ed/E_ed)
    return


@app.cell
def _():
    sy.Eq(EDV,V_0+P_ed/E_ed)
    return


@app.cell
def _():
    sy.Eq(CO,HR*SV*k_Rhy)
    return


@app.cell
def _():
    # the mega equation (linearized to hell though)
    sy.Eq(CO,HR*SV*k_Rhy).subs({SV:E_es*(EDV-V_0)/(E_es+E_a)}).subs({EDV:V_0+P_ed/E_ed})
    return


@app.cell
def _():
    # the mega equation (linearized to hell though)
    print(sy.Eq(CO,HR*SV*k_Rhy).subs({SV:E_es*(EDV-V_0)/(E_es+E_a)}).subs({EDV:V_0+P_ed/E_ed}))
    return


@app.cell
def _():
    sy.Eq(k_Rhy_NSR,1.0)
    return


@app.cell
def _():
    sy.Eq(k_Rhy_Afib,0.8)
    return


@app.cell
def _():
    sy.Eq(SBP,E_a*SV)
    return


@app.cell
def _():
    sy.Eq(PP, SBP - DBP)
    return


@app.cell
def _():
    sy.Eq(PP,SV/C_a).subs({SV:80,C_a:1.5})
    return


@app.cell
def _():
    sy.Eq(DBP,SBP*sy.exp(-T_d/tau))
    return


@app.cell
def _():
    sy.Eq(T_d,2/3*60/HR)
    return


@app.cell
def _():
    sy.Eq(tau,SVR*C_a)
    return


@app.cell
def _():
    sy.Eq(DBP,SBP*sy.exp(-T_d/tau)).subs({tau:SVR*C_a,T_d:2/3*60/HR,SBP:E_a*SV})
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
