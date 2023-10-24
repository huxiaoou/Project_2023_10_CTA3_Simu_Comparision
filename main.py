import datetime as dt
from skyrim.whiterun import SetFontGreen, SetFontYellow
from simulation_fun import cal_simulations_mp, evaluate_simu
from lib_struct import database_structure, get_lib_struct_signals

if __name__ == "__main__":
    from config import signal_ids, proc_num, test_windows, calendar_path, instrument_info_path
    from config import md_by_instru_dir, major_minor_dir, available_universe_dir, sig_dir, simu_dir
    from config import concerned_instruments_universe, bgn_date, cost_reservation, cost_rate, minimum_weight_threshold
    from config import selected_indicators

    today, default_init_premium = dt.datetime.now().strftime("%Y%m%d"), "1000"
    stp_date = input(f"Please input the STP-DATE of simulation, format = [YYYYMMDD], default is {today}:") or today
    init_premium = input(f"Please input the init-premium, unit = WANYUAN, default = {default_init_premium}:") or default_init_premium
    init_premium = int(init_premium) * 1e4

    database_structure.update({_: get_lib_struct_signals(_) for _ in signal_ids})
    cal_simulations_mp(
        proc_num=proc_num, signal_ids=signal_ids, test_windows=test_windows,
        calendar_path=calendar_path, instrument_info_path=instrument_info_path,
        md_by_instru_dir=md_by_instru_dir, major_minor_dir=major_minor_dir, available_universe_dir=available_universe_dir,
        sig_dir=sig_dir, dst_dir=simu_dir,
        database_structure=database_structure, test_universe=concerned_instruments_universe,
        test_bgn_date=bgn_date, test_stp_date=stp_date,
        cost_reservation=cost_reservation, cost_rate=cost_rate, init_premium=init_premium,
        minimum_weight_threshold=minimum_weight_threshold,
        skip_if_exist=False,
    )

    print("=" * 120)
    print(f"init premium: {SetFontGreen(f'{init_premium/1e4:.2f} WANYUAN'):.>36s}")
    print(f"begin date  : {SetFontYellow(bgn_date):.>36s}")
    print(f"stop  date  : {SetFontYellow(stp_date):.>36s}")
    print(f"cost  rate  : {SetFontGreen(f'{cost_rate:.4f}'):.>36s}")
    print(f"min weight  : {SetFontGreen(f'{minimum_weight_threshold:.4f}'):.>36s}")
    print("-" * 120)
    evaluate_simu(
        signal_ids=signal_ids, simu_dir=simu_dir, hold_period_n=1, start_delay=0,
        selected_indicators=selected_indicators,
    )
    print("-" * 120, "\n")
