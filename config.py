import os

signal_ids = ["RF", "RD", "NF", "ND"]
test_windows = [1]
calendar_path = r"E:\Deploy\Data\Calendar\cne_calendar.csv"
instrument_info_path = r"E:\Deploy\Data\Futures\InstrumentInfo3.csv"
md_by_instru_dir = r"E:\Deploy\Data\Futures\by_instrument\by_instru_md"
major_minor_dir = r"E:\Deploy\Data\Futures\by_instrument"
available_universe_dir = r"E:\Deploy\Data\ForProjects\cta3\available_universe"
sig_dir = r"E:\Deploy\Data\ForProjects\cta3\signals\portfolios"
simu_dir = os.path.join(r"E:\ProjectsData", os.getcwd().split("\\")[-1])
if not os.path.exists(simu_dir):
    os.mkdir(simu_dir)

concerned_instruments_universe = [
    "AU.SHF",
    "AG.SHF",
    "CU.SHF",
    "AL.SHF",
    "PB.SHF",
    "ZN.SHF",
    "SN.SHF",
    "NI.SHF",
    "SS.SHF",
    "RB.SHF",
    "HC.SHF",
    "J.DCE",
    "JM.DCE",
    "I.DCE",
    "FG.CZC",
    "SA.CZC",
    "UR.CZC",
    "ZC.CZC",
    "SF.CZC",
    "SM.CZC",
    "Y.DCE",
    "P.DCE",
    "OI.CZC",
    "M.DCE",
    "RM.CZC",
    "A.DCE",
    "RU.SHF",
    "BU.SHF",
    "FU.SHF",
    "L.DCE",
    "V.DCE",
    "PP.DCE",
    "EG.DCE",
    "EB.DCE",
    "PG.DCE",
    "TA.CZC",
    "MA.CZC",
    "SP.SHF",
    "CF.CZC",
    "CY.CZC",
    "SR.CZC",
    "C.DCE",
    "CS.DCE",
    "JD.DCE",
    "LH.DCE",
    "AP.CZC",
    "CJ.CZC",
]
bgn_date = "20140701"
cost_rate, cost_reservation, minimum_weight_threshold = 5e-4, 0, 3e-3
proc_num = 5

selected_indicators = [
    "hold_period_return",
    "annual_return",
    "annual_volatility",
    "max_drawdown_scale",
    "sharpe_ratio",
    "calmar_ratio",
]
